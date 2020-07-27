import requests
import random

from team_rating_factory import get_team_rating
# from plot import {name_of_plot_function}


def gen_linreg_equation():
    r = requests.get('https://api.collegefootballdata.com/games?year=2019&seasonType=regular')
    games = r.json()

    data_x = []
    data_y = []
    for x in range(0, 50):
        indx = random.randint(0, 800)

        home_team = games[indx]['home_team']
        home_points = games[indx]['home_points']
        away_team = games[indx]['away_team']
        away_points = games[indx]['away_points']

        home_rating = get_team_rating(home_team, 2019)
        away_rating = get_team_rating(away_team, 2019)

        if home_rating > away_rating:
            data_x.append(home_rating - away_rating)
            data_y.append(home_points - away_points)
        else:
            data_x.append(away_rating - home_rating)
            data_y.append(away_points - home_points)

    # name_of_plot_function(data_x, data_y)


def main():
    print "Generating Lin Regression Equation"
    gen_linreg_equation()


main()


