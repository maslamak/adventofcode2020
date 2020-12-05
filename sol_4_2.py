import string
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
    flag = False
    all_true = True
    for j in range(columns - 1):
        if data2[i][j] == 0:
            all_true = False
            flag = True
            print(i, ' inv\n')
            break
    if flag == False:
        byr = int(data2[i][0])
        iyr = int(data2[i][1])
        eyr = int(data2[i][2])
        hgt = str(data2[i][3])
        if hgt[-2:] == 'in':
            hgt_in = int(hgt[0:-2])
            hgt_cm = -1
        elif hgt[-2:] == 'cm':
            hgt_cm = int(hgt[0:-2])
            hgt_in = -1
        else:
            hgt_cm = -1
            hgt_in = -1
        hcl = data2[i][4]
        ecl = data2[i][5]
        pid = str(data2[i][6])
        cid = data2[i][7]
        if not (1920 <= byr <= 2002):
            all_true = False
            print(i, ' byr ', byr, '\n')
        if not (2010 <= iyr <= 2020):
            all_true = False
            print(i, ' iyr ', iyr, '\n')
        if not (2020 <= eyr <= 2030):
            all_true = False
            print(i, ' eyr ', eyr, '\n')
        if not (59 <= hgt_in < 76 or 150 <= hgt_cm <= 193):
            all_true = False
            print(i, ' hgt ', hgt, '\n')
        if hcl[0] != '#' or len(hcl) != 7 or not (all(char in string.hexdigits for char in hcl[1:])):
            print(i, ' hcl ', hcl, '\n')
            all_true = False
        ecl_valid_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if not (ecl in ecl_valid_list):
            print(i, ' ecl ', ecl, '\n')
            all_true = False
        if len(pid) != 9:
            print(i, ' pid ', pid, '\n')
            all_true = False
    if all_true:
        valid_count += 1
        print(i, '   ')
print(valid_count)
