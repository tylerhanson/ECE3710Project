import requests
import random

from team_rating_factory import get_team_rating
from Plot import x_y_


def gen_linreg_equation():
    r = requests.get('https://api.collegefootballdata.com/games?year=2019&seasonType=regular')
    games = r.json()

    data_x = []
    data_y = []
    for x in range(0, 50):
        indx = random.randint(0, 500)

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

    x_y_(data_x, data_y)


def test_straight_up_accuracy():
    r = requests.get('https://api.collegefootballdata.com/games?year=2019&seasonType=regular')
    games = r.json()

    x = 0.0846
    y = 9.7504
    number_correct = 0
    for i in range(0, len(games)):
        indx = i

        home_team = games[indx]['home_team']
        home_points = games[indx]['home_points']
        away_team = games[indx]['away_team']
        away_points = games[indx]['away_points']

        home_rating = get_team_rating(home_team, 2019)
        away_rating = get_team_rating(away_team, 2019)

        if home_rating > away_rating:
            margin_of_victory = home_points - away_points
            if margin_of_victory > 0:
                number_correct = number_correct + 1
        else:
            margin_of_victory = away_points - home_points
            if margin_of_victory > 0:
                number_correct = number_correct + 1

        print "Pass: " + str(indx) + " - Accuracy = " + str(number_correct)

    print "Straight Up Accuracy: " + str(number_correct) + "/" + str(len(games))


def test_against_vegas_accuracy():
    r = requests.get('https://api.collegefootballdata.com/games?year=2019&seasonType=regular')
    games = r.json()

    x = 0.0846
    y = 9.7504
    number_correct = 0
    number_processed = 0
    for i in range(0, 400):
        indx = random.randint(0, len(games))

        br = requests.get('https://api.collegefootballdata.com/lines?gameId=' + str(games[indx]['id'])
                          + '&year=2019&seasonType=regular')
        bet_info = br.json()

        if bet_info[0] and bet_info[0]['lines'][0]:
            number_processed = number_processed + 1

            home_team = games[indx]['home_team']
            home_points = games[indx]['home_points']
            away_team = games[indx]['away_team']
            away_points = games[indx]['away_points']

            home_rating = get_team_rating(home_team, 2019)
            away_rating = get_team_rating(away_team, 2019)

            predicted_winner = ""
            expected_spread = 0
            margin_of_victory = 0
            if home_rating > away_rating:
                predicted_winner = home_team
                expected_spread = (x * (home_rating - away_rating)) + y
                margin_of_victory = home_points - away_points
            else:
                predicted_winner = away_team
                expected_spread = (x * (away_rating - home_rating)) + y
                margin_of_victory = away_points - home_points

            line = bet_info[0]['lines'][0]['formattedSpread']
            if predicted_winner in line:

                spread = float(bet_info[0]['lines'][0]['spread'])
                if expected_spread > spread:
                    if margin_of_victory > spread:
                        number_correct = number_correct + 1
                else:
                    if margin_of_victory < spread:
                        number_correct = number_correct + 1

                print str(number_correct) + "/" + str(number_processed)

    print "Against Vegas Accuracy: " + str(number_correct) + "/" + str(number_processed)


def test_game_spreads_prediction_accuracy():
    r = requests.get('https://api.collegefootballdata.com/games?year=2019&seasonType=regular')
    games = r.json()

    x = 0.0846
    y = 9.7504
    number_correct = 0
    for i in range(0, len(games)):
        indx = i

        home_team = games[indx]['home_team']
        home_points = games[indx]['home_points']
        away_team = games[indx]['away_team']
        away_points = games[indx]['away_points']

        home_rating = get_team_rating(home_team, 2019)
        away_rating = get_team_rating(away_team, 2019)

        predicted_winner = ""
        margin_of_victory = 0
        if home_rating > away_rating:
            predicted_winner = home_team
            expected_spread = (x * (home_rating - away_rating)) + y
            margin_of_victory = home_points - away_points
        else:
            predicted_winner = away_team
            expected_spread = (x * (away_rating - home_rating)) + y
            margin_of_victory = away_points - home_points

        if expected_spread <= margin_of_victory:
            number_correct = number_correct + 1

    print "Spread Predictor Accuracy: " + str(number_correct) + "/" + str(len(games))


def main():
    # test_game_spreads_prediction_accuracy()  #49.7%
    # test_straight_up_accuracy()  # 83.5%
    # test_against_vegas_accuracy()  # 65.3
    gen_linreg_equation()


main()
