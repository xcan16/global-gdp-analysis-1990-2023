"""
Data processing functions for GDP per capita analysis
Author: GitHub Portfolio Project
"""

import pandas as pd
import numpy as np
from .utils import get_continent_mapping

def load_and_clean_data(file_path='../data/gdp-per-capita-worldbank.csv'):
    """
    Load and clean the GDP per capita dataset
    """
    # Load data
    df = pd.read_csv(file_path)
    
    # Get GDP column name
    gdp_column = [col for col in df.columns if col not in ['Entity', 'Code', 'Year']][0]
    
    print(f"📊 Original dataset size: {df.shape}")
    print(f"💰 GDP column: {gdp_column}")
    
    # Remove missing GDP values
    df_clean = df.dropna(subset=[gdp_column]).copy()
    
    # Remove negative GDP values if any
    df_clean = df_clean[df_clean[gdp_column] >= 0]
    
    # Add continent information
    continent_mapping = get_continent_mapping()
    df_clean['Continent'] = df_clean['Entity'].map(continent_mapping)
    
    print(f"✅ Cleaned dataset size: {df_clean.shape}")
    print(f"🌍 Countries: {df_clean['Entity'].nunique()}")
    print(f"📅 Year range: {df_clean['Year'].min()} - {df_clean['Year'].max()}")
    
    return df_clean, gdp_column

def prepare_analysis_data(df, gdp_column):
    """
    Prepare data for analysis by adding calculated columns
    """
    df_analysis = df.copy()
    
    # Add year-over-year growth rate
    df_analysis = df_analysis.sort_values(['Entity', 'Year'])
    df_analysis['yoy_growth'] = df_analysis.groupby('Entity')[gdp_column].pct_change() * 100
    
    # Add 5-year moving average
    df_analysis['ma_5y'] = df_analysis.groupby('Entity')[gdp_column].rolling(window=5, min_periods=1).mean().reset_index(0, drop=True)
    
    # Add log transformation for better distribution
    df_analysis['log_gdp'] = np.log(df_analysis[gdp_column])
    
    return df_analysis

def calculate_growth_rate(df, gdp_column, entity_col='Entity', year_col='Year'):
    """
    Calculate year-over-year growth rate
    """
    df_sorted = df.sort_values([entity_col, year_col])
    df_sorted['growth_rate'] = df_sorted.groupby(entity_col)[gdp_column].pct_change() * 100
    return df_sorted

def get_moving_average(df, gdp_column, window=5, entity_col='Entity'):
    """
    Calculate moving average for GDP values
    """
    df_ma = df.copy()
    df_ma[f'ma_{window}y'] = df_ma.groupby(entity_col)[gdp_column].rolling(window=window, min_periods=1).mean().reset_index(0, drop=True)
    return df_ma
    df_analysis['log_gdp'] = np.log(df_analysis[gdp_column])
    
    # Add GDP categories
    df_analysis['gdp_category'] = pd.cut(
        df_analysis[gdp_column],
        bins=[0, 5000, 15000, 50000, float('inf')],
        labels=['Low Income', 'Lower Middle', 'Upper Middle', 'High Income']
    )
    
    return df_analysis

def get_world_trends(df, gdp_column):
    """
    Calculate world trends and statistics
    """
    world_trends = df.groupby('Year').agg({
        gdp_column: ['mean', 'median', 'std', 'min', 'max'],
        'Entity': 'count'
    }).round(2)
    
    world_trends.columns = ['_'.join(col).strip() for col in world_trends.columns.values]
    world_trends = world_trends.reset_index()
    
    return world_trends

def get_continent_trends(df, gdp_column):
    """
    Calculate continent-wise trends
    """
    continent_trends = df.groupby(['Year', 'Continent']).agg({
        gdp_column: 'mean',
        'Entity': 'count'
    }).round(2)
    
    continent_trends = continent_trends.reset_index()
    continent_trends = continent_trends.rename(columns={gdp_column: 'avg_gdp', 'Entity': 'country_count'})
    
    return continent_trends

def analyze_crisis_impact(df, gdp_column):
    """
    Analyze impact of economic crises
    """
    crisis_analysis = {}
    
    # 2008 Financial Crisis
    pre_2008 = df[df['Year'].isin([2006, 2007])].groupby('Entity')[gdp_column].mean()
    post_2008 = df[df['Year'].isin([2008, 2009])].groupby('Entity')[gdp_column].mean()
    
    crisis_2008 = pd.DataFrame({
        'pre_crisis': pre_2008,
        'during_crisis': post_2008
    }).dropna()
    
    crisis_2008['impact_2008'] = ((crisis_2008['during_crisis'] - crisis_2008['pre_crisis']) / crisis_2008['pre_crisis'] * 100)
    
    # COVID-19 Impact
    pre_covid = df[df['Year'].isin([2018, 2019])].groupby('Entity')[gdp_column].mean()
    during_covid = df[df['Year'].isin([2020, 2021])].groupby('Entity')[gdp_column].mean()
    
    crisis_covid = pd.DataFrame({
        'pre_crisis': pre_covid,
        'during_crisis': during_covid
    }).dropna()
    
    crisis_covid['impact_covid'] = ((crisis_covid['during_crisis'] - crisis_covid['pre_crisis']) / crisis_covid['pre_crisis'] * 100)
    
    crisis_analysis['2008_crisis'] = crisis_2008
    crisis_analysis['covid_crisis'] = crisis_covid
    
    return crisis_analysis

def get_inequality_trends(df, gdp_column):
    """
    Calculate inequality trends over time
    """
    inequality_data = []
    
    for year in df['Year'].unique():
        year_data = df[df['Year'] == year]
        if len(year_data) >= 10:  # Minimum countries for meaningful calculation
            
            # Calculate inequality metrics
            max_gdp = year_data[gdp_column].max()
            min_gdp = year_data[gdp_column].min()
            ratio = max_gdp / min_gdp if min_gdp > 0 else np.nan
            
            # Gini coefficient approximation
            sorted_gdp = year_data[gdp_column].sort_values()
            n = len(sorted_gdp)
            cum_sum = sorted_gdp.cumsum()
            gini = (2 * (np.arange(1, n+1) * sorted_gdp).sum() - (n + 1) * cum_sum.iloc[-1]) / (n * cum_sum.iloc[-1])
            
            inequality_data.append({
                'Year': year,
                'max_gdp': max_gdp,
                'min_gdp': min_gdp,
                'ratio': ratio,
                'gini_approx': gini,
                'std_dev': year_data[gdp_column].std()
            })
    
    return pd.DataFrame(inequality_data)

def get_growth_champions_and_laggards(df, gdp_column, min_years=15):
    """
    Identify fastest growing and declining countries
    """
    # Filter countries with sufficient data
    country_years = df.groupby('Entity')['Year'].count()
    sufficient_data = country_years[country_years >= min_years].index
    df_filtered = df[df['Entity'].isin(sufficient_data)]
    
    growth_analysis = []
    
    for country in df_filtered['Entity'].unique():
        country_data = df_filtered[df_filtered['Entity'] == country].sort_values('Year')
        
        if len(country_data) >= min_years:
            # Calculate compound annual growth rate (CAGR)
            first_year = country_data.iloc[0]
            last_year = country_data.iloc[-1]
            years = last_year['Year'] - first_year['Year']
            
            if first_year[gdp_column] > 0 and years > 0:
                cagr = (((last_year[gdp_column] / first_year[gdp_column]) ** (1/years)) - 1) * 100
                
                growth_analysis.append({
                    'Entity': country,
                    'start_year': first_year['Year'],
                    'end_year': last_year['Year'],
                    'start_gdp': first_year[gdp_column],
                    'end_gdp': last_year[gdp_column],
                    'total_growth': ((last_year[gdp_column] - first_year[gdp_column]) / first_year[gdp_column]) * 100,
                    'cagr': cagr,
                    'years': years
                })
    
    growth_df = pd.DataFrame(growth_analysis)
    
    # Get top performers
    top_growers = growth_df.nlargest(10, 'cagr')
    worst_performers = growth_df.nsmallest(10, 'cagr')
    
    return top_growers, worst_performers, growth_df