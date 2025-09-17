# 📊 GDP Analysis Visualizations

This directory contains all the visualizations generated from the Global GDP Per Capita Analysis project. Each visualization corresponds to specific analysis sections and provides insights into global economic trends.

## 📁 Plot Categories

### 🔍 **Data Exploration Plots**
- `01_gdp_distribution.png` - Distribution of GDP Per Capita values
- `02_data_availability.png` - Data completeness by year
- `03_top_bottom_countries.png` - Top 10 and Bottom 10 countries comparison

### 📈 **EDA Analysis Plots**
- `04_world_gdp_trend.*` - World average GDP trend over time (Interactive)
- `05_continental_trends.*` - GDP trends by continent (Interactive)
- `06_crisis_impact.*` - Economic crisis impact analysis (Interactive)
- `07_wealth_distribution.png` - GDP distribution with statistical measures

### 🔧 **Feature Engineering Plots**
- `08_growth_distribution.png` - Year-over-year growth rate distribution
- `09_volatility_analysis.*` - Risk vs return analysis for major economies (Interactive)

### 📊 **Summary & Additional Plots**
- `10_summary_dashboard.png` - Comprehensive 4-panel summary dashboard
- `continent_2023.png` - Continental comparison for latest year
- `inequality_trends.png` - Wealth inequality trends analysis
- `world_gdp_trend.png` - Simplified world GDP trend

## 🎨 **File Formats**

- **PNG Files**: High-resolution static images (300 DPI) suitable for presentations and reports
- **HTML Files**: Interactive Plotly visualizations that can be opened in web browsers

## 📱 **Usage Recommendations**

### For Presentations:
- Use PNG files for PowerPoint or static documents
- Recommended: `10_summary_dashboard.png` for overview slides

### For Interactive Analysis:
- Open HTML files in web browsers for interactive exploration
- Recommended: `04_world_gdp_trend.html`, `05_continental_trends.html`

### For Portfolio:
- Include `10_summary_dashboard.png` as a project overview
- Use `06_crisis_impact.html` to demonstrate interactive capabilities

## 🔧 **Regenerating Plots**

To regenerate all visualizations, run:
```bash
python generate_plots.py
```

This will:
1. Load the GDP dataset
2. Process data with continent mappings
3. Generate all visualizations
4. Save files to this directory

## 📊 **Technical Details**

- **Resolution**: 300 DPI for PNG files
- **Dimensions**: Optimized for both screen and print
- **Color Scheme**: Professional color palette with accessibility considerations
- **Interactivity**: Plotly-based charts support zoom, pan, and hover features

---

*Generated on: September 2025*  
*Total Visualizations: 17 files*  
*Project: Global GDP Per Capita Analysis (1990-2023)*