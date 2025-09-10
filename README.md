Analytics Dashboard — Pet Project
An interactive analytics dashboard built with Streamlit.  
The project demonstrates practical expertise in data analytics, statistics, A/B testing, and predictive modeling.  
It is designed as a portfolio-ready pet project to highlight professional skills in data analysis and dashboard development.

Live Demo
[Open the Dashboard](https://petanalytics.streamlit.app/)

Objectives
- Showcase the ability to build end-to-end data products: from data preparation to deployment.
- Apply statistical analysis for business-like decision-making (A/B testing, effect sizes).
- Demonstrate predictive modeling with regression, evaluation metrics, and visual diagnostics.
- Deliver a clean, consistent, and professionally designed user experience.

Features
 1. Overview
- KPI metrics (record count, averages).
- Distribution plots with kernel density and annotated sample size.
- Group comparisons (bar charts, boxplots) with professional labeling.
2. A/B Testing
- Statistical tests: Welch’s t-test and Mann–Whitney U.
- Effect size calculation (Cohen’s d).
- Density plots and boxplots for clear group comparison.
3. Predictive Modeling
- Linear Regression with preprocessing (OneHotEncoder + ColumnTransformer).
- Model evaluation using R², MAE, RMSE.
- Predicted vs Actual visualization for model diagnostics.

The analysis is based on a public dataset inspired by the **Student Performance Dataset** (often used in data science tutorials).  
- Source: [Kaggle — Student Performance Data Set](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)  
- Description:  
  - Each row represents a student.  
  - Features include demographic attributes (gender, parental education, lunch, test preparation) and exam scores in math, reading, and writing.  
  - Target variables such as **mean_score** and **total_score** are derived for analytics and modeling.  

This dataset is well-suited for demonstrating statistical comparisons, KPI dashboards, and regression modeling.

Installation
```bash
git clone https://github.com/myshkivska/pet_analytics.git
cd pet_analytics
pip install -r requirements.txt
streamlit run app.py

Tech Stack
Python — data analysis & modeling
Streamlit — interactive dashboards & deployment
pandas / seaborn / matplotlib — data manipulation & visualization
scikit-learn — preprocessing, regression, evaluation
scipy — statistical testing
