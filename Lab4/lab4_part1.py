ages = [12, 18, 33, 84, 45, 67, 12, 82, 95, 16, 10, 23, 43, 29, 40, 34, 30, 16, 44, 69, 70, 74, 38, 65, 36, 83, 50, 11, 7, 9, 64, 78, 37, 3, 8, 68, 22, 4, 60, 22, 4, 
        60, 33, 82, 45, 23, 5, 18, 28, 99, 17, 81, 14, 88, 50, 19, 59, 6, 44, 93, 35, 72, 25, 63, 11, 69, 11, 76, 10, 60, 30, 14, 21, 82, 47, 6, 21, 88, 46, 78, 92, 
        48, 36, 28, 51]

record_length_of_ages = len(ages)

updated_ages = []

plus_1_year = 1

for each_age in ages:
    updated_ages.append(each_age + plus_1_year)

for age in ages[0: ]:
    if age < 16 or age > 65:
        ages.remove(age)

updated_ages = sorted(ages)

young_adults = 0

for age in updated_ages:
    if age > 16 and age < 25:
        young_adults += 1
        print("Number of young adults is", young_adults)

for age in updated_ages:
    if age > 16 and age < 25:
        young_adults += 1

print(updated_ages)

word = input("Enter a word")
vowels = "aeiou"
count = 0

for letter in word: 
    if letter.lower() in vowels:
        count += 1
print(count)

# 


