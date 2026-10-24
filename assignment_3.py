import random
stdCode = 34551001
stdName = "Yusuf"
stdLastName = "Abulghaith"
stdMidterm = 80
stdFinal = 98.5
stdCity = " Woodbridge "
stdEmail = "yusuf.abulghaith@school.com"
stdPhone = "555-0142"
stdComment = ""

# PART A: NUMBERS
# 1
a = 12
b = 12.0
c = 12 + 3j

print(type(a))
print(type(b))
print(type(c))

# 2
# PREDICTION: The type of x = 35e3 is complex. print(x) will show 35e3.
# x = 35e3
# print(x)
# lines above were used to test my prediction
# My prediction was incorrect. x is actually a float; the output was 35000.0 which is 35 * 10^3, where e is "10 to the power of."

# 3
print(random.randrange(1, 11))


# PART B: CASTING
# 4
bonusPoints = "75"
stdMidterm += int(bonusPoints)
print(stdMidterm)

# 5
# PREDICTION: The following is what I predict will be printed by each line:
                # print(int(9.99)) -> 9
                # print(float(7)) -> 7.0
                # print(str(3.0)) -> "3.0"
# print(int(9.99))
# print(float(7))
# print(str(3.0))
# lines above were used to test my prediction; my predicton was correct.
# Note: I used quotation marks indicate that 3.0 was converted to a str, but print() removes them.

# 6
print("Student code: " + str(stdCode))

# 7
# PREDICTION: I predict that there will be a type error because print only accepts strings.
            # The type of error I predicted was incorrect, but I had known that it was an error.
# print(int("12.5")) line used to see print output
print(int(12.5)) # corrected line

# PART C: STRINGS
# 8
print(stdName[0])
print(stdLastName[-1])

# 9
print(stdName[0:3])

# 10
print(stdName.upper())
print(stdLastName.lower())

# 11
print(stdCity.strip())
print(len(stdCity))
print(len(stdCity.strip()))

# 12
print(stdPhone.replace("-", " "))

# 13
print(stdEmail.split("@"))
# PREDICTION: I predict that split() will return arr as the data type.
# print(type(stdEmail.split("@")))
# The line above was used to test my prediction. My prediction was close; I used the incorrect term. Rather than arr, the type would be list.

# 14
print(f"{stdName} {stdLastName} scored {stdFinal} on the final.")

# 15
stdMidterm = 80 # recovered original value due to change in #4
print(f"Average: {(stdMidterm + stdFinal)/2:.2f}")

# 16
print("The teacher said \"Great job!\" to Yusuf.")

# 17
print("school" in stdEmail)

# PART D: BOOLEANS
# 18
# PREDICTION: The following is True or False for each:
                # bool(0) -> True # incorrect; the correct output is False
                # bool(15) -> True
                # bool("") -> False
                # bool("False") -> True
                # bool([]) -> False
                # bool(None) -> False
print(bool(0))
print(bool(15))
print(bool(""))
print(bool("False"))
print(bool([]))
print(bool(None))

# 19
print(bool(stdComment))
# Line above outputs False because stdComment is an empty string. bool returns False when the value is empty, null, or 0.

# 20
print(isinstance(stdFinal, float))

# BONUS
print(stdName[::-1])



