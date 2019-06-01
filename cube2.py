cube = [
        ['w0','w1','w2','w3','w4','w5','w6','w7','w8'],
        ['g0','g1','g2','g3','g4','g5','g6','g7','g8'],
        ['r0','r1','r2','r3','r4','r5','r6','r7','r8'],
        ['b0','b1','b2','b3','b4','b5','b6','b7','b8'],
        ['o0','o1','o2','o3','o4','o5','o6','o7','o8'],
        ['y0','y1','y2','y3','y4','y5','y6','y7','y8']
        ]



# Clockwise cube turns (Right, Left, Up, Down, Front, Back)
def R():
    side1 = [cube[0][p] for p in range(2,9,3)]  # White
    side2 = [cube[2][p] for p in range(2,9,3)]  # Red
    side3 = [cube[4][p] for p in range(2,9,3)]  # Orange
    side4 = [cube[5][p] for p in range(2,9,3)]  # Yellow
    b1 = [cube[3][p] for p in range(0,3)]
    b2 = [cube[3][p] for p in range(3,6)]
    b3 = [cube[3][p] for p in range(6,9)]
    c = 0
    bc = 0

    for i in range(2,9,3):
        cube[0][i] = side2[c]
        cube[2][i] = side4[c]
        cube[4][i] = side1[c]
        cube[5][i] = side3[c]
        c += 1

    for i in range(0,9,3):
        cube[3][i] = b3[bc]
        cube[3][i+1] = b2[bc]
        cube[3][i+2] = b1[bc]
        bc += 1

def L():
    side1 = [cube[0][p] for p in range(0,9,3)]  # White
    side2 = [cube[2][p] for p in range(0,9,3)]  # Red
    side3 = [cube[4][p] for p in range(0,9,3)]  # Orange
    side4 = [cube[5][p] for p in range(0,9,3)]  # Yellow
    g1 = [cube[1][p] for p in range(0,3)]
    g2 = [cube[1][p] for p in range(3,6)]
    g3 = [cube[1][p] for p in range(6,9)]
    c = 0
    gc = 0

    for i in range(0,9,3):
        cube[0][i] = side3[c]
        cube[2][i] = side1[c]
        cube[4][i] = side4[c]
        cube[5][i] = side2[c]
        c += 1

    for i in range(0,9,3):
        cube[1][i] = g3[gc]
        cube[1][i+1] = g2[gc]
        cube[1][i+2] = g1[gc]
        gc += 1

def U():
    side1 = [cube[2][p] for p in range(0,3)]  # Red
    side2 = [cube[1][p] for p in range(0,3)]  # Green
    side3 = [cube[4][p] for p in range(0,3)]  # Orange
    side4 = [cube[3][p] for p in range(0,3)]  # Blue
    w1 = [cube[0][p] for p in range(0,3)]
    w2 = [cube[0][p] for p in range(3,6)]
    w3 = [cube[0][p] for p in range(6,9)]
    c = 0
    wc = 0

    for i in range(0,3):
        cube[2][i] = side4[c]
        cube[1][i] = side1[c]
        cube[4][i] = side2[c]
        cube[3][i] = side3[c]
        c += 1

    for i in range(0,9,3):
        cube[0][i] = w3[wc]
        cube[0][i+1] = w2[wc]
        cube[0][i+2] = w1[wc]
        wc += 1

def D():
    side1 = [cube[2][p] for p in range(6,9)]  # Red
    side2 = [cube[1][p] for p in range(6,9)]  # Green
    side3 = [cube[4][p] for p in range(6,9)]  # Orange
    side4 = [cube[3][p] for p in range(6,9)]  # Blue
    y1 = [cube[5][p] for p in range(0,3)]
    y2 = [cube[5][p] for p in range(3,6)]
    y3 = [cube[5][p] for p in range(6,9)]
    c = 0
    yc = 0

    for i in range(6,9):
        cube[2][i] = side2[c]
        cube[1][i] = side3[c]
        cube[4][i] = side4[c]
        cube[3][i] = side1[c]
        c += 1

    for i in range(0,9,3):
        cube[5][i] = y3[yc]
        cube[5][i+1] = y2[yc]
        cube[5][i+2] = y1[yc]
        yc += 1

def F():
    side1 = [cube[0][p] for p in range(6,9)]  # White
    side2 = [cube[1][p] for p in range(2,9,3)]  # Green
    side3 = [cube[5][p] for p in range(0,3)]  # Yellow
    side4 = [cube[3][p] for p in range(0,9,3)]  # Blue
    r1 = [cube[2][p] for p in range(0,3)]
    r2 = [cube[2][p] for p in range(3,6)]
    r3 = [cube[2][p] for p in range(6,9)]
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    rc = 0

    for i in range(6,9):
        cube[0][i] = side2[c1]
        c1 += 1

    for i in range(2,9,3):
        cube[1][i] = side3[c2]
        c2 += 1

    for i in range(0,9,3):
        cube[3][i] = side1[c3]
        c3 += 1

    for i in range(0,3):
        cube[5][i] = side4[c4]
        c4 += 1

    for i in range(0,9,3):
        cube[2][i] = r3[rc]
        cube[2][i+1] = r2[rc]
        cube[2][i+2] = r1[rc]
        rc += 1

def B():
    side1 = [cube[0][p] for p in range(0,3)]  # White
    side2 = [cube[1][p] for p in range(0,9,3)]  # Green
    side3 = [cube[5][p] for p in range(8,5,-1)]  # Yellow
    side4 = [cube[3][p] for p in range(2,9,3)]  # Blue
    o1 = [cube[4][p] for p in range(0,3)]
    o2 = [cube[4][p] for p in range(3,6)]
    o3 = [cube[4][p] for p in range(6,9)]
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    oc = 0

    for i in range(0,3):
        cube[0][i] = side4[c1]
        c1 += 1

    for i in range(0,9,3):
        cube[1][i] = side1[c2]
        c2 += 1

    for i in range(2,9,3):
        cube[3][i] = side3[c3]
        c3 += 1

    for i in range(0,3):
        cube[5][i] = side2[c4]
        c4 += 1

    for i in range(0,9,3):
        cube[4][i] = o3[oc]
        cube[4][i+1] = o2[oc]
        cube[4][i+2] = o1[oc]
        oc += 1

# Counter-clockwise turns (Right-inverted, Left-inverted, Up-inverted, Down-inverted, Front-inverted, Back-inverted)

def RI():
    side1 = [cube[0][p] for p in range(2,9,3)]  # White
    side2 = [cube[2][p] for p in range(2,9,3)]  # Red
    side3 = [cube[4][p] for p in range(2,9,3)]  # Orange
    side4 = [cube[5][p] for p in range(2,9,3)]  # Yellow
    b1 = [cube[3][p] for p in range(0,3)]
    b2 = [cube[3][p] for p in range(3,6)]
    b3 = [cube[3][p] for p in range(6,9)]
    print(b1)
    print(b2)
    print(b3)
    c = 0
    bc = 2

    for i in range(2,9,3):
        cube[0][i] = side3[c]
        cube[2][i] = side1[c]
        cube[4][i] = side4[c]
        cube[5][i] = side2[c]
        c += 1

    for i in range(0,9,3):
        print(i)
        cube[3][i] = b1[bc]
        cube[3][i+1] = b2[bc]
        cube[3][i+2] = b3[bc]
        bc -= 1

def L():
    side1 = [cube[0][p] for p in range(0,9,3)]  # White
    side2 = [cube[2][p] for p in range(0,9,3)]  # Red
    side3 = [cube[4][p] for p in range(0,9,3)]  # Orange
    side4 = [cube[5][p] for p in range(0,9,3)]  # Yellow
    g1 = [cube[1][p] for p in range(0,3)]
    g2 = [cube[1][p] for p in range(3,6)]
    g3 = [cube[1][p] for p in range(6,9)]
    c = 0
    gc = 0

    for i in range(0,9,3):
        cube[0][i] = side3[c]
        cube[2][i] = side1[c]
        cube[4][i] = side4[c]
        cube[5][i] = side2[c]
        c += 1

    for i in range(0,9,3):
        cube[1][i] = g3[gc]
        cube[1][i+1] = g2[gc]
        cube[1][i+2] = g1[gc]
        gc += 1


# def DI():
#     side1 = [cube[2][p] for p in range(6,9)]  # Red
#     side2 = [cube[1][p] for p in range(6,9)]  # Green
#     side3 = [cube[4][p] for p in range(6,9)]  # Orange
#     side4 = [cube[3][p] for p in range(6,9)]  # Blue
#     print(side4)
#     w1 = [cube[0][p] for p in range(0,3)]
#     w2 = [cube[0][p] for p in range(3,6)]
#     w3 = [cube[0][p] for p in range(6,9)]
#     c = 0
#     wc = 0

#     for i in range(6,9):
#         cube[2][i] = side4[c]
#         cube[1][i] = side1[c]
#         cube[4][i] = side2[c]
#         cube[3][i] = side3[c]
#         c += 1

#     for i in range(0,9,3):
#         cube[0][i] = w3[wc]
#         cube[0][i+1] = w2[wc]
#         cube[0][i+2] = w1[wc]
#         wc += 1

if __name__ == "__main__":
    RI()
    print(cube)
