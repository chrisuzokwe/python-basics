
studentgrades = {}

while True:

    f = open('cnu25_grades.txt', 'a')

    select = input("Select an option:\n "
      " [1] Add Student Grade\n "
      " [2] Remove Student Grade\n "
      " [3] Modify Student Grade\n "
      " [4] Display All Student Grades\n"
      "\n"
      "Enter Selection:\n")

    if select == 1:
        name = raw_input("--Add Student--\n  Enter Name:")
        grade = raw_input("  Enter Grade:\n")

        studentgrades[name] = grade

        f.write('Student Successfully Added!\n')

    elif select == 2:
        name = raw_input("--Remove Student--\n  Enter Name:\n")

        del studentgrades[name]

        f.write('Successfully Removed ' + str(name) + '!\n')

    elif select == 3:
        name = raw_input("--Modify Student Grade--\n  Enter Name:")
        grade = raw_input("  Enter Grade:\n")

        studentgrades[name] = grade

        f.write('Successfully Updated ' + str(name) + '!\n')

    elif select == 4:
        for key, value in studentgrades.items():
            f.write('--Displaying All Students--\n''%s: %s\n' % (key, value))
