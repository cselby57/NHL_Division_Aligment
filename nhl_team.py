from define import *

NHL_coords = []


class NHLdivision:
    def __init__(self):
        self.teams = [1, 2, 3, 4]

    def add_teams(self, NHL_slice):
        self.teams = NHL_slice

    def reset(self):
        self.teams = [1, 2, 3, 4]


class NHLTeam:
    def __init__(self, city, lat, long):
        self.city = city
        self.index = NHL_cities.index(city)
        self.latitude = lat
        self.longitude = long
        self.dist = 0
        self.division = None
        self.group = [[], []]
        self.other = [[], [], [], [], []]

    def get_distance(self):
        # iterate through all other teams in nhl
        # add distance between cities weighted by number of games played based on relationship between divisions
        for team in self.division:
            self.dist += NHL_coords[self.index][team.index] * 0.5 * intra_division_games
        for team in self.group[0]:
            self.dist += NHL_coords[self.index][team.index] * 0.5 * close_division_games
        for team in self.group[1]:
            self.dist += NHL_coords[self.index][team.index] * 0.5 * close_division_games
        for division in self.other:
            for team in division:
                self.dist += NHL_coords[self.index][team.index] * 0.5 * far_division_games


    def add_group(self, a, b):
        self.group[0] = a
        self.group[1] = b

    def reset(self):
        self.dist = 0
        self.division = None
        self.group = [None, None]
        self.other = [None, None, None, None, None]