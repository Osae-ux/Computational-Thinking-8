# Beginning: create variables
right_points = 0
wrong_points = 0


# Middle: Ask questions
answer = input("Who is the best basketball player of all time A) lebron james, or B) michael jordan?")
if answer == "A":
    right_points += 1
elif answer == "B":
    wrong_points += 1


answer = input("What is the best ice cream flavor A) chocolate, or B) mint chocolate chip?")
if answer == "A":
    wrong_points += 1
elif answer == "B":
    right_points += 1


answer = input("What is the best mexican food chain A) taco del mar, or B) taco bell?")
if answer == "A":
    right_points += 1
elif answer == "B":
    wrong_points += 1


answer = input("What is the best NBA team A) Cleveland Cavaliers, or B) Los Angeles Lakers?")
if answer == "A":
    wrong_points += 1
elif answer == "B":
    right_points += 1


answer = input("Who is the GOAT A) Cristiano Ronaldo, or B) Lionel Messi?")
if answer == "A":
    wrong_points += 1
elif answer == "B":
    right_points += 1


# end of quiz:
if right_points > wrong_points:
    print("You are smart")
if wrong_points > right_points:
    print("You need to go back to school")