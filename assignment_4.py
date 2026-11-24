# Exercise 1: Class Grade Book

scores = [88,92,75,64,95]

# 1
new_score = input("Enter a new score: ")
scores.append(int(new_score))

# 2
print("Number of scores: " + str(len(scores)))

# 3
print("Highest score: " + str(max(scores)))
print("Lowest score: " + str(min(scores)))

# 4
avg_score = sum(scores)/len(scores)
print("Average score: " + str(avg_score))

# 5
scores = sorted(scores)[::-1]
print("Top 3 scores: " + str(scores[0]) + ", " + str(scores[1]) + ", " + str(scores[2]))

# 6
if(avg_score >= 90):
    print("A class")

elif(avg_score >= 80):
    print("B class")

else:
    print("Keep working")

