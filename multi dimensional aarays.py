def dif():
    a = int(raw_input("enter the number of column"))
    b = int(raw_input("enter the number of row"))
    lol = [[[] for _ in range(a)] for _ in range(b)]
    return (a, b, lol)


def fill(a, b, lol):
    for x in range(b):
        print ("now enter the elements in  row %d" % x)
        for y in range(a):
            print ("now enter the elements in  row %d" % x)
            p = int(raw_input("enter the element in column  %d of row %d" % (y, x)))
            lol[x][y] = p
            y += 1
        x += 1
    print(lol)


q, j, lol = dif()
fill(q, j, lol)
