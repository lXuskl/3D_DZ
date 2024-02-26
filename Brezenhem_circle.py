from PIL import Image, ImageOps, ImageDraw
import matplotlib.pyplot as plt


def brezenhem_circle(center_x, center_y, radius):
    # ������� ���� ��� ����������� ���������� ��� ������������� ��������� ������� ��� ����������� ���� ����������
    size = (max(center_x, center_y, radius) * 2)
    image = Image.new("RGB", (size * 2 + 1, size * 2 + 1))
    draw = ImageDraw.Draw(image)

    temp_x = radius
    temp_y = 0
    d = 1 - radius
    points = []

    while temp_x >= temp_y:
        # ��������� ������������ ����� ��� ����������, ������ ��������� �����
        points.extend([(temp_x, temp_y), (-temp_x, temp_y), (temp_x, -temp_y), (-temp_x, -temp_y),
                            (temp_y, temp_x), (-temp_y, temp_x), (temp_y, -temp_x), (-temp_y, -temp_x)])

        temp_y += 1
        if d < 0:
            d += 2 * temp_y + 1
        else:
            temp_x -= 1
            d += 2 * (temp_y - temp_x) + 1

    # ������� ����� � ������������ � ��������� ������������ ������
    points = [(size - x - center_x, size - y - center_y) for x, y in points]

    # ������ ��� ��������� ����� ������
    for x in range(2 * size + 1):
        draw.point((x, size), (100, 100, 100))
        draw.point((size, x), (100, 100, 100))

    # ������ ���������� �� ������� �������������� ������
    for point in points:
        draw.point(point, (255, 255, 255))

    # �������� ����������� �� �����������, ����� ��� �� ���� ������������
    image = ImageOps.mirror(image)

    plt.figure('Brezenhem circle')  # ����� �������� ����
    plt.imshow(image)
    plt.axis('off')  # ��������� ����������� ����������� ����
    plt.show()

def main():
    center_x = int(input('center x = '))  # ���������� x ������ ����������
    center_y = int(input('center y = '))  # ���������� x ������ ����������
    radius = int(input('radius = '))  # ���������� x ������ ����������

    brezenhem_circle(center_x, center_y, radius)
