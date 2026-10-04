# NYC Public School SAT Test Results Analysis

## Overview
Every year, high school students across New York City take the SAT—a standardized exam evaluating college readiness in Reading, Writing, and Mathematics. This project uses Python and pandas to perform an exploratory data analysis (EDA) on test performance data from NYC public high schools.

## Project Objectives
* **Identify Top Math Performers:** Filter high schools achieving an average math score of >= 640 (out of 800).
* **Rank Overall Performance:** Determine the top 10 schools in NYC based on combined SAT performance (`math + reading + writing`).
* **Analyze Regional Variance:** Identify which NYC borough exhibits the largest standard deviation in overall SAT scores to measure educational performance dispersion.

## Repository Structure
```text
nyc-sat-data-science/
├── data/
│   └── schools.csv
├── notebooks/
│   └── nyc_school_analysis.ipynb
├── .gitignore
├── README.md
├── main.py
└── requirements.txt
