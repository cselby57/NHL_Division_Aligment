# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import math
from haversine import haversine, Unit

from define import *


"""def haversine(c0, c1):
    ""
    calculate great circle distance between 2 latitude longitude coordinate pairs
    :param c0:
    :param c1:
    :return:
    ""
    R = 6371
    #convert degrees of coordinates to radians
    c00 = c0[0] * math.pi / 180
    c01 = c0[1] * math.pi / 180
    c10 = c1[0] * math.pi / 180
    c11 = c1[1] * math.pi / 180
    a = (math.sin((c10 - c00) / 2)**2) + (math.cos(c00) * math.cos(c10) * math.sin((c11 - c01) / 2)**2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d
"""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('NHL_Distance.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar="'")
        NHL_coords = []
        for row in reader:
            tmp = []
            for dist in row:
                tmp.append(float(dist))
            NHL_coords.append(tmp)
        print(NHL_coords)

    with open('NHL_Distance.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for i, city in enumerate(NHL):
            data = []
            print('Working on ' + city)
            for j in range(32):
                dist = haversine(NHL_coords[i], NHL_coords[j], unit='km')
                if dist < 1.0:
                    dist = 0
                data.append(dist)
            writer.writerow(data)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/


