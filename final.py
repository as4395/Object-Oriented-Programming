# The purpose of this project is to analyze the relationship between Attendance and Exam Scores.

# Extract: Load dataset (Link: https://www.kaggle.com/datasets/lainguyn123/student-performance-factors)
import pandas as pd
data = pd.read_csv("StudentPerformanceFactors.csv")  
print(data.columns)

# Transformation: Change information so that there are averages for Exam Scores are grouped by Attendance levels
attendance_total_count = {}  # Keys: Attendance Levels, Values: Count of Rows (Students), Total Exam Score
for index, each_row in data.iterrows():
    if each_row["Attendance"] >= 0:
        attendance = each_row["Attendance"]
        if attendance not in attendance_total_count:
            attendance_total_count[attendance] = [1, each_row["Exam_Score"]]
        else:
            count_rows = attendance_total_count[attendance][0]
            total_score = attendance_total_count[attendance][1]
            attendance_total_count[attendance] = [count_rows + 1, total_score + each_row["Exam_Score"]]

for key, value in attendance_total_count.items():
    attendance_total_count[key] = attendance_total_count[key][1] / attendance_total_count[key][0]

attendance_total_count = dict(sorted(attendance_total_count.items()))

# Loading: Create a bar chart showing the relationship between Attendance and Exam Scores
import matplotlib.pyplot as plt
plt.bar(attendance_total_count.keys(), attendance_total_count.values(), color="palegreen")
plt.title("Average Exam Score by Attendance Level")
plt.xlabel("Attendance Level")
plt.ylabel("Average Exam Score")
plt.savefig("Attendance_vs_ExamScore.jpg")
print("The project was saved as a jpg")