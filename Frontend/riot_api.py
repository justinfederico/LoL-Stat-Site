import numpy as np
import time
import pandas as pd  # love me some dataframes
from riotwatcher import LolWatcher, ApiError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
import requests
from flask_sqlalchemy import SQLAlchemy
from Frontend.Nexus import Matches


def data_fetch(summoner):
    metadata = []
    engine = create_engine(
        'sqlite:///C:\\Users\\Jarel Macanas\\PycharmProjects\\LoL-Stat-Site\\Frontend\\matches.db')  # using relative path

    Matches.metadata.create_all(engine)
    lol_watcher = LolWatcher('insert_your_key_here')  # do NOT share this or post this anywhere.
    my_region = 'na1'  # I don't care about other regions atm
    me = lol_watcher.summoner.by_name('na1', summoner)
    n_games = 5  # just for testing, keep it under 10
    Games = {}  # data container for all match data
    match_info = {}

    versions = lol_watcher.data_dragon.versions_for_region(my_region)
    champions_version = versions['n']['champion']
    summoner_spells_version = versions['n']['summoner']
    items_version = versions['n']['item']
    current_champ_list = lol_watcher.data_dragon.champions(champions_version)
    current_summoners_list = lol_watcher.data_dragon.summoner_spells(summoner_spells_version)
    my_matches = lol_watcher.match.matchlist_by_puuid('americas',
                                                      me['puuid'], count=5)  # this guy right here is the problem child

    j = 0
    cont = 0
    try:
        while cont < n_games:
            match_detail = lol_watcher.match.by_id('americas', my_matches[j])
            participants = []
            runes = []

            metadata_row = {'gameMode': match_detail['info']['gameMode'],
                            'gameDuration': match_detail['info']['gameDuration']}
            metadata.append(metadata_row)

            for row in match_detail['info']['participants']:
                participants_row = {'summonerName': row['summonerName'],
                                    'summonerLevel': row['summonerLevel'],
                                    'champion': row['championId'],
                                    'championName': row['championName'], 'win': row['win'],
                                    'kills': row['kills'], 'deaths': row['deaths'], 'assists': row['assists'],
                                    'summoner1Id': row['summoner1Id'],
                                    'summoner2Id': row['summoner2Id'], 'item0': row['item0'],
                                    'item1': row['item1'], 'item2': row['item2'], 'item3': row['item3'],
                                    'item4': row['item4'], 'item5': row['item5'], 'item6': row['item6'],
                                    'totalMinionsKilled': row['totalMinionsKilled'],
                                    'visionWardsBoughtInGame': row['visionWardsBoughtInGame'],
                                    'visionScore': row['visionScore'], 'totalDamageDealt': row['totalDamageDealt'],
                                    'totalDamageDealtToChampions': row['totalDamageDealtToChampions'],
                                    'goldEarned': row['goldEarned'], 'totalDamageTaken': row['totalDamageTaken']}
                # 'perk': row['perk'], 'var1': row['var1'], 'var2': row['var2'], 'var3': row['var3']
                participants.append(participants_row)
                # runes_row = {'perk': row['perks']['styles']['selections']['perk'].values(),
                #              'var1': row['perks']['styles']['selections']['var1'].values(),
                #              'var2': row['perks']['styles']['selections']['var2'].values(),
                #              'var3': row['perks']['styles']['selections']['var3'].values()}
                # runes.append(runes_row)
                # print(runes)
                Games[j] = pd.DataFrame(participants)
                # print(Games[j])
            champ_dict = {}  # sort of useless now since champ assets named after ID only
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
        # Concatenate dataframes into one large dataframe
        df = pd.concat(Games)
        # print(df)
        # Convert Pandas Dataframe to SQL Table
        df.to_sql('matches', con=engine, if_exists='append')




    except Exception as e:
        cont += 1
        print('Except caught')
        print(e)
    finally:
        return metadata



def get_free_champs():
    lol_watcher = LolWatcher('insert_your_key_here')  # do NOT share this or post this anywhere.
    my_region = 'na1'  # I don't care about other regions atm
    free_champs = lol_watcher.champion.rotations(my_region)
    free_champs = free_champs['freeChampionIds']
    return free_champs
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
