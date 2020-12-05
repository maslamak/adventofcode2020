fname = "input_3.txt"
with open(fname) as f:
    array = [list(line.strip()) for line in f]

right_list = [1, 3, 5, 7, 1]
down_list = [1, 1, 1, 1, 2]
product = 1
for i in range(len(right_list)):
    right = right_list[i]
    down = down_list[i]
    col = 0
    treecount = 0
    for row in range(0, len(array), down):
        if array[row][col] == "#":
            treecount += 1
        col += right
        if col >= len(array[0]):
            col = col - len(array[0])
    product *= treecount

print(product)
