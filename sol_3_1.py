fname = "input_3.txt"
with open(fname) as f:
    array = [list(line.strip()) for line in f]

right = 3
down = 1
col = 0
treecount = 0
for row in range(0, len(array), down):
    if array[row][col] == "#":
        treecount += 1
    col += right
    if col >= len(array[0]):
        col = col - len(array[0])

print(treecount)
