"""
Utility functions for GDP per capita analysis
Author: GitHub Portfolio Project
"""

import pandas as pd
import numpy as np

def get_continent_mapping():
    """
    Returns a dictionary mapping countries to continents
    """
    continent_mapping = {
        # Europe
        'Albania': 'Europe', 'Andorra': 'Europe', 'Austria': 'Europe', 'Belarus': 'Europe', 
        'Belgium': 'Europe', 'Bosnia and Herzegovina': 'Europe', 'Bulgaria': 'Europe', 
        'Croatia': 'Europe', 'Cyprus': 'Europe', 'Czech Republic': 'Europe', 'Czechia': 'Europe',
        'Denmark': 'Europe', 'Estonia': 'Europe', 'Finland': 'Europe', 'France': 'Europe', 
        'Germany': 'Europe', 'Greece': 'Europe', 'Hungary': 'Europe', 'Iceland': 'Europe', 
        'Ireland': 'Europe', 'Italy': 'Europe', 'Latvia': 'Europe', 'Lithuania': 'Europe', 
        'Luxembourg': 'Europe', 'Malta': 'Europe', 'Moldova': 'Europe', 'Monaco': 'Europe', 
        'Montenegro': 'Europe', 'Netherlands': 'Europe', 'North Macedonia': 'Europe', 
        'Norway': 'Europe', 'Poland': 'Europe', 'Portugal': 'Europe', 'Romania': 'Europe', 
        'Russia': 'Europe', 'San Marino': 'Europe', 'Serbia': 'Europe', 'Slovakia': 'Europe', 
        'Slovenia': 'Europe', 'Spain': 'Europe', 'Sweden': 'Europe', 'Switzerland': 'Europe', 
        'Ukraine': 'Europe', 'United Kingdom': 'Europe', 'Vatican': 'Europe',
        
        # Asia
        'Afghanistan': 'Asia', 'Armenia': 'Asia', 'Azerbaijan': 'Asia', 'Bahrain': 'Asia', 
        'Bangladesh': 'Asia', 'Bhutan': 'Asia', 'Brunei': 'Asia', 'Cambodia': 'Asia', 
        'China': 'Asia', 'Georgia': 'Asia', 'India': 'Asia', 'Indonesia': 'Asia', 
        'Iran': 'Asia', 'Iraq': 'Asia', 'Israel': 'Asia', 'Japan': 'Asia', 
        'Jordan': 'Asia', 'Kazakhstan': 'Asia', 'Kuwait': 'Asia', 'Kyrgyzstan': 'Asia', 
        'Laos': 'Asia', 'Lebanon': 'Asia', 'Malaysia': 'Asia', 'Maldives': 'Asia', 
        'Mongolia': 'Asia', 'Myanmar': 'Asia', 'Nepal': 'Asia', 'North Korea': 'Asia', 
        'Oman': 'Asia', 'Pakistan': 'Asia', 'Palestine': 'Asia', 'Philippines': 'Asia', 
        'Qatar': 'Asia', 'Saudi Arabia': 'Asia', 'Singapore': 'Asia', 'South Korea': 'Asia', 
        'Sri Lanka': 'Asia', 'Syria': 'Asia', 'Taiwan': 'Asia', 'Tajikistan': 'Asia', 
        'Thailand': 'Asia', 'Timor': 'Asia', 'Turkey': 'Asia', 'Turkmenistan': 'Asia', 
        'United Arab Emirates': 'Asia', 'Uzbekistan': 'Asia', 'Vietnam': 'Asia', 'Yemen': 'Asia',
        
        # Africa
        'Algeria': 'Africa', 'Angola': 'Africa', 'Benin': 'Africa', 'Botswana': 'Africa', 
        'Burkina Faso': 'Africa', 'Burundi': 'Africa', 'Cameroon': 'Africa', 'Cape Verde': 'Africa', 
        'Central African Republic': 'Africa', 'Chad': 'Africa', 'Comoros': 'Africa', 
        'Congo': 'Africa', 'Democratic Republic of Congo': 'Africa', 'Djibouti': 'Africa', 
        'Egypt': 'Africa', 'Equatorial Guinea': 'Africa', 'Eritrea': 'Africa', 'Eswatini': 'Africa', 
        'Ethiopia': 'Africa', 'Gabon': 'Africa', 'Gambia': 'Africa', 'Ghana': 'Africa', 
        'Guinea': 'Africa', 'Guinea-Bissau': 'Africa', 'Ivory Coast': 'Africa', 'Kenya': 'Africa', 
        'Lesotho': 'Africa', 'Liberia': 'Africa', 'Libya': 'Africa', 'Madagascar': 'Africa', 
        'Malawi': 'Africa', 'Mali': 'Africa', 'Mauritania': 'Africa', 'Mauritius': 'Africa', 
        'Morocco': 'Africa', 'Mozambique': 'Africa', 'Namibia': 'Africa', 'Niger': 'Africa', 
        'Nigeria': 'Africa', 'Rwanda': 'Africa', 'Sao Tome and Principe': 'Africa', 
        'Senegal': 'Africa', 'Seychelles': 'Africa', 'Sierra Leone': 'Africa', 'Somalia': 'Africa', 
        'South Africa': 'Africa', 'South Sudan': 'Africa', 'Sudan': 'Africa', 'Tanzania': 'Africa', 
        'Togo': 'Africa', 'Tunisia': 'Africa', 'Uganda': 'Africa', 'Zambia': 'Africa', 'Zimbabwe': 'Africa',
        
        # North America
        'Canada': 'North America', 'United States': 'North America', 'Mexico': 'North America',
        'Antigua and Barbuda': 'North America', 'Bahamas': 'North America', 'Barbados': 'North America',
        'Belize': 'North America', 'Costa Rica': 'North America', 'Cuba': 'North America',
        'Dominica': 'North America', 'Dominican Republic': 'North America', 'El Salvador': 'North America',
        'Grenada': 'North America', 'Guatemala': 'North America', 'Haiti': 'North America',
        'Honduras': 'North America', 'Jamaica': 'North America', 'Nicaragua': 'North America',
        'Panama': 'North America', 'Saint Kitts and Nevis': 'North America', 'Saint Lucia': 'North America',
        'Saint Vincent and the Grenadines': 'North America', 'Trinidad and Tobago': 'North America',
        
        # South America
        'Argentina': 'South America', 'Bolivia': 'South America', 'Brazil': 'South America', 
        'Chile': 'South America', 'Colombia': 'South America', 'Ecuador': 'South America', 
        'Guyana': 'South America', 'Paraguay': 'South America', 'Peru': 'South America', 
        'Suriname': 'South America', 'Uruguay': 'South America', 'Venezuela': 'South America',
        
        # Oceania
        'Australia': 'Oceania', 'Fiji': 'Oceania', 'Kiribati': 'Oceania', 'Marshall Islands': 'Oceania',
        'Micronesia': 'Oceania', 'Nauru': 'Oceania', 'New Zealand': 'Oceania', 'Palau': 'Oceania',
        'Papua New Guinea': 'Oceania', 'Samoa': 'Oceania', 'Solomon Islands': 'Oceania',
        'Tonga': 'Oceania', 'Tuvalu': 'Oceania', 'Vanuatu': 'Oceania'
    }
    
    return continent_mapping

def add_continent_column(df):
    """
    Add continent column to dataframe based on Entity column
    """
    continent_mapping = get_continent_mapping()
    df_copy = df.copy()
    df_copy['Continent'] = df_copy['Entity'].map(continent_mapping)
    
    # Handle unmapped countries
    unmapped = df_copy[df_copy['Continent'].isnull()]['Entity'].unique()
    if len(unmapped) > 0:
        print(f"⚠️ Kıta mapping'i olmayan ülkeler: {list(unmapped)}")
        # Default to 'Other' for unmapped countries
        df_copy['Continent'] = df_copy['Continent'].fillna('Other')
    
    return df_copy

def get_crisis_years():
    """
    Returns dictionary of major economic crisis years
    """
    return {
        '2008_crisis': [2008, 2009],
        'covid_crisis': [2020, 2021, 2022]
    }

def calculate_growth_rate(df, gdp_column, entity_column='Entity'):
    """
    Calculate year-over-year growth rate for each entity
    """
    df_copy = df.copy()
    df_copy = df_copy.sort_values([entity_column, 'Year'])
    df_copy['growth_rate'] = df_copy.groupby(entity_column)[gdp_column].pct_change() * 100
    return df_copy

def get_moving_average(df, gdp_column, window=5, entity_column='Entity'):
    """
    Calculate moving average for GDP per capita
    """
    df_copy = df.copy()
    df_copy = df_copy.sort_values([entity_column, 'Year'])
    df_copy[f'{window}y_moving_avg'] = df_copy.groupby(entity_column)[gdp_column].rolling(window=window, min_periods=1).mean().reset_index(0, drop=True)
    return df_copy

def filter_complete_data(df, min_years=10):
    """
    Filter entities that have data for at least min_years
    """
    entity_counts = df['Entity'].value_counts()
    valid_entities = entity_counts[entity_counts >= min_years].index
    return df[df['Entity'].isin(valid_entities)]

def get_top_bottom_countries(df, gdp_column, year=2023, n=10):
    """
    Get top and bottom n countries for a specific year
    """
    year_data = df[df['Year'] == year].copy()
    if len(year_data) == 0:
        # Try latest available year
        latest_year = df['Year'].max()
        year_data = df[df['Year'] == latest_year].copy()
        print(f"⚠️ {year} verisi bulunamadı, {latest_year} kullanılıyor")
    
    top_countries = year_data.nlargest(n, gdp_column)
    bottom_countries = year_data.nsmallest(n, gdp_column)
    
    return top_countries, bottom_countries