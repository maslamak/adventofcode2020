import csv

fname = r"input_3.txt"
with open(fname) as f:
    array = [list(line.strip()) for line in f]

right_rep_times = 2
outfile = r"output_3_extra.csv"

sol_list = []
for fake_right in range(0, right_rep_times * len(array[0])):
    right = fake_right // len(array[0])
    for down in range(1, len(array)):
        col = 0
        treecount = 0
        for row in range(0, len(array), down):
            if array[row][col] == "#":
                treecount += 1
            col += right
            if col >= len(array[0]):
                col = col - len(array[0])
        sol_list.append([fake_right, down, treecount])

with open(outfile, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(sol_list)
