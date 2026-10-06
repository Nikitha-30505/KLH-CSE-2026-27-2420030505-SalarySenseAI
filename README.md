# SalarySense AI: Employee Salary Prediction Using Regression Models

## Project Overview

SalarySense AI is a machine learning-based platform developed to predict employee salaries using regression techniques. The system analyzes employee-related factors such as age, gender, education level, job title, years of experience, industry, location, and company size to estimate salary values.

The project provides a Flask-based web application where users can enter employee details and obtain an estimated salary prediction.

## Team Members

1. Nikitha - 2420030505
2. Revanth - 2420030605

## Supervisor

Supervisor: Garimidi Siva Sree

## Abstract

Salary prediction is an important application of machine learning that can support organizations, employees, and job seekers in understanding compensation patterns. Employee salary depends on multiple factors such as educational qualification, professional experience, job role, industry, location, and company size.

SalarySense AI applies regression-based machine learning to analyze these factors and predict an estimated employee salary. The project includes dataset preparation, data preprocessing, feature transformation, model training, evaluation, and deployment through a Flask-based web application.

The developed system provides a simple and user-friendly platform for entering employee information and obtaining salary predictions. The project demonstrates how machine learning can support data-driven salary analysis and career-related decision making.

## Dataset

The project uses an employee salary dataset containing information related to:

- Age
- Gender
- Education Level
- Job Title
- Years of Experience
- Industry
- Location
- Company Size
- Salary

The dataset used in the project is:

`datasets/salary_data.csv`

The dataset is included in the repository for project execution and reproducibility.

## Objectives

- To analyze employee-related factors influencing salary.
- To preprocess and prepare salary data for machine learning.
- To develop a regression model for employee salary prediction.
- To evaluate the performance of the trained model.
- To provide salary predictions through a Flask-based web application.

## Methodology

The project follows these major steps:

1. Dataset Collection
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis
4. Feature Selection
5. Categorical Data Encoding
6. Regression Model Training
7. Model Evaluation
8. Salary Prediction
9. Flask Web Application Development
10. Testing and Result Analysis

## Machine Learning Model

The project uses **Linear Regression** for predicting continuous salary values.

The categorical features are transformed using Label Encoding before being provided to the regression model.

### Model Performance

The trained model achieved the following results:

- **MAE:** 6855.11
- **RMSE:** 8531.52
- **R² Score:** 0.9397

The trained model is saved as:

`Src/models/best_model.pkl`

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Flask
- HTML
- CSS
- JavaScript
- Matplotlib
- Git
- GitHub

## Web Application

The project includes a Flask-based web application that allows users to enter employee information and obtain an estimated salary prediction.

The application contains:

- Home Page
- Salary Prediction Page
- Prediction Result Page
- Dashboard
- About Page

## Project Structure

```text
KLH-CSE-2026-27-2420030505-SalarySenseAI/
│
├── datasets/
│   └── salary_data.csv
│
├── doc/
│   └── Final-Project.pptx
│
├── Results/
│   ├── about_page.png
│   ├── dashboard.png
│   ├── home_page.png
│   ├── prediction_input.png
│   └── prediction_result.png
│
├── Src/
│   ├── models/
│   │   └── best_model.pkl
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── js/
│   ├── templates/
│   │   ├── about.html
│   │   ├── dashboard.html
│   │   ├── index.html
│   │   ├── predict.html
│   │   ├── report.html
│   │   └── result.html
│   ├── app.py
│   ├── generate_dataset.py
│   ├── train_model.py
│   └── requirements.txt
│
├── .gitignore
└── README.md
