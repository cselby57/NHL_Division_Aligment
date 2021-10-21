from define import *

NHL_coords = []


class NHLDivision:
    def __init__(self, name):
        """
        :param name: division name, used to identify partnered (close) divisions
        """
        self.name = name
        self.group = ()
        self.other = ()
        self.teams = [1, 2, 3, 4]

    def add_teams(self, teams: list):
        """
        :param teams: tuple of teams in the division
        :return:
        """
        self.teams = teams

    def init_teams(self):
        # collect the teams from the group divisions
        group_teams = []
        other_teams = []
        for division in self.group:
            group_teams.append(division.get_teams)
        for division in self.other:
            other_teams.append(division.get_teams)

        # let each team know who their new division partners are
        # let each team know which teams are in their group divisions
        for team in self.teams:
            tmp = self.teams
            team.add_division(tmp.remove(team))
            team.add_group(tuple(group_teams))
            team.add_others(tuple(other_teams))



    def add_group(self, group: tuple):
        """
        :param group: list of divisions to play extra games against
        :return: void
        """
        self.group = group

    def get_teams(self):
        """
        :return: tuple of teams in the division
        """
        return tuple(self.teams)

    def reset(self):
        self.teams = [1, 2, 3, 4]


class NHLTeam:
    """
    This class will contain the information specific to a team and methods to calculate the total distance
    that team would travel during a full season.
    """
    def __init__(self, city, lat, long):
        self.city = city
        self.index = NHL_cities.index(city)
        self.latitude = lat
        self.longitude = long
        self.dist = 0
        self.division = ()
        self.group = ((), ())
        self.other = ((), (), (), (), ())

    def get_distance(self):
        """
        calculate the total distance traveled during a full season
        assumptions on distance travelled:
            distances between cities are great circle distances between arenas
            travel to another city always begins from the home city, road trips to multiple cities are not considered
                this is not a travelling salesperson problem as NHL team travel will vary drastically depending on the
                order of opponents in the schedule from year to year. The goal is create optimum clusters of
                geographically close cities to minimize the average travel across multiple seasons.
            road / home games are accounted by scaling the number of games played by 1/2
        :return: the totol distance to all other cities scaled by the number of games played against each team
        """

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

    def add_group(self, group: tuple):
        """
        :param group: tuple of divisions to play additional games against
        :return: void
        """
        self.group = group

    def add_division(self, teams: tuple):

    def add_others(self, other: tuple):

    def reset(self):
        """
        reset division alignment objects for the next iteration
        :return: void
        """
        self.dist = 0
        self.division = ()
        self.group = ((), ())
        self.other = ((), (), (), (), ())