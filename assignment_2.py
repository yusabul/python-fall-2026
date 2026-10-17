stdCode = 34551001
stdName = "Yusuf"
stdLastName = "Abulghaith"
stdMidterm = 80
stdFinal = 98.5
stdGPA = 3.7
stdActive = True
stdCourses = ["Python", "Math", "English"]
stdBirthDate = (2002, 1, 28)
stdProfile = {"name": "Yusuf", "city": "Woodbridge"}
stdSkills = {"typing", "Excel", "typing"}
stdAdvisor = None

#1
print(type(stdCode))
print(type(stdName))
print(type(stdFinal))

#2
print(type(stdActive))
print(type(stdAdvisor))

#3
print(type(stdCourses))
print(type(stdBirthDate))
print(type(stdProfile))
print(type(stdSkills))

#4
# PREDICTION: I predict that stdSkills will print 3 items, because there are three items in the dictionary.
# print(stdSkills) This line was used to test if my prediction was right or not
# My prediction was wrong because I didn't know that stdSkills was actually a set and that sets also used {}.

#5
x = 5j
print(type(x))

#6
r = range(5)
print(type(r))
print(list(r))

#7
stdMidterm = float(stdMidterm)
print(stdMidterm)
print(type(stdMidterm))

#8
# PREDICTION: I predict that print(int(stdFinal)) will show 98. It will not round up because int truncates the decimal point and any values after it.
# print(int(stdFinal)) This line was used to test my prediction was right, and it was!

#9
stdCode = str(stdCode)
print(len(stdCode))

#10
stdCourses = frozenset(stdCourses)
print(type(stdCourses))

#11
msg = b"Hello"
print(type(msg))

#12
# PREDICTION: I predict the following data types for each value:
#                   10 -> int
#                   10.0 -> float
#                   "10" -> str
#                   [10] -> list
#                   (10,) -> tuple
#                   {10} -> set
#                   {'a': 10} -> dict
#                   True -> bool
# print(type(10), type(10.0), type("10"), type([10]), type((10,)), type({10}), type({'a': 10}), type(True))
# The line abpve was used to test if my prediction was correct, and it was!

#13
# PREDICTION: I predict that the data type of stdMidterm + stdFinal will be a float, assuming that the change of stdMidterm into a float value from #7 is kept.
#             I think the data type of stdMidterm +stdFinal would still be a float even if stdMidterm's original type (int) were kept.
# print(type(stdMidterm + stdFinal))
# print(type(int(stdMidterm) + stdFinal))
# The lines above were used to test if my prediction was correct and it was!

#14
# PREDICTION: I predict that the data type of stdMidterm / 2 would be a float regardless of whether the change of stdMidterm's type in #7 was applied or not.
# print(type(stdMidterm/2))
# print(type(int(stdMidterm)/2))
# The lines above were used to test if my prediction was correct and it was!

#15
print(type((10,)))

# BONUS
# print(type((1))) shows <class 'int'> instead of class tuple because tuples use commas after each value within the ().
# For example, print(type((1,)) would give you <class 'tuple'> as the output
# However, it would also be considered a tuple if it were a case where there is more than one value within the () such as (1,20).
# The comma at the end for (1,) is neccessary because 1 is the only value.
