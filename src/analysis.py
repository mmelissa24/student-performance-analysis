import pandas as pd 
import matplotlib.pyplot as plt  

# load the student data
df = pd.read_csv('data/student_data.csv')

# calculate final grade
df['final_grade'] = (df['assignment_score'] * 0.4) + (df['exam_score'] * 0.6)

# create pass/fail column
df['passed'] = df['final_grade'] >= 70

# show the full dataset with new columns
print('Student Data with Final Grades:')
print(df)

print("\nAverage Final Grade by Course:")
course_averages = df.groupby("course")["final_grade"].mean().sort_values(ascending=False)
print(course_averages)

print("\nPass/Fail Counts:")
pass_counts = df["passed"].value_counts()
print(pass_counts)

print("\nStudents At Risk of Failing:")
at_risk_students = df[df["final_grade"] < 70]
print(at_risk_students[["student_name", "course", "final_grade"]])

print("\nAverage Study Hours by Course:")
study_hours_by_course = df.groupby("course")["study_hours"].mean().sort_values(ascending=False)
print(study_hours_by_course)

# Chart 1: Average final grade by course
course_averages.plot(kind="bar")
plt.title("Average Final Grade by Course")
plt.xlabel("Course")
plt.ylabel("Average Final Grade")
plt.tight_layout()
plt.savefig("average_grade_by_course.png")
plt.show()
plt.clf()

# Chart 2: Study hours vs final grade
plt.scatter(df["study_hours"], df["final_grade"])
plt.title("Study Hours vs Final Grade")
plt.xlabel("Study Hours")
plt.ylabel("Final Grade")
plt.tight_layout()
plt.savefig("study_hours_vs_final_grade.png")
plt.show()


