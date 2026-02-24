employees = {
    101: [25000, 30000, 28000],
    102: [40000, 35000],
    103: [20000, 22000, 21000]
}

for dept in employees:
    print("Department:", dept)
    print("Minimum Salary:", min(employees[dept]))
    print("Maximum Salary:", max(employees[dept]))
    print()
