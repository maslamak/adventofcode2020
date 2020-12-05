import pandas as pd

fname = "input_2.txt"
data = pd.read_csv(fname, sep="-|:| |  ", header=None, engine='python')

counter = data[0].count()
valid_count = 0
print(counter)

for i in range(0, counter):
    pos1 = data[0][i] - 1
    pos2 = data[1][i] - 1
    valid_letter = data[2][i]
    pwd = data[4][i]
    pos1_letter = pwd[pos1]
    pos2_letter = pwd[pos2]
    if (pos1_letter == valid_letter or pos2_letter == valid_letter) and not (
            pos1_letter == valid_letter and pos2_letter == valid_letter):
        valid_count = valid_count + 1

print(valid_count)
