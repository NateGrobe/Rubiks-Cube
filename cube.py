import numpy
from PIL import Image

x = 2048
y = 1024

data = numpy.zeros((y, x, 3), dtype=numpy.uint8)

colors = {
    'w': [255,255,255],
    'r': [255,0,0],
    'y': [255,255,0],
    'o': [255,128,0],
    'b': [0,0,255],
    'g': [0,255,0],
    'b': [0,0,0]
}

cube = [
        # cube 0
        [
                ['w','w','w'],
                ['w','w','w'],
                ['w','w','w']
        ],
        # cube 1
        [
                ['r','r','r'],
                ['r','r','r'],
                ['r','r','r']
        ],
        # cube 2
        [
                ['y','y','y'],
                ['y','y','y'],
                ['y','y','y']
        ],
        # cube 3
        [
                ['o','o','o'],
                ['o','o','o'],
                ['o','o','o']
        ],
        # cube 4
        [
                ['b','b','b'],
                ['b','b','b'],
                ['b','b','b']
        ],
        # cube 5
        [
                ['g','g','g'],
                ['g','g','g'],
                ['g','g','g']
        ]
]

def render_empty_layout(d):
    hori_start = 57
    hori_end = 965
    vert_start = 418
    vert_end = 1627

    # Makes background white
    for ya in range(0, y):
        for xa in range(0, x):
            d[ya,xa] = colors['w']

    # Places horizontal lines
    for tpx in range(hori_start, hori_end, 302):
        if tpx == 57 or tpx == 963:
            for rpx in range(tpx, tpx+2):
                for px in range(vert_end-302, vert_end):
                    d[rpx,px] = colors['b']
        else:
            for rpx in range(tpx, tpx+2):
                for px in range(vert_start,vert_end):
                    d[rpx,px] = colors['b']


    # Places vertical lines
    for tpx in range(vert_start, vert_end, 302):
        if tpx >= 1324:
            for rpx in range(tpx, tpx+2):
                for px in range(hori_start, hori_end):
                    d[px, rpx] = colors['b']
        elif tpx == vert_start:
            for rpx in range(tpx, tpx+2):
                for px in range(hori_start + 302, hori_end - 302):
                    d[px, rpx] = colors['b']
        else:
            for rpx in range(tpx, tpx+2):
                for px in range(hori_start + 302, hori_end - 302):
                    d[px, rpx] = colors['b']



    image = Image.fromarray(data)

    image.show()

if __name__ == "__main__":
    render_empty_layout(data)
