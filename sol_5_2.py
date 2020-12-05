import pandas as pd

f = open(r"input_5.txt")
outfile = r"output_5.csv"

seats = f.read().splitlines()

rows = list(range(0, 128))
cols = list(range(0, 8))
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
    seat_row.append(row[0])
    seat_col.append(col[0])

visible_boardingpasses = list(zip(seat_row, seat_col, seat_id))

pd_visible_boardingpasses = pd.DataFrame(visible_boardingpasses, columns=['row', 'col', 'id'])

all_rows = []
all_cols = []
all_id = []
for i in range(128):
    for j in range(8):
        all_rows.append(i)
        all_cols.append(j)
        all_id.append(i * 8 + j)

all_combinations = list(zip(all_rows, all_cols, all_id))
pd_all_combination = pd.DataFrame(all_combinations, columns=['row', 'col', 'id'])

merged_pd = pd.merge(pd_visible_boardingpasses, pd_all_combination, how='outer', indicator=True)
merged_pd.to_csv(outfile)
