import random
import time
operators = ["+", "-", "*"]
min_operands = 3
max_operands = 12
total_problems = 10


def generate_problem():
    left = random.randint(min_operands, max_operands)
    right = random.randint(min_operands, max_operands)
    operator = random.choice(operators)
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer
expr, answer = generate_problem()

wrong = 0
input("Press Enter to start the math challenge...")
print("-----------------------------------")

start_time = time.time()

for i in range(total_problems):
    expr, answer = generate_problem()
    guess = input("Problem #" + str(i+1) + ": " + expr + " = ")
    while True:
        if guess == str(answer):
            print("Correct!")
            break
        else:
            print("Incorrect. Try again.")
            guess = input("Try again: ")
end_time = time.time()
totaltime = end_time - start_time
print("----------------------------------")
print("Math challenge complete!")
print("Total time taken: " + str(round(totaltime, 2)) + " seconds")
