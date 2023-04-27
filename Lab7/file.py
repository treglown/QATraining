file = open("teams.txt", "w")

sports_teams = ["Man United", "Man City", "Newcastle", "Baraca FC", "Liverpool"]

for i in sports_teams:
    newline = i + "\n"
    file.write(newline)

file.close()

file = open("teams.txt", "r")

lines = file.readlines()

print(lines[0].strip)
print(lines[3].strip)

file.close()


file = open("teams.txt", "r")

lines = file.readlines()

file.close()
lines[0] = "This is a new line"

file = open("teams.txt", "w")

for i in range(len(lines)):
    if i == len(lines)-1:
        file.write(lines[i])
    else: file.write(lines[i].strip() + "\n")

file.close()

file = open("teams.txt", "r")

for line in file:
    print(line.strip())

file.close()