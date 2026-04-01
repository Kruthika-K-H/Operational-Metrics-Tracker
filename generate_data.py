import pandas as pd
import random

weeks = [f"Week {i}" for i in range(1, 25)]
teams = ["Alpha", "Beta", "Gamma", "Delta", "Omega", "Sigma", "Zeta"]

data = []

for week in weeks:
    for team in teams:
        for _ in range(5):

            assigned = random.randint(40, 120)

            # Team-based performance
            if team == "Gamma":
                performance_factor = random.uniform(0.5, 0.75)
            elif team == "Alpha":
                performance_factor = random.uniform(0.85, 1.0)
            else:
                performance_factor = random.uniform(0.7, 0.9)

            # Performance dip
            if week in ["Week 10", "Week 11", "Week 12"]:
                performance_factor *= 0.8

            completed = int(assigned * performance_factor)
            resolution_time = round(random.uniform(2.5, 8.0), 1)

            data.append([week, team, assigned, completed, resolution_time])

df = pd.DataFrame(data, columns=[
    "Week", "Team", "Tasks_Assigned",
    "Tasks_Completed", "Resolution_Time_hrs"
])

df.to_excel("ops_data.xlsx", index=False)

print("✅ Dataset created:", len(df), "rows")