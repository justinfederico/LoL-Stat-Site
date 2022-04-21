import numpy as np
import time
import pandas as pd  # if SQL was based
from riotwatcher import LolWatcher, ApiError
import sqlite3 as sql

conn = sql.connect('RIOT-API-DATA.sqlite')

lol_watcher = LolWatcher('RGAPI-f8005d6e-8f26-4b34-b46a-acc5a1cceb89')  # do NOT share this or post this anywhere.
summoner = 'Fęderico'
my_region = 'na1'  # I don't care about other regions atm
me = lol_watcher.summoner.by_name('na1', summoner)
n_games = 10  # just for testing, keep it under 5
Games = {}  # data container

versions = lol_watcher.data_dragon.versions_for_region(my_region)
champions_version = versions['n']['champion']
summoner_spells_version = versions['n']['summoner']
items_version = versions['n']['item']
current_champ_list = lol_watcher.data_dragon.champions(champions_version)
current_summoners_list = lol_watcher.data_dragon.summoner_spells(summoner_spells_version)
my_matches = lol_watcher.match.matchlist_by_puuid('americas', me['puuid'])  # this guy right here is the problem child

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
        temp = Games[j]
        temp.to_sql('Match', conn, index=True, if_exists='replace')
        conn.close()
        j += 1
        cont += 1
        print('guh')

except:
    cont += 1

finally:

    xyz = 1
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
