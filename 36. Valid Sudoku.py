s = [ [ j for j in range(9)] for i in range(9) ]

rows = []
cols = []
boxs = []

# get all the rows value 
for i in range(9):
    row = []
    for j in range(9):
        row.append(s[i][j])
        # print(s[i][j])
    rows.append(row)

#  get all the columns
col = 0
while(col<9):
    c = []
    row = 0
    while(row<9):
        # print( s[row][col])
        c.append( s[row][col])
        row += 1

    cols.append(c)
    
    col += 1

# print(s)
# print(cols)

for r in range(i,i+3,1):
    b = 3
    s = 
    while(b):

