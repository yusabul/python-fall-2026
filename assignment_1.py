stdCode = 34551001
stdMidterm = 80
stdFinal = 98
stdName = "Yusuf"
stdLastName = "Abulghaith"

#1
print("Student Name: " + stdName + " " + stdLastName + " - Student Code: " + str(stdCode))

#2
print("Student Grade Final: " + str(stdFinal))

#3
print(stdName, stdLastName)

#4
print(str(stdFinal) + " " + stdLastName)

#5
print(stdFinal == stdMidterm)

#6
print(stdFinal != stdMidterm)

#7
print("Average (Midterm and Final) is: " + str((stdMidterm + stdFinal)/2))

#8
stdCode = 1
print("New Student Code:", stdCode)

#9
print((stdName != "Ayesha") or (stdFinal > stdMidterm) and (stdMidterm != stdFinal))

#10
stdCode = 34551001 # Updated to the original value
print("345" in str(stdCode)) # Would have been False because strCode = 1 from number 8

#11
print("345" not in str(stdCode))

#12
print (5 * 2 % 5)

#13
print("Final is: " + str(stdFinal))

#14
print("3" * 3)
