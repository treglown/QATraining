import statistics
import math
data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"
def grades():
    for x in grades:
        print(x)

grades = data.split(',')

median_grades = statistics.median(grades)
mean_grades = statistics.mean(grades)
total_grades = sum(grades)
average_grades = float(total_grades // len(grades))
grades = list(map(int, grades))
grades = sorted(grades)
min_grades = min(grades)
max_grades = max(grades)

grade_summary = "The minimum grade is {}, the maximum grade is {}, the median grade is{}, the average grade is {}, the total grade is {}."

print(grade_summary.format(min_grades, max_grades, median_grades, average_grades, average_grades, total_grades ))


