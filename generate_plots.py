#!/usr/bin/env python3
"""
Script to generate and save all visualizations from the GDP analysis project.
This script runs through all notebooks and saves plots to outputs/plots/
"""

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import warnings
warnings.filterwarnings('ignore')

# Set up paths
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(project_root, 'src'))
data_path = os.path.join(project_root, 'data')
output_path = os.path.join(project_root, 'outputs', 'plots')

# Create output directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

# Import utility functions
try:
    from utils import get_continent_mapping
except ImportError:
    print("Warning: Could not import utils. Creating continent mapping manually.")
    def get_continent_mapping():
        return {
            'Afghanistan': 'Asia', 'Albania': 'Europe', 'Algeria': 'Africa',
            'Argentina': 'South America', 'Australia': 'Oceania', 'Austria': 'Europe',
            'Bangladesh': 'Asia', 'Belgium': 'Europe', 'Brazil': 'South America',
            'Canada': 'North America', 'China': 'Asia', 'Egypt': 'Africa',
            'France': 'Europe', 'Germany': 'Europe', 'India': 'Asia',
            'Indonesia': 'Asia', 'Italy': 'Europe', 'Japan': 'Asia',
            'Kenya': 'Africa', 'Mexico': 'North America', 'Nigeria': 'Africa',
            'Norway': 'Europe', 'Pakistan': 'Asia', 'Russia': 'Europe',
            'South Africa': 'Africa', 'South Korea': 'Asia', 'Spain': 'Europe',
            'Sweden': 'Europe', 'Turkey': 'Asia', 'United Kingdom': 'Europe',
            'United States': 'North America'
        }

def load_and_prepare_data():
    """Load and prepare the GDP dataset"""
    print("📊 Loading GDP dataset...")
    
    # Load data
    df = pd.read_csv(os.path.join(data_path, 'gdp-per-capita-worldbank.csv'))
    
    # Add continent mapping
    continent_mapping = get_continent_mapping()
    df['Continent'] = df['Entity'].map(continent_mapping)
    
    # Clean data
    gdp_column = 'GDP per capita, PPP (constant 2021 international $)'
    df_clean = df.dropna(subset=[gdp_column])
    df_clean = df_clean[df_clean[gdp_column] > 0]
    
    print(f"✅ Data loaded: {len(df_clean)} records, {df_clean['Entity'].nunique()} countries")
    return df_clean, gdp_column

def save_plot(fig, filename, plot_type='matplotlib'):
    """Save plot to outputs/plots/ directory"""
    if plot_type == 'matplotlib':
        filepath = os.path.join(output_path, f"{filename}.png")
        fig.savefig(filepath, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"💾 Saved: {filename}.png")
    elif plot_type == 'plotly':
        # Save as both HTML and PNG
        html_path = os.path.join(output_path, f"{filename}.html")
        png_path = os.path.join(output_path, f"{filename}.png")
        
        fig.write_html(html_path)
        try:
            fig.write_image(png_path, width=1200, height=800, scale=2)
            print(f"💾 Saved: {filename}.html and {filename}.png")
        except Exception as e:
            print(f"💾 Saved: {filename}.html (PNG save failed: {e})")

def generate_data_exploration_plots(df, gdp_column):
    """Generate plots from data exploration notebook"""
    print("\n🔍 Generating Data Exploration Plots...")
    
    # 1. GDP Distribution Histogram
    plt.figure(figsize=(12, 6))
    plt.hist(df[gdp_column], bins=50, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title('Distribution of GDP Per Capita (2021 International $)', fontsize=16, fontweight='bold')
    plt.xlabel('GDP Per Capita (USD)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.grid(True, alpha=0.3)
    save_plot(plt.gcf(), "01_gdp_distribution")
    plt.close()
    
    # 2. Data Completeness by Year
    yearly_count = df.groupby('Year')['Entity'].count()
    plt.figure(figsize=(14, 6))
    plt.plot(yearly_count.index, yearly_count.values, marker='o', linewidth=2, markersize=6)
    plt.title('Data Availability by Year', fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Countries', fontsize=12)
    plt.grid(True, alpha=0.3)
    save_plot(plt.gcf(), "02_data_availability")
    plt.close()
    
    # 3. Top and Bottom Countries (Latest Year)
    latest_year = df['Year'].max()
    latest_data = df[df['Year'] == latest_year].sort_values(gdp_column, ascending=False)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Top 10
    top_10 = latest_data.head(10)
    ax1.barh(range(len(top_10)), top_10[gdp_column], color='lightgreen')
    ax1.set_yticks(range(len(top_10)))
    ax1.set_yticklabels(top_10['Entity'])
    ax1.set_title(f'Top 10 Countries by GDP Per Capita ({latest_year})', fontweight='bold')
    ax1.set_xlabel('GDP Per Capita (USD)')
    
    # Bottom 10
    bottom_10 = latest_data.tail(10)
    ax2.barh(range(len(bottom_10)), bottom_10[gdp_column], color='lightcoral')
    ax2.set_yticks(range(len(bottom_10)))
    ax2.set_yticklabels(bottom_10['Entity'])
    ax2.set_title(f'Bottom 10 Countries by GDP Per Capita ({latest_year})', fontweight='bold')
    ax2.set_xlabel('GDP Per Capita (USD)')
    
    plt.tight_layout()
    save_plot(fig, "03_top_bottom_countries")
    plt.close()

def generate_eda_plots(df, gdp_column):
    """Generate plots from EDA analysis notebook"""
    print("\n📈 Generating EDA Analysis Plots...")
    
    # 1. World GDP Trend Over Time
    world_avg = df.groupby('Year')[gdp_column].mean()
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=world_avg.index,
        y=world_avg.values,
        mode='lines+markers',
        name='World Average',
        line=dict(width=3, color='#2E86AB'),
        marker=dict(size=6)
    ))
    
    fig.update_layout(
        title='World Average GDP Per Capita Trend (1990-2023)',
        xaxis_title='Year',
        yaxis_title='GDP Per Capita (USD)',
        height=600,
        template='plotly_white'
    )
    save_plot(fig, "04_world_gdp_trend", 'plotly')
    
    # 2. Continental Comparison
    continent_data = df.groupby(['Year', 'Continent'])[gdp_column].mean().reset_index()
    
    fig = px.line(continent_data, x='Year', y=gdp_column, color='Continent',
                  title='GDP Per Capita by Continent Over Time',
                  labels={gdp_column: 'GDP Per Capita (USD)'})
    fig.update_layout(height=600, template='plotly_white')
    save_plot(fig, "05_continental_trends", 'plotly')
    
    # 3. Crisis Impact Analysis (2008 vs COVID)
    crisis_years = [2007, 2008, 2009, 2019, 2020, 2021]
    crisis_data = df[df['Year'].isin(crisis_years)]
    world_crisis = crisis_data.groupby('Year')[gdp_column].mean()
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=world_crisis.index,
        y=world_crisis.values,
        mode='lines+markers',
        name='World Average GDP',
        line=dict(width=3),
        marker=dict(size=8)
    ))
    
    # Add crisis annotations
    fig.add_vline(x=2008, line_dash="dash", line_color="red", 
                  annotation_text="2008 Financial Crisis")
    fig.add_vline(x=2020, line_dash="dash", line_color="red",
                  annotation_text="COVID-19 Pandemic")
    
    fig.update_layout(
        title='Economic Crisis Impact on Global GDP',
        xaxis_title='Year',
        yaxis_title='GDP Per Capita (USD)',
        height=600,
        template='plotly_white'
    )
    save_plot(fig, "06_crisis_impact", 'plotly')
    
    # 4. Wealth Inequality Analysis
    latest_year = df['Year'].max()
    latest_data = df[df['Year'] == latest_year].dropna(subset=[gdp_column])
    
    plt.figure(figsize=(14, 8))
    plt.hist(latest_data[gdp_column], bins=30, alpha=0.7, color='lightblue', edgecolor='black')
    plt.axvline(latest_data[gdp_column].mean(), color='red', linestyle='--', 
                label=f'Mean: ${latest_data[gdp_column].mean():,.0f}')
    plt.axvline(latest_data[gdp_column].median(), color='green', linestyle='--',
                label=f'Median: ${latest_data[gdp_column].median():,.0f}')
    
    plt.title(f'GDP Per Capita Distribution ({latest_year})', fontsize=16, fontweight='bold')
    plt.xlabel('GDP Per Capita (USD)', fontsize=12)
    plt.ylabel('Number of Countries', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    save_plot(plt.gcf(), "07_wealth_distribution")
    plt.close()

def generate_feature_engineering_plots(df, gdp_column):
    """Generate plots from feature engineering notebook"""
    print("\n🔧 Generating Feature Engineering Plots...")
    
    # Calculate growth rates for visualization
    df_sorted = df.sort_values(['Entity', 'Year'])
    df_sorted['yoy_growth'] = df_sorted.groupby('Entity')[gdp_column].pct_change() * 100
    
    # 1. Growth Rate Distribution
    growth_data = df_sorted.dropna(subset=['yoy_growth'])
    
    plt.figure(figsize=(12, 6))
    plt.hist(growth_data['yoy_growth'], bins=50, alpha=0.7, color='lightgreen', edgecolor='black')
    plt.title('Distribution of Year-over-Year GDP Growth Rates', fontsize=16, fontweight='bold')
    plt.xlabel('Growth Rate (%)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.axvline(0, color='red', linestyle='--', label='Zero Growth')
    plt.legend()
    plt.grid(True, alpha=0.3)
    save_plot(plt.gcf(), "08_growth_distribution")
    plt.close()
    
    # 2. Volatility Analysis (Major Economies)
    major_economies = ['United States', 'China', 'Germany', 'Japan', 'United Kingdom']
    volatility_data = []
    
    for country in major_economies:
        country_data = df_sorted[df_sorted['Entity'] == country]
        if len(country_data) > 5:
            volatility = country_data['yoy_growth'].std()
            avg_growth = country_data['yoy_growth'].mean()
            volatility_data.append({
                'Country': country,
                'Volatility': volatility,
                'Average_Growth': avg_growth
            })
    
    if volatility_data:
        vol_df = pd.DataFrame(volatility_data)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=vol_df['Volatility'],
            y=vol_df['Average_Growth'],
            mode='markers+text',
            text=vol_df['Country'],
            textposition='top center',
            marker=dict(size=12, color='blue', opacity=0.7),
            name='Countries'
        ))
        
        fig.update_layout(
            title='Growth Rate vs Volatility (Major Economies)',
            xaxis_title='Volatility (Standard Deviation of Growth %)',
            yaxis_title='Average Growth Rate (%)',
            height=600,
            template='plotly_white'
        )
        save_plot(fig, "09_volatility_analysis", 'plotly')

def generate_summary_dashboard():
    """Generate a comprehensive summary dashboard"""
    print("\n📊 Generating Summary Dashboard...")
    
    # Create a multi-panel summary plot
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Global GDP Analysis - Summary Dashboard', fontsize=20, fontweight='bold')
    
    # Load data for summary
    df, gdp_column = load_and_prepare_data()
    
    # Panel 1: World trend
    world_avg = df.groupby('Year')[gdp_column].mean()
    axes[0,0].plot(world_avg.index, world_avg.values, linewidth=2, color='blue')
    axes[0,0].set_title('World GDP Trend', fontweight='bold')
    axes[0,0].set_xlabel('Year')
    axes[0,0].set_ylabel('GDP Per Capita (USD)')
    axes[0,0].grid(True, alpha=0.3)
    
    # Panel 2: Continental comparison (latest year)
    latest_year = df['Year'].max()
    continent_latest = df[df['Year'] == latest_year].groupby('Continent')[gdp_column].mean().sort_values(ascending=True)
    axes[0,1].barh(range(len(continent_latest)), continent_latest.values, color='lightgreen')
    axes[0,1].set_yticks(range(len(continent_latest)))
    axes[0,1].set_yticklabels(continent_latest.index)
    axes[0,1].set_title(f'GDP by Continent ({latest_year})', fontweight='bold')
    axes[0,1].set_xlabel('GDP Per Capita (USD)')
    
    # Panel 3: Growth distribution
    df_sorted = df.sort_values(['Entity', 'Year'])
    df_sorted['yoy_growth'] = df_sorted.groupby('Entity')[gdp_column].pct_change() * 100
    growth_clean = df_sorted['yoy_growth'].dropna()
    axes[1,0].hist(growth_clean, bins=30, alpha=0.7, color='orange')
    axes[1,0].set_title('Growth Rate Distribution', fontweight='bold')
    axes[1,0].set_xlabel('Growth Rate (%)')
    axes[1,0].set_ylabel('Frequency')
    axes[1,0].axvline(0, color='red', linestyle='--')
    
    # Panel 4: Top performers (latest year)
    latest_data = df[df['Year'] == latest_year].sort_values(gdp_column, ascending=False).head(8)
    axes[1,1].bar(range(len(latest_data)), latest_data[gdp_column], color='lightcoral')
    axes[1,1].set_xticks(range(len(latest_data)))
    axes[1,1].set_xticklabels([entity[:8] + '...' if len(entity) > 8 else entity 
                               for entity in latest_data['Entity']], rotation=45)
    axes[1,1].set_title(f'Top Performers ({latest_year})', fontweight='bold')
    axes[1,1].set_ylabel('GDP Per Capita (USD)')
    
    plt.tight_layout()
    save_plot(fig, "10_summary_dashboard")
    plt.close()

def main():
    """Main function to generate all plots"""
    print("🎨 Starting plot generation for GDP Analysis Project...")
    print("=" * 60)
    
    try:
        # Load data
        df, gdp_column = load_and_prepare_data()
        
        # Generate all plot categories
        generate_data_exploration_plots(df, gdp_column)
        generate_eda_plots(df, gdp_column)
        generate_feature_engineering_plots(df, gdp_column)
        generate_summary_dashboard()
        
        print("\n" + "=" * 60)
        print("🎉 All visualizations have been generated successfully!")
        print(f"📁 Plots saved to: {output_path}")
        
        # List generated files
        plot_files = [f for f in os.listdir(output_path) if f.endswith(('.png', '.html'))]
        print(f"📊 Generated {len(plot_files)} visualization files:")
        for file in sorted(plot_files):
            print(f"  • {file}")
            
    except Exception as e:
        print(f"❌ Error generating plots: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()