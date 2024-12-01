
files = open('day1/input.txt', 'r')

lines = files.readlines()
lines = [line.strip().split("   ") for line in lines]

# Task 1 (idk I could have done this with functional thingish but I'm lazy)
left = [int(line[0]) for line in lines]
right = [int(line[1]) for line in lines]

l = left.copy() # need for Task 2
r = right.copy() # need for Task 2

dis = list()
for i in range(len(left)):
    dis.append(min(left) - min(right) if min(left) > min(right) else min(right) - min(left))
    left.remove(min(left))
    right.remove(min(right))


print(sum(dis))

#Task 2
sim = [elem * r.count(elem) for elem in l]
print(sum(sim))