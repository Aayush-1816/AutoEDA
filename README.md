# 📊 AutoEDA – Automated Exploratory Data Analysis Toolkit

A Python-based command-line tool that performs **automated exploratory data analysis (EDA)** and basic visualization on structured datasets.

While built as a general data analysis tool, this project can also support **security analytics workflows** such as log exploration, anomaly detection preparation, and pattern discovery.

---

## 🚀 Features

- 📂 Load any CSV dataset
- 🛠 Automatic missing value handling  
  - Numerical → filled with median  
  - Categorical → filled with "Unknown"
- 📊 Summary statistics and column type analysis
- 🔍 Null value inspection
- 📈 Automatic visualisations:
  - Categorical distribution plots
  - Numerical histograms with KDE
  - Correlation heatmap for numeric features

---

## 🛡️ Security Analytics Use Cases

This toolkit can be applied in cybersecurity for:

- Log dataset exploration before detection modeling  
- Identifying unusual patterns in authentication logs  
- Preparing structured datasets for anomaly detection  
- Visualising correlations in security event data  

---

## 🛠 Technologies Used

- Python  
- Pandas  
- Matplotlib  
- Seaborn  

---

## ⚙️ Installation

```bash
git clone https://github.com/Aayush-1816/AutoEDA.git
cd AutoEDA
pip install -r requirements.txt
