files = open("day2/input.txt")

lines = files.readlines()
lines = [line.strip().split(" ") for line in lines]
tf = list()
idx_l = list()
print(len(lines))
for index, lists in enumerate(lines):
    tmp = list()
    for i in range(1, len(lists)):
        tmp.append(int(lists[i]) - int(lists[i-1]))
    if not all(map(lambda x: x>0, tmp)) and not all(map(lambda x: x<0, tmp)):
        idx_l.append(index)

# print(idx_l)

for idx in reversed(idx_l):
    # print(lines[idx])
    lines.remove(lines[idx])
# lines.remove(idx_l)
print(len(idx_l))
print("lines",len(lines))

for indexi, step in enumerate(lines):
    length = len(lines[indexi]) - 1
    tmpf = True

    for indexj, num in enumerate(step):
        if not tmpf:
            continue
        if indexj == 0:
            continue
        else:
            num1 = int(lines[indexi][indexj-1]) - int(num)

            if (num1 <= 3 and num1 > 0) or (num1 >= -3 and num1 < 0):
                lines[indexi][indexj-1] = int(lines[indexi][indexj-1]) - int(num)
                print(lines[indexi])
                if indexj == length:
                    lines[indexi].pop(-1)
                    tf.append(True)
                
            else:
                tf.append(False)
                tmpf = False

print(len(lines))                                                                                                                                                                         
print(len(idx_l))
print(len(tf))               
print(tf.count(True))