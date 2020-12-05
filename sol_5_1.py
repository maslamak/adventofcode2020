f = open("input_5.txt")
seats = f.read().splitlines()

rows = list(range(0, 128))
cols = list(range(0, 8))
row = rows
col = cols
seat_id = []
seat_row = []
seat_col = []

for seat in seats:
    row = rows
    col = cols
    for char in seat:
        if char == 'F':
            row = row[0:int(len(row) / 2)]
        elif char == "B":
            row = row[int(len(row) / 2):]
        elif char == "L":
            col = col[0:int(len(col) / 2)]
        elif char == "R":
            col = col[int(len(col) / 2):]
    s_id = row[0] * 8 + col[0]
    seat_id.append(s_id)

print(max(seat_id))
