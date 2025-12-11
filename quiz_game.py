print("Welcome to my quiz game!")
score = 0
qnum = 0
playing = input("Do you want to play? (yes/no) ")
if playing == "yes":
    print("Great! Let's start the quiz.")
else:
    quit()
    
print("hello")

answer = input("What does CPU stand for? ")
qnum += 1
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Central Processing Unit.")
answer2 = input("What does GPU stand for? ")
qnum += 1
if answer2.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Graphics Processing Unit.")
answer3 = input("What does RAM stand for? ")
qnum += 1
if answer3.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Random Access Memory.")
answer4 = input("What does PSU stand for? ")
qnum += 1
if answer4.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Power Supply Unit.")   
print("Thanks for playing!")
print("You got " + str(score) + " questions correct out of " + str(qnum) + ".")
print("Your score is " + str((score/qnum)*100) + "%.")
