from __future__ import division
import requests


def get_team_rating(team_name, year):
    rating = 0

    # Basic Team Stats
    team_stats_r = \
        requests.get('https://api.collegefootballdata.com/stats/season?year=' + str(year) + '&team=' + team_name)
    team_stats = team_stats_r.json()

    if len(team_stats) > 0:
        games = list(filter(lambda x: x['statName'] == 'games', team_stats))[0]['statValue']

        turnovers_per_game = \
            (list(filter(lambda x: x['statName'] == 'turnovers', team_stats))[0]['statValue'] / games) * 1
        third_down_conversions_per_game = \
            (list(filter(lambda x: x['statName'] == 'thirdDownConversions', team_stats))[0]['statValue'] / games) * 10

        # Advanced Team Stats
        team_adv_stats_r = \
            requests.get('https://api.collegefootballdata.com/stats/season/advanced?year=2019&team=Utah')
        team_adv_stats = team_adv_stats_r.json()

        pass_ppa = team_adv_stats[0]['offense']['passingPlays']['ppa'] * 100
        rush_ppa = team_adv_stats[0]['offense']['rushingPlays']['ppa'] * 100
        offense_success_rate = team_adv_stats[0]['offense']['successRate'] * 100
        pass_d_ppa = team_adv_stats[0]['defense']['passingPlays']['ppa'] * 100
        rush_d_ppa = team_adv_stats[0]['defense']['rushingPlays']['ppa'] * 100
        points_per_opportunity = team_adv_stats[0]['offense']['pointsPerOpportunity'] * 10

        # Team Talent Rankings
        team_talent_r = requests.get('https://api.collegefootballdata.com/talent?year=' + str(year))
        team_talent = team_talent_r.json()
        talent_rating = float(list(filter(lambda x: x['school'] == team_name, team_talent))[0]['talent']) / 15

        # SP Rating
        sp_r = requests.get('https://api.collegefootballdata.com/ratings/sp?year=' + str(year) + '&team=' + team_name)
        sp = sp_r.json()
        sp_rating = sp[0]['rating']

        rating += pass_ppa + rush_ppa + offense_success_rate + points_per_opportunity
        rating += talent_rating + sp_rating + third_down_conversions_per_game
        rating -= (pass_d_ppa + rush_d_ppa + turnovers_per_game)

    return round(rating, 2)

