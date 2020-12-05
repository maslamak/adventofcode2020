fname = r"input_4.txt"
f = open(fname)
columns = 8
data0 = f.read()
data1 = data0.split('\n\n')
rows = len(data1)
data2 = [[0 for x in range(columns)] for y in range(rows)]
key_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

for line_no, line in enumerate(data1):
    for key_list_col, key in enumerate(key_list):
        key_start = line.find(key)
        if key_start >= 0:
            space_pos = line[key_start:].find(' ')
            new_line_pos = line[key_start:].find('\n')
            if space_pos == -1 and new_line_pos == -1:
                delimiter_pos = len(line)
            elif space_pos >= 0 and new_line_pos >= 0:
                delimiter_pos = min(space_pos, new_line_pos) + key_start
            elif space_pos >= 0:
                delimiter_pos = space_pos + key_start
            elif new_line_pos >= 0:
                delimiter_pos = new_line_pos + key_start
            data2[line_no][key_list_col] = line[key_start + 4:delimiter_pos]
valid_count = 0
for i in range(len(data2)):
    all_true = True
    for j in range(columns - 1):
        if data2[i][j] == 0:
            all_true = False
            break
    if all_true:
        valid_count += 1
print(valid_count)
