fname = r"C:\Users\Mohammed Aslam\OneDrive\Desktop\code\input_6.txt"

f = open(fname)
data0 = f.read()
data1 = data0.split('\n\n')

total = 0
for line in data1:
    total_yes_within_group = 0
    no_ppl = (str(line).count('\n')) + 1
    response = (str(line).replace('\n', ''))
    no_unique_response = len(set(response))
    for char in set(response):
        if response.count(char) == no_ppl:
            total_yes_within_group += 1
    total += total_yes_within_group

print(total)
