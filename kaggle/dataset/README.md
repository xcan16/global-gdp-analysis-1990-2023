# Global GDP Per Capita Analysis Dataset (1990-2023)

## 📋 Dataset Description

This dataset contains comprehensive GDP per capita data from the World Bank covering the period 1990-2023. The data includes both raw and cleaned versions for immediate analysis.

## 📊 Data Source

- **Source**: World Bank Open Data
- **Indicator**: GDP per capita, PPP (constant 2017 international $)
- **Time Period**: 1990-2023
- **Coverage**: Global (All countries and regions)
- **Update Frequency**: Annual

## 📁 Files Included

### 1. `gdp-per-capita-worldbank.csv`
- **Description**: Raw GDP per capita data as downloaded from World Bank
- **Rows**: ~7,000+ observations
- **Columns**: 4 (Entity, Code, Year, GDP per capita)
- **Data Quality**: Contains missing values for some country-year combinations

### 2. `gdp_cleaned.csv`
- **Description**: Cleaned version with missing values removed
- **Rows**: ~6,000+ observations
- **Columns**: 4 (Entity, Code, Year, GDP per capita)
- **Data Quality**: No missing values, ready for analysis

## 📈 Key Statistics

- **Countries/Regions**: 200+ entities
- **Time Span**: 34 years (1990-2023)
- **GDP Range**: $400 - $200,000+ (wide economic spectrum)
- **Data Completeness**: ~85% after cleaning

## 🔍 Column Descriptions

| Column | Type | Description |
|--------|------|-------------|
| `Entity` | String | Country or region name |
| `Code` | String | ISO 3-letter country code |
| `Year` | Integer | Year of observation (1990-2023) |
| `GDP per capita, PPP (constant 2017 international $)` | Float | GDP per capita in constant 2017 international dollars, adjusted for purchasing power parity |

## 💡 Use Cases

This dataset is perfect for:

- **Economic Development Analysis**: Track country progress over time
- **Comparative Economics**: Compare GDP levels across countries
- **Time Series Analysis**: Analyze economic trends and patterns
- **Crisis Impact Studies**: Study effects of 2008 financial crisis, COVID-19
- **Regional Economic Studies**: Compare economic performance by region
- **Income Inequality Research**: Analyze global wealth distribution
- **Data Science Practice**: Excellent for data cleaning, visualization, and statistical analysis

## 🛠️ Data Processing Notes

- **Missing Data**: Some countries have incomplete data for certain years
- **Currency**: All values in constant 2017 international dollars (PPP adjusted)
- **Methodology**: World Bank methodology for GDP calculations
- **Comparability**: PPP adjustment makes cross-country comparisons meaningful

## 📊 Sample Analysis Ideas

1. **Economic Growth Trends**: Analyze which countries had fastest GDP growth
2. **Crisis Impact**: Study how 2008 financial crisis and COVID-19 affected different economies
3. **Development Convergence**: Examine if poorer countries are catching up to richer ones
4. **Regional Comparisons**: Compare economic performance across continents
5. **Outlier Analysis**: Identify countries with exceptional economic performance

## 🤝 Acknowledgments

- **World Bank**: For providing open access to high-quality economic data
- **Our World in Data**: For data aggregation and accessibility

## 📄 License

This dataset is released under **CC0 1.0 Universal (Public Domain)**. You are free to use, modify, and distribute this data for any purpose.

## 🔗 Related Resources

- [World Bank Open Data](https://data.worldbank.org/)
- [Our World in Data - Economic Growth](https://ourworldindata.org/economic-growth)
- [Analysis Notebook](link-to-your-kaggle-notebook) (Coming soon!)

---

**Happy Analyzing! 📈**