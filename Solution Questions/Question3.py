
import csv

dept_salary = {}
max_salary = 0
top_employee = ""

with open("employees.csv", "r") as f:
    data = csv.DictReader(f)

    for employee in data:
        emp_name = employee["name"]
        dept = employee["department"]
        pay = int(employee["salary"])

        if dept not in dept_salary:
            dept_salary[dept] = []

        dept_salary[dept].append(pay)

        if pay > max_salary:
            max_salary = pay
            top_employee = emp_name

print("Average Salary of Each Department:")

for dept in dept_salary:
    total = sum(dept_salary[dept])
    count = len(dept_salary[dept])
    print(dept, ":", total / count)

print("Highest Paid Employee:")
print("Name:", top_employee)
print("Salary:", max_salary)
