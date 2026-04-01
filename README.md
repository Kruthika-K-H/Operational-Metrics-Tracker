# 📊 Operational Metrics Tracker

## 🚀 Project Overview

This project automates weekly operational performance tracking using Python. It simulates real-world business operations where teams are monitored based on task completion, efficiency, and delays.

The system generates insights, visualizations, and an automated PDF report to support decision-making in operations management.

---

## 🎯 Objectives

* Automate weekly operations review
* Identify underperforming teams
* Generate KPI-based insights
* Provide visual dashboards for trend analysis
* Create automated reports for stakeholders

---

## 📂 Dataset Description

The dataset contains simulated operational data across multiple teams over 24 weeks.

### Columns:

* **Week** – Time period of operations
* **Team** – Team name
* **Tasks_Assigned** – Number of tasks assigned
* **Tasks_Completed** – Number of tasks completed
* **Resolution_Time_hrs** – Time taken to complete tasks

---

## ⚙️ Key Features

### ✅ KPI Calculation

* Completion Rate (%)
* Efficiency (Tasks per hour)
* Delay (Pending tasks)

### 🚨 Alert System

* **Critical**: Completion Rate < 75%
* **Warning**: 75% – 85%
* **Performance Risk**: High resolution time
* **On Track**: Optimal performance

### 📈 Visualizations

* Line Chart → Weekly performance trend
* Heatmap → Team-wise performance comparison

### 📄 Automated Reporting

* Generates PDF report with:

  * KPI summary
  * Team performance
  * Charts

---

## 🧠 Business Insights

* Team Gamma consistently underperformed, indicating possible workload imbalance or inefficiency
* Performance dip observed during Weeks 10–12, simulating operational disruption
* High-performing teams like Alpha maintained stability across all weeks
* Resolution time impacts overall efficiency significantly

---

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* FPDF

---

## ▶️ How to Run

### Step 1: Install dependencies

pip install pandas matplotlib seaborn fpdf openpyxl

### Step 2: Generate dataset

python generate_data.py

### Step 3: Run analysis

python metrics_tracker.py

---

## 📁 Output

* performance_trend.png
* heatmap.png
* Weekly_Report.pdf

---

## 💡 Future Enhancements

* Real-time dashboard using Power BI
* Email alert system for critical teams
* Integration with live operational databases

---

## 📌 Conclusion

This project demonstrates how automation, data analysis, and visualization can improve operational decision-making and performance tracking in real-world scenarios.

---
