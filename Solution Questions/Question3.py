import csv

departments={}

with open ("employees.csv","r") as file:
    reader=csv.DictReader(file)


    for row in reader:
     name=row["name"]
     department=row["department"]
     salary=row["salary"]
     
     departments[department].append(salary)




