import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import os

# Load data
df = pd.read_excel("ops_data.xlsx")

# Create output folder
os.makedirs("output", exist_ok=True)

# KPIs
df['Completion_Rate'] = (df['Tasks_Completed'] / df['Tasks_Assigned']) * 100
df['Efficiency'] = df['Tasks_Completed'] / df['Resolution_Time_hrs']
df['Delay'] = df['Tasks_Assigned'] - df['Tasks_Completed']

# Status Logic
def get_status(row):
    if row['Completion_Rate'] < 75:
        return "Critical"
    elif row['Completion_Rate'] < 85:
        return "Warning"
    elif row['Resolution_Time_hrs'] > 6:
        return "Performance Risk"
    else:
        return "On Track"

df['Status'] = df.apply(get_status, axis=1)

# Avg performance
team_avg = df.groupby('Team')['Completion_Rate'].mean().sort_values()
print("\n📊 Average Performance by Team:")
print(team_avg)

# -------------------------------
# 📈 Line Chart
# -------------------------------
trend = df.groupby('Week')['Completion_Rate'].mean()

plt.figure()
trend.plot(marker='o')
plt.title("Weekly Performance Trend")
plt.xlabel("Week")
plt.ylabel("Completion Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/performance_trend.png")
plt.close()

# -------------------------------
# 🔥 Heatmap (FIXED)
# -------------------------------
pivot = df.pivot_table(
    index='Team',
    columns='Week',
    values='Completion_Rate',
    aggfunc='mean'
)

# Sort weeks properly
pivot = pivot.reindex(sorted(pivot.columns, key=lambda x: int(x.split()[1])), axis=1)

plt.figure()
sns.heatmap(pivot, annot=False)
plt.title("Team Performance Heatmap")
plt.tight_layout()
plt.savefig("output/heatmap.png")
plt.close()

# -------------------------------
# 📄 PDF Report
# -------------------------------
pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=12)

total_tasks = df['Tasks_Assigned'].sum()
avg_rate = df['Completion_Rate'].mean()

pdf.cell(200, 10, "Operational Metrics Report", ln=True)
pdf.cell(200, 10, f"Total Tasks: {total_tasks}", ln=True)
pdf.cell(200, 10, f"Avg Completion Rate: {avg_rate:.2f}%", ln=True)

pdf.ln(10)
pdf.cell(200, 10, "Team Performance:", ln=True)

for team, rate in team_avg.items():
    pdf.cell(200, 8, f"{team}: {rate:.2f}%", ln=True)

pdf.ln(10)

# Add images
pdf.image("output/performance_trend.png", w=180)
pdf.ln(5)
pdf.image("output/heatmap.png", w=180)

pdf.output("output/Weekly_Report.pdf")

print("\n✅ Report Generated: output/Weekly_Report.pdf")