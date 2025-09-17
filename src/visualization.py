"""
Visualization functions for GDP per capita analysis
Author: GitHub Portfolio Project
"""

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# Set style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def plot_world_gdp_trend(world_trends, gdp_column, save_path=None):
    """
    Plot world GDP per capita trend over time
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Main trend line  
    mean_col = f'{gdp_column}_mean' if f'{gdp_column}_mean' in world_trends.columns else gdp_column
    min_col = f'{gdp_column}_min' if f'{gdp_column}_min' in world_trends.columns else gdp_column
    max_col = f'{gdp_column}_max' if f'{gdp_column}_max' in world_trends.columns else gdp_column
    
    ax.plot(world_trends['Year'], world_trends[mean_col], 
            linewidth=3, marker='o', markersize=4, label='World Average', color='#2E86AB')
    
    # Fill between min and max if available
    if min_col in world_trends.columns and max_col in world_trends.columns:
        ax.fill_between(world_trends['Year'], 
                        world_trends[min_col], 
                    world_trends['GDP per capita, PPP (constant 2021 international $)_max'],
                    alpha=0.2, color='lightblue', label='Min-Max Range')
    
    # Crisis periods
    ax.axvspan(2008, 2009, alpha=0.3, color='red', label='2008 Financial Crisis')
    ax.axvspan(2020, 2022, alpha=0.3, color='orange', label='COVID-19 Pandemic')
    
    ax.set_title('🌍 World GDP Per Capita Trend (1990-2023)', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('GDP Per Capita (USD)', fontsize=12)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Add annotations
    ax.annotate('📈 Steady Growth Period', xy=(2005, 12000), xytext=(2000, 15000),
                arrowprops=dict(arrowstyle='->', color='green'), fontsize=10)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()
    
    # Key insights
    print("🔍 Key Insights:")
    print(f"📊 Average growth: {((world_trends.iloc[-1]['GDP per capita, PPP (constant 2021 international $)_mean'] / world_trends.iloc[0]['GDP per capita, PPP (constant 2021 international $)_mean'] - 1) * 100):.1f}% over the period")
    print(f"💰 2023 World Average: ${world_trends.iloc[-1]['GDP per capita, PPP (constant 2021 international $)_mean']:,.0f}")

def plot_continent_comparison(continent_trends, save_path=None):
    """
    Plot continent-wise GDP comparison
    """
    # Interactive Plotly version
    fig = px.line(continent_trends, x='Year', y='avg_gdp', color='Continent',
                  title='🌍 GDP Per Capita by Continent (1990-2023)',
                  labels={'avg_gdp': 'Average GDP Per Capita (USD)', 'Year': 'Year'},
                  width=900, height=600)
    
    # Add crisis periods
    fig.add_vrect(x0=2008, x1=2009, fillcolor="red", opacity=0.2, 
                  annotation_text="2008 Crisis", annotation_position="top left")
    fig.add_vrect(x0=2020, x1=2022, fillcolor="orange", opacity=0.2,
                  annotation_text="COVID-19", annotation_position="top right")
    
    fig.update_layout(
        title_font_size=16,
        xaxis_title_font_size=12,
        yaxis_title_font_size=12,
        legend_title_font_size=12
    )
    
    if save_path:
        fig.write_html(save_path.replace('.png', '.html'))
    
    fig.show()
    
    # Static version for GitHub
    plt.figure(figsize=(12, 8))
    
    for continent in continent_trends['Continent'].unique():
        data = continent_trends[continent_trends['Continent'] == continent]
        plt.plot(data['Year'], data['avg_gdp'], marker='o', linewidth=2, 
                label=continent, markersize=3)
    
    plt.axvspan(2008, 2009, alpha=0.3, color='red', label='2008 Crisis')
    plt.axvspan(2020, 2022, alpha=0.3, color='orange', label='COVID-19')
    
    plt.title('🌍 GDP Per Capita by Continent', fontsize=16, fontweight='bold')
    plt.xlabel('Year')
    plt.ylabel('Average GDP Per Capita (USD)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()

def plot_top_bottom_countries(df, gdp_column, year=2023, save_path=None):
    """
    Plot top and bottom countries comparison
    """
    year_data = df[df['Year'] == year]
    if len(year_data) == 0:
        year = df['Year'].max()
        year_data = df[df['Year'] == year]
        print(f"⚠️ Using {year} data instead")
    
    # Get top and bottom 10
    top_10 = year_data.nlargest(10, gdp_column)
    bottom_10 = year_data.nsmallest(10, gdp_column)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Top 10
    bars1 = ax1.barh(range(len(top_10)), top_10[gdp_column], 
                     color=plt.cm.Greens(np.linspace(0.4, 0.8, len(top_10))))
    ax1.set_yticks(range(len(top_10)))
    ax1.set_yticklabels(top_10['Entity'])
    ax1.set_title(f'🏆 Top 10 Richest Countries ({year})', fontsize=14, fontweight='bold')
    ax1.set_xlabel('GDP Per Capita (USD)')
    
    # Add value labels
    for i, (idx, row) in enumerate(top_10.iterrows()):
        ax1.text(row[gdp_column] + 1000, i, f'${row[gdp_column]:,.0f}', 
                va='center', fontsize=9)
    
    # Bottom 10
    bars2 = ax2.barh(range(len(bottom_10)), bottom_10[gdp_column], 
                     color=plt.cm.Reds(np.linspace(0.4, 0.8, len(bottom_10))))
    ax2.set_yticks(range(len(bottom_10)))
    ax2.set_yticklabels(bottom_10['Entity'])
    ax2.set_title(f'📉 Bottom 10 Poorest Countries ({year})', fontsize=14, fontweight='bold')
    ax2.set_xlabel('GDP Per Capita (USD)')
    
    # Add value labels
    for i, (idx, row) in enumerate(bottom_10.iterrows()):
        ax2.text(row[gdp_column] + 50, i, f'${row[gdp_column]:,.0f}', 
                va='center', fontsize=9)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()
    
    # Print insights
    ratio = top_10.iloc[0][gdp_column] / bottom_10.iloc[0][gdp_column]
    print(f"💰 Wealth Gap: The richest country has {ratio:.1f}x more GDP per capita than the poorest")

def plot_world_map_choropleth(df, gdp_column, year=2023, save_path=None):
    """
    Create interactive world map showing GDP per capita
    """
    year_data = df[df['Year'] == year]
    if len(year_data) == 0:
        year = df['Year'].max()
        year_data = df[df['Year'] == year]
    
    # Create choropleth map
    fig = px.choropleth(
        year_data,
        locations='Code',
        color=gdp_column,
        hover_name='Entity',
        hover_data={gdp_column: ':,.0f'},
        color_continuous_scale='Viridis',
        title=f'🗺️ Global GDP Per Capita Distribution ({year})',
        labels={gdp_column: 'GDP Per Capita (USD)'}
    )
    
    fig.update_layout(
        title_font_size=16,
        geo=dict(showframe=False, showcoastlines=True, projection_type='equirectangular'),
        width=1000,
        height=600
    )
    
    if save_path:
        fig.write_html(save_path.replace('.png', '.html'))
    
    fig.show()

def plot_crisis_impact(crisis_analysis, save_path=None):
    """
    Plot impact of economic crises
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # 2008 Crisis Impact
    crisis_2008 = crisis_analysis['2008_crisis']
    
    # Top 10 most affected (negative impact)
    most_affected_2008 = crisis_2008.nsmallest(10, 'impact_2008')
    axes[0, 0].barh(range(len(most_affected_2008)), most_affected_2008['impact_2008'], 
                    color='red', alpha=0.7)
    axes[0, 0].set_yticks(range(len(most_affected_2008)))
    axes[0, 0].set_yticklabels(most_affected_2008.index)
    axes[0, 0].set_title('📉 Most Affected by 2008 Crisis', fontweight='bold')
    axes[0, 0].set_xlabel('GDP Change (%)')
    
    # Top 10 least affected or gained (positive impact)
    least_affected_2008 = crisis_2008.nlargest(10, 'impact_2008')
    axes[0, 1].barh(range(len(least_affected_2008)), least_affected_2008['impact_2008'], 
                    color='green', alpha=0.7)
    axes[0, 1].set_yticks(range(len(least_affected_2008)))
    axes[0, 1].set_yticklabels(least_affected_2008.index)
    axes[0, 1].set_title('📈 Least Affected by 2008 Crisis', fontweight='bold')
    axes[0, 1].set_xlabel('GDP Change (%)')
    
    # COVID Crisis Impact
    crisis_covid = crisis_analysis['covid_crisis']
    
    # Most affected by COVID
    most_affected_covid = crisis_covid.nsmallest(10, 'impact_covid')
    axes[1, 0].barh(range(len(most_affected_covid)), most_affected_covid['impact_covid'], 
                    color='orange', alpha=0.7)
    axes[1, 0].set_yticks(range(len(most_affected_covid)))
    axes[1, 0].set_yticklabels(most_affected_covid.index)
    axes[1, 0].set_title('🦠 Most Affected by COVID-19', fontweight='bold')
    axes[1, 0].set_xlabel('GDP Change (%)')
    
    # Least affected by COVID
    least_affected_covid = crisis_covid.nlargest(10, 'impact_covid')
    axes[1, 1].barh(range(len(least_affected_covid)), least_affected_covid['impact_covid'], 
                    color='blue', alpha=0.7)
    axes[1, 1].set_yticks(range(len(least_affected_covid)))
    axes[1, 1].set_yticklabels(least_affected_covid.index)
    axes[1, 1].set_title('💪 Resilient to COVID-19', fontweight='bold')
    axes[1, 1].set_xlabel('GDP Change (%)')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()

def plot_inequality_trends(inequality_data, save_path=None):
    """
    Plot wealth inequality trends over time
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    
    # Rich-Poor Ratio
    axes[0, 0].plot(inequality_data['Year'], inequality_data['ratio'], 
                    linewidth=3, marker='o', color='red')
    axes[0, 0].set_title('💰 Wealth Gap: Rich/Poor Ratio', fontweight='bold')
    axes[0, 0].set_ylabel('Ratio (Richest/Poorest)')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Gini Coefficient Approximation
    axes[0, 1].plot(inequality_data['Year'], inequality_data['gini_approx'], 
                    linewidth=3, marker='s', color='purple')
    axes[0, 1].set_title('📊 Inequality Index (Gini Approx)', fontweight='bold')
    axes[0, 1].set_ylabel('Gini Coefficient')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Standard Deviation
    axes[1, 0].plot(inequality_data['Year'], inequality_data['std_dev'], 
                    linewidth=3, marker='^', color='orange')
    axes[1, 0].set_title('📈 GDP Dispersion (Std Dev)', fontweight='bold')
    axes[1, 0].set_ylabel('Standard Deviation')
    axes[1, 0].set_xlabel('Year')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Max vs Min GDP
    axes[1, 1].plot(inequality_data['Year'], inequality_data['max_gdp'], 
                    linewidth=2, label='Richest Country', color='green')
    axes[1, 1].plot(inequality_data['Year'], inequality_data['min_gdp'], 
                    linewidth=2, label='Poorest Country', color='red')
    axes[1, 1].set_title('🏆 Extreme Values Over Time', fontweight='bold')
    axes[1, 1].set_ylabel('GDP Per Capita (USD)')
    axes[1, 1].set_xlabel('Year')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()

def create_animated_gdp_plot(df, gdp_column, save_path=None):
    """
    Create animated plot showing GDP evolution over time
    """
    # Select top 15 countries by latest GDP
    latest_year = df['Year'].max()
    top_countries = df[df['Year'] == latest_year].nlargest(15, gdp_column)['Entity'].tolist()
    
    df_top = df[df['Entity'].isin(top_countries)]
    
    fig = px.line(df_top, x='Year', y=gdp_column, color='Entity',
                  title='🎬 GDP Per Capita Evolution: Top 15 Countries',
                  labels={gdp_column: 'GDP Per Capita (USD)', 'Year': 'Year'},
                  width=1000, height=600,
                  animation_frame='Year' if len(df['Year'].unique()) <= 20 else None)
    
    fig.update_layout(title_font_size=16)
    
    if save_path:
        fig.write_html(save_path.replace('.png', '_animated.html'))
    
    fig.show()
    
    return fig