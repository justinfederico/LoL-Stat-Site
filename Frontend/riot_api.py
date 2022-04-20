import numpy as np
import time
import pandas as pd  # love me some dataframes
import sqlalchemy
from riotwatcher import LolWatcher, ApiError
from sqlalchemy import create_engine


def data_fetch(summoner):
    engine = create_engine(
        'sqlite:///C:\\Users\\justi\\PycharmProjects\\LoL-Stat-Site\\Frontend\\matches.db')  # using relative path
    lol_watcher = LolWatcher('RGAPI-ae43c690-0fcb-4ed8-8c40-a5f8f9f92ce4')  # do NOT share this or post this anywhere.
    my_region = 'na1'  # I don't care about other regions atm
    me = lol_watcher.summoner.by_name('na1', summoner)
    n_games = 5  # just for testing, keep it under 10
    Games = {}  # data container for all match data

    versions = lol_watcher.data_dragon.versions_for_region(my_region)
    champions_version = versions['n']['champion']
    summoner_spells_version = versions['n']['summoner']
    items_version = versions['n']['item']
    current_champ_list = lol_watcher.data_dragon.champions(champions_version)
    current_summoners_list = lol_watcher.data_dragon.summoner_spells(summoner_spells_version)
    my_matches = lol_watcher.match.matchlist_by_puuid('americas',
                                                      me['puuid'])  # this guy right here is the problem child

    j = 0
    cont = 0
    try:
        while cont < n_games:
            match_detail = lol_watcher.match.by_id('americas', my_matches[j])
            participants = []
            for row in match_detail['info']['participants']:
                participants_row = {'summonerName': row['summonerName'], 'champion': row['championId'],
                                    'championName': row['championName'], 'win': row['win'],
                                    'kills': row['kills'], 'deaths': row['deaths'], 'assists': row['assists'],
                                    'summoner1Id': row['summoner1Id'],
                                    'summoner2Id': row['summoner2Id'],
                                    'item1': row['item1'], 'item2': row['item2'], 'item3': row['item3'],
                                    'item4': row['item4'], 'item5': row['item5'], 'item6': row['item6'],
                                    'totalMinionsKilled': row['totalMinionsKilled']}
                participants.append(participants_row)
                Games[j] = pd.DataFrame(participants)

            champ_dict = {}
            for key in current_champ_list['data']:
                row = current_champ_list['data'][key]
                champ_dict[row['key']] = row['id']

            summoners_dict = {}
            for key in current_summoners_list['data']:
                row = current_summoners_list['data'][key]
                summoners_dict[row['key']] = row['id']

                Games[j] = pd.DataFrame(participants)

            j += 1
            cont += 1
            print('Iteration!')
        df = pd.concat(Games)
        print("it did concat")
        print(df)
        df.to_sql('matches', con=engine, if_exists='append')
    except Exception as e:
        cont += 1
        print('Except caught')
        print(e)
    finally:

        xyz = 1


def asset_fetch():
    summonerSpellPath = 0
    summonerRunesPath = 0

# Error Handler

# try:
# response = lol_watcher.summoner.by_name(my_region, summoner)
# except ApiError as err:
# if err.response.status_code == 429:
# print('We should retry in {} seconds.'.format(err.response.headers['Retry-After']))
##print('future requests wait until the retry-after time passes')
# elif err.response.status_code == 404:
# print('Summoner with that stupid ass name not found.')
# else:
# raise
