import random
#ask how many question user
q_number = int(input("How many questions would you like? "))
#low and high numbers
#low_mun = int(input("What is the lowest number? "))
#high_mun = int(input("What is the highest number? "))
#make user to chose what he wants to solve
print("Chose what do to: ")
chose = int(input("1 - Add\n2 - Subtract\n3 - Multiply\n4 - Divide\n"))
#make user to solve what he chose
for q_number in range(1, q_number + 1):
    print(f"Question, {q_number}:")
#RNG
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
#Solve
#Addition
print(f"{num1} + {num2} =?")
ans_add = num1 + num2
userAns_add = int(input())
#subtraction
print(f"{num1} - {num2} =?")
ans_sub = num1 - num2
userAns_sub = int(input())
#multiplication
print(f"{num1} * {num2} =?")
ans_mul = num1 * num2
userAns_mul = int(input())
#division
print(f"{num1} / {num2} =?")
ans_div = num1 / num2
userAns_div = int(input())

if userAns_add == ans_add:  print("Correct!")
else:   print("Nope")
if userAns_sub == ans_sub:  print("Correct!")
else:   print("Nope")
if userAns_mul == ans_mul:  print("Correct!")
else:   print("Nope")
if userAns_div == ans_div:  print("Correct!")