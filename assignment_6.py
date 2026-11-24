# Exercise 3: Employee Payroll

employees = [("Ali", 20.0, 45), ("Sara", 25.0, 38), ("Omar", 18.5, 50)]

# 1
empl_num = int(input("Enter an employee number from 0 to 2: "))

# 2
name = employees[empl_num][0]
rate = employees[empl_num][1]
hours = employees[empl_num][2]

# 3
if hours <= 40:
    weekly_pay = rate * hours

elif hours > 40:
    extra_hours = hours - 40
    base_pay = rate * 40
    overtime_pay = extra_hours * rate * 1.5
    weekly_pay = base_pay + overtime_pay

# 4
print(name, weekly_pay)

# 5
new_name = input("Enter a new employee's name: ")
new_rate = float(input("Enter the employee's rate: "))
new_hours = int(input("Enter the employee's hours: "))

employees.append((new_name, new_rate, new_hours))

# 6
print("Number of employees: " + str(len(employees)))


# employees[empl_num][1] = 15.0
# This line was used to test if Ali's rate can be changed in the tuple
# The output was: TypeError: 'tuple' object does not support item assignment
# The reason behind this is because tuples are immutable meaning once they are initialized they cannot be changed.
# In order to change the rate you would need to replace the whole tuple value:
#       employees[empl_num] = ("Ali", 15.0, 45)
#       print(employees)
# print line above was used to test if tuple was changed; it was
