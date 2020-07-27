import requests
import random
from team_rating_factory import get_team_rating


#    def sort_by_rating(e):
#    return e['rating']


#    def get_ratings_by_year(year):
#    r = requests.get('https://api.collegefootballdata.com/teams/fbs?year=' + str(year))
#    teams = r.json()
#    rankings = []
#    for team in teams:
#        rating = get_team_rating(team['school'], year)
#        rankings.append({"team": team['school'], "rating": rating})

#    rankings.sort(reverse=True, key=sort_by_rating)
#    for ranking in rankings:
#        print ranking['team'] + ': ' + str(ranking['rating'])

def gen_linreg_equation():
    # Get Games
    r = requests.get('https://api.collegefootballdata.com/games?year=2019&seasonType=regular')
    games = r.json()
    data = []

    # Loop through 50 ?
    for x in range(0, 50):
        indx = random.randint(0, 200)
        home_rating = get_team_rating(games[indx].home_team)
        away_rating = get_team_rating(games[indx].away_team)

        if home_rating > away_rating:
            data.append([home_rating - away_rating, games[indx].home_points - games[indx].away_points])
        else:
            data.append([away_rating - home_rating, games[indx].away_points - games[indx].home_points])

    # Use Pandas to gen equation


def main():
    print "Generating Lin Regression Equation"
    gen_linreg_equation()


main()


