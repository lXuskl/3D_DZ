from PIL import Image, ImageOps
import math
import matplotlib.pyplot as plt
def Bresenham(image, x0: int, y0: int, x1: int, y1: int, color: tuple = (255, 255, 255)):
    delta_x = abs(x1 - x0)
    delta_y = abs(y1 - y0)
    error = 0
    diff = 1

    # ����� ��������� � ������, ���� ��������� ���������� ������ �� ��� �, ��� ��������
    if(x0 - x1 > 0):
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    # �������� �� ��������
    if(y0 - y1 > 0):
        diff = -1

    # ���� ���� ������ ��� ����� 45, �� �����������/��������� ���������� y
    if(delta_x >= delta_y):
        y_i = y0
        for x in range(x0, x1 + 1):
            image.putpixel((x, y_i), color)
            error = error + 2 * delta_y
            if error >= delta_x:
                y_i += diff
                error -= 2 * delta_x
    # ����� - �� ���������� x
    elif(delta_x < delta_y):
        # ��������� ������� ������
        if(diff == -1):
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        x_i = x0
        for y in range(y0, y1 + 1):
            image.putpixel((x_i, y), color)
            error = error + 2 * delta_x
            if error >= delta_y:
                x_i += diff
                error -= 2 * delta_y
    

def filler(image, boundaries, mn, qmx):
    for i in range(mn, qmx+1):
        ## ��������� ������ ����� �����������
        li=[]
        for boundary in boundaries:
            if min(boundary[0][1], boundary[1][1]) <= i <= max(boundary[0][1], boundary[1][1]):
                li.append(math.ceil(boundary[0][0]+(((i-boundary[0][1])*(boundary[1][0]-boundary[0][0]))/(boundary[1][1]-boundary[0][1]))))    
        ## ��������� ����� �� �����������
        li.sort()

        ## ������ ��������� ���������� ����� ������� ����� �������
        for j in range(0, len(li), 2):
            if j+1>=len(li): break
            for x in range(li[j], li[j+1]):
                print((x, i))
                image.putpixel((x, i), (0, 128, 0))

min1 = 5
max1 = 13

boundaries = [[(2, 15), (2, 5)], [(2, 5), (10, 2)], [(10, 2), (13, 10)], [(13, 10), (2, 15)] ]

image = Image.new("RGB", (20, 20))

for i in range(len(boundaries)):
    Bresenham(image, boundaries[i][0][0], boundaries[i][0][1], boundaries[i][1][0], boundaries[i][1][1])

filler(image, boundaries, min1, max1)

plt.imshow(image)
plt.show()
