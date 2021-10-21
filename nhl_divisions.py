import csv

from nhl_team import NHLTeam, NHLDivision

NHL = []



if __name__ == '__main__':
    with open('NHL_Distance_qouted.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar="'")
        NHL_coords = []
        for row in reader:
            tmp = []
            for dist in row:
                tmp.append(float(dist))
            NHL_coords.append(tmp)
        #print(NHL_coords)
        print("Coordinates loaded")