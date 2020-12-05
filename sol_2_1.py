import pandas as pd

fname = "input_2.txt"

data = pd.read_csv(fname, sep="-|:| |  ", header=None, engine='python')

counter = data[0].count()
valid_count = 0
print(counter)

for i in range(0, counter):
    valid_min = data[0][i]
    valid_max = data[1][i]
    valid_letter = data[2][i]
    pwd = data[4][i]
    current_count = pwd.count(valid_letter)
    if valid_min <= current_count <= valid_max:
        valid_count = valid_count + 1

print(valid_count)
