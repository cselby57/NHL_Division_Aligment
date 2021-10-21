NHL_cities = ['Anaheim','Arizona','Boston','Buffalo','Calgary','Carolina','Chicago','Colorado','Columbus','Dallas',
       'Detroit','Edmonton','Florida','Las Vegas','Los Angeles','Minnesota','Montreal','Nashville','New Jersey ',
       'New York Islanders','New York Rangers','Ottawa','Philadelphia','Pittsburgh','San Jose','Seattle','St Louis',
       'Tampa Bay','Toronto','Vancouver','Washington','Winnipeg']


intra_division_games = 6  # 18
close_division_games = 3  # 24
far_division_games = 2  # 40



Division_Groups = ((2, 3), (1, 4), (1, 5), (2, 6), (3, 7), (4, 8), (5, 8), (6, 7))
#                    1        2       3      4        5      6        7      8



"""
wacky playoff style

intra_division_games = 4  # 12
close_division_games = 3  # 24
far_division_games = 2  # 40
76 games





Last 6 games - all games count for regular season points totals

top 4 division winners by points - play each other 2 times for seeds 1-4, determined by points in the 6 games
bottom 4 division winners by points - play each other 2 times for seeds 5-8, determined by points in the 6 games
middle 16 teams - play 6 games against other middle 16 teams, seeds 8-16 determined by season points total including the 6 games
bottom 8 teams by points - play against 6 of the 7 other teams, drafts spots 1-8 determined by highest points in the 6 games

alternate middle 16
2nd and 3rd seeds in their division play 2 games head to head + 1 game against each of the 2nd and 3rd seeds from their close divisions
"""
