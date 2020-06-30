import requests
from team_rating_factory import get_team_rating


def sort_by_rating(e):
    return e['rating']


def get_ratings_by_year(year):
    r = requests.get('https://api.collegefootballdata.com/teams/fbs?year=' + str(year))
    teams = r.json()
    rankings = []
    for team in teams:
        rating = get_team_rating(team['school'], year)
        rankings.append({"team": team['school'], "rating": rating})

    rankings.sort(reverse=True, key=sort_by_rating)
    for ranking in rankings:
        print ranking['team'] + ': ' + str(ranking['rating'])


def main():
    print "Getting team ratings for 2019. This could take about 5 minutes..."
    get_ratings_by_year(2019)


main()


