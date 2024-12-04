import re

file = open("input.txt", "r")
file = file.readlines()

matches = list()

# Task 1

for line in file:
    matches.append(re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", line))

# flatten list bc not up for that shit
matches = [x[i] for x in matches for i in range(len(x))]
# only nums
matches = [x.removeprefix("mul(") for x in matches]
matches = [x.removesuffix(")") for x in matches]
matches = [x.split(",") for x in matches]

su = sum([int(x[0]) * int(x[1]) for x in matches])
print(su)

# Task 2

matches = list()

for line in file:
    matches.append(re.findall("do\(\)|don't\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)", line))

# flatten list bc not up for that shit
matches = [x[i] for x in matches for i in range(len(x))]
right_choice = list()
do = True
for idx, item in enumerate(matches):
    if do:
        if not item == "do()" and not item == "don't()":
            right_choice.append(item)
    if item == "do()":
        do = True
    if item == "don't()":
        do = False

# only nums
right_choice = [x.removeprefix("mul(") for x in right_choice]
right_choice = [x.removesuffix(")") for x in right_choice]
right_choice = [x.split(",") for x in right_choice]

su = sum([int(x[0]) * int(x[1]) for x in right_choice])

print(su)