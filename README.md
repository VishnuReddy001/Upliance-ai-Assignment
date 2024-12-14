# Upliance.ai.Assignment
# Assignment Report: Customer Orders and Sessions Analysis

## Overview
This project involves analyzing a dataset of customer orders and session activities to generate key insights and KPIs. The analysis includes cleaning the data, performing descriptive analysis, and creating visualizations in python and also in Power BI. The aim is to provide actionable insights into customer behavior, meal preferences, and business performance.

---

## Table of Contents
1. [Objective](#objective)  
2. [Datasets Used](#datasets-used)  
3. [Data Preparation](#data-preparation)  
4. [Analysis](#analysis)  
5. [Key Insights and KPIs](#key-insights-and-kpis)  
6. [Visualizations](#visualizations)  
7. [Conclusion](#conclusion)  
8. [Contact Information](#Contact-information)

---

## Objective
The goal of this assignment is to:
- Analyze customer order and session data.
- Identify trends in customer behavior, meal preferences, and ratings.
- Generate KPIs to improve business decision-making.
- Visualize the insights effectively using python and Power BI.

---

## Datasets Used
### 1. **Customer Dataset**
- Contains customer details like age, location, registration date, favorite meals, and total orders.

### 2. **Session Dataset**
- Tracks user sessions, including session start/end times, meal types, dish names, and session ratings.

### 3. **Orders Dataset**
- Contains transaction details like order ID, amount, order status, and customer ratings.

---

## Data Preparation
### 1. **Data Cleaning**
- Checked for missing values and duplicates:
  - `Rating` column had missing values, handled by filling with the average rating.
- Removed irrelevant or inconsistent data.
- Standardized column names for consistency.

### 2. **Data Merging**
- Merged the three datasets using `User ID` and `Session ID` as keys for a comprehensive analysis.

### 3. **New Columns Created**
- **Age Group:** Categorized customers into age groups (`18-30`, `30-40`, etc.).
- **Session Duration:** Calculated the session duration in minutes.
- **Time of Day:** Categorized sessions into `Morning`, `Afternoon`, `Evening`, or `Night`.

---

## Analysis
### Descriptive Statistics
- **Age Distribution:** Most customers fall in the `18-30` age group.
- **Location Trends:** Top cities include New York, Los Angeles, and Chicago.
- **Meal Preferences:** Dinner is the most popular meal type.
- **Customer Ratings:** Average session rating is 4.25 out of 5.

### Trends Observed
1. **Session Duration vs Rating:** Longer sessions tend to have higher ratings.
2. **Order Amount Distribution:** Most orders are between $7 and $15.
3. **Top Dishes Ordered:** Certain dishes drive more sessions and orders.
4. **High-Performing Cities:** New York and Los Angeles contribute significantly to revenue.

---

## Key Insights and KPIs
### Key Insights
1. **Age Group Contribution:** Customers aged 18-30 generate the highest number of sessions and orders.
2. **Meal Popularity:** Dinner has the highest engagement, followed by lunch.
3. **Top Cities by Revenue:** New York leads in both orders and session engagement.
4. **Customer Loyalty:** Users with higher session durations are more likely to place orders.

### KPIs
- **Average Session Rating:** 4.25
- **Average Order Value:** $11.05
- **Top Age Group:** 18-30 years
- **Most Popular Meal Type:** Dinner
- **Top City:** New York
- **Average Session Duration:** 45 minutes

---

## Visualizations
### Visuals Created in python as well as Power BI
1. **Age Group vs Total Orders:** Bar chart to show contribution by age groups.
2. **Meal Preferences:** Pie chart showing the percentage of breakfast, lunch, and dinner.
3. **Session Duration vs Rating:** Scatter plot highlighting the relationship.
4. **Top Cities by Revenue:** Map visualization.
5. **Order Amount Distribution:** Histogram showing the range of order values.
6. **Trends Over Time:** Line chart showing order trends by date.

---

## Instructions to Run Analysis
1. **Data Cleaning and Merging:** Run the Python script `ai_assignment.py`.
2. **Data Visualization:** Open Power BI and import the processed dataset.
3. **Export the Report:** Save the Power BI report and share with stakeholders.

---

## How to Access the Power BI Dashboard
1. Open Power BI and import the `.pbix` file.
2. Navigate through the interactive tabs to explore insights.

---

## Conclusion
- Customers aged 18-30 and in cities like New York drive the majority of revenue.
- Dinner is the most engaging meal type, providing an opportunity to introduce new dinner menu items.
- Longer sessions correlate with higher ratings, suggesting the importance of engagement.

---

## Contact Information
For any queries or collaboration:
- **Name**: Vishnu Reddy
- **Email**: msvvr9866@gmail.com
- **GitHub Repository**: https://github.com/VishnuReddy001/Upliance.ai.Assignment
- **LinkedIn**: https://www.linkedin.com/in/vishnu-reddy-maruri/
- **Phone No**: 9550445483
