# student-performance-analysis 

## Project Overview

This project analyzes a fake student performance dataset using Python, pandas, and Matplotlib. The goal is to practice working with CSV data, creating calculated columns, summarizing data, and visualizing trends.

The analysis looks at student grades, study hours, attendance rates, course averages, pass/fail status, and students who may be at risk of failing.

## Skills Used

- Python
- pandas
- Matplotlib
- CSV files
- Data analysis
- Data cleaning
- Grouping and sorting data
- Calculated columns
- Data visualization

## Dataset

The dataset includes fake student information with the following columns:

- 'student_id'
- 'student_name'
- 'course'
- 'study_hours'
- 'attendance_rate'
- 'assignment_score'
- 'exam_score'

The Python script calculates:

- 'final_grade'
- 'passed'

## Files

student-performance-analysis/
├── README.md
├── requirements.txt
├── data/
    └── student_data.csv
├── src/
    └── analysis.py
├── average_grade_by_course.png
└── study_hours_vs_final_grade.png

# HOW TO RUN THE PROJECT:
1) Clone or Download the repository(click green "Code" button to download)
2) Open project in a new terminal or Codespace(if using Git)
3) Install required libraries --> pip install -r requirements.txt
4) run the analysis --> python src/analysis.py
5) view results

# Questions Answered

This project answers questions such as:

- What is the average final grade by course?
- How many students passed of fail?
- Which students are at risk of failing?
- What is the average number of study hours by course?
- Is there a relationship between study hours and final grade?

# Visualizations

The project creates two charts:

1) Average Final Grade by Course
2) Study Hours vs Final Grade

These charts help show grade trends across courses and compare students study time with final performance.

# Project Summary

In this project I used Python and pandas to analyze student data. I created calculated columns, grouped data by course, filtered students based on grade performance, and used Matplotlib to create visualizations. This project shows data analysis skills that are useful for data science and coding-related roles.