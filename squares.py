x = 1

while x <= 100:
    square = x**2
    if square > 2000:
        break
    print(x, "=", square)
    x += 1

# Part 2 Factorial.py

num = int(input("Input a number"))

factorial = 1
while num > 1:
    factorial *= num
    num -= 1
print("Factorial: ", factorial)

# Part 3 investment

investment = float(input("How much have you invested: £ "))
goal = float(input("What is the goal to reach: £ "))
interest = float(input("What is the interest rate: "))
interest = interest / 100

time_in_years = 0

while investment < goal:
    investment *= (1 + interest)
    time_in_years += 1

print(f"It will take {time_in_years} to reach your goal of {goal}!")

# Part 4 getInt.py

min_value = 1
max_value = 100
tries = 0

while tries <3:
    value = int(input(f"Input any number between {min_value} and {max_value}"))
    if min_value <= max_value:
        print(f"incorrect input entered: {value}")
        break
    else:
        print("Incorrect input")

    tries += 1

if tries == 3:
    print("Too many tries entered!")

# Part 5 CountVowels.py

word = input("Enter a word: ")
vowel_count = 0
counter = 0

while counter < len(word):
    x = word[counter]
    if x.lower() in "aeiou":
        vowel_count += 1
    counter += 1

print(f"number of vowels in {word} is {vowel_count}")

# Part 6 ExamAverage

maths_mark = 999
english_mark = 999
ict_mark = 999

while (maths_mark < 0 or maths_mark >100):
    maths_mark = int(input("Enter maths mark(0-100): "))
while (english_mark < 0 or english_mark >100):
    english_mark = int(input("Enter english mark(0-100): "))
while (ict_mark < 0 or ict_mark >100):
    ict_mark = int(input("Enter ict mark(0-100): "))

average_mark = (maths_mark + english_mark + ict_mark) / 3

if average_mark >= 65:
    result = "pass"
else:
    result = "fail"

print(f"Average mark: {average_mark}: {result}")
