# Kaggle Upload Instructions

## 📋 Prerequisites

1. **Install Kaggle CLI**:
   ```bash
   pip install kaggle
   ```

2. **Setup Kaggle API**:
   - Go to Kaggle.com → Account → API → Create New API Token
   - Download `kaggle.json` and place it in:
     - Windows: `C:\\Users\\{username}\\.kaggle\\kaggle.json`
     - Mac/Linux: `~/.kaggle/kaggle.json`

## 📊 Dataset Upload

1. **Navigate to dataset directory**:
   ```bash
   cd "C:\\Users\\MONSTER\\Desktop\\Global_GDP_Per_Capita_(1990-2023)\\kaggle\\dataset"
   ```

2. **Create dataset**:
   ```bash
   kaggle datasets create -p . --dir-mode zip
   ```

   Or update existing dataset:
   ```bash
   kaggle datasets version -p . -m "Updated GDP data with improved analysis"
   ```

## 📓 Notebook Upload

1. **Navigate to notebook directory**:
   ```bash
   cd "C:\\Users\\MONSTER\\Desktop\\Global_GDP_Per_Capita_(1990-2023)\\kaggle\\notebook"
   ```

2. **Upload notebook**:
   ```bash
   kaggle kernels push -p .
   ```

## 🔧 Alternative: Manual Upload

### Dataset Upload:
1. Go to [Kaggle Datasets](https://www.kaggle.com/datasets)
2. Click "New Dataset"
3. Upload the files from `kaggle/dataset/` folder
4. Use the metadata from `dataset-metadata.json`

### Notebook Upload:
1. Go to [Kaggle Notebooks](https://www.kaggle.com/code)
2. Click "New Notebook"
3. Copy the content from `global-gdp-analysis-kaggle.ipynb`
4. Link to your uploaded dataset

## 📝 Important Notes

- **Dataset Title**: "Global GDP Per Capita Analysis (1990-2023)"
- **Dataset ID**: Should be `{username}/global-gdp-per-capita-1990-2023`
- **License**: CC0 1.0 Universal (Public Domain)
- **Tags**: economics, gdp, world bank, economic development, time series

## 🎯 Success Metrics

After upload, your dataset should have:
- ✅ Professional description and documentation
- ✅ Clean, well-structured data files
- ✅ Comprehensive analysis notebook
- ✅ Proper tags and categories
- ✅ Engaging visualizations

## 🚀 Promotion Tips

1. **Share on social media** with relevant hashtags
2. **Post in economics/data science communities**
3. **Create follow-up notebooks** with specific analyses
4. **Engage with comments** and feedback
5. **Cross-promote** with your other projects

---

**Good luck with your Kaggle uploads! 🌟**