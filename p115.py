location = input()

col = location[1]
row = location[0]

avail = 8

if col == '1' or col == '8':
    avail //= 2

elif col == '2' or col == '7':
    avail -= 2

if row == 'a' or row == 'h':
    avail //= 2

elif row == 'b' or row == 'g':
    avail -= 2

print(avail)
