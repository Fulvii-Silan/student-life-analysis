

import pandas as pd
import random

students = []

for student_id in range(1, 51):  # 50 students
    for day in range(1, 31):     # 30 days
        hours = random.randint(0, 6)
        students.append({
            "student_id": student_id,
            "day": day,
            "study_hours": hours
        })

df = pd.DataFrame(students)
df.to_csv("data/raw/study_log.csv", index=False)

print("Dataset created!")
