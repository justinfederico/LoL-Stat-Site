import numpy as np
import time
import pandas as pd  # if SQL was based
from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher('RGAPI-e9b2b885-07ce-4637-904e-4dd3e208fc90')  # do NOT share this or post this anywhere.
summoner = 'Fęderico'
my_region = 'na1'  # I don't care about other regions atm
me = lol_watcher.summoner.by_name('na1', summoner)
n_games = 20  # just for testing, keep it under 5
Games = {}  # data container
Game_duration = np.zeros(n_games)  # extracts duration of match
Damage = np.zeros(n_games)  # extracts amount of damage

versions = lol_watcher.data_dragon.versions_for_region(my_region)
champions_version = versions['n']['champion']
summoner_spells_version = versions['n']['summoner']
items_version = versions['n']['item']
current_champ_list = lol_watcher.data_dragon.champions(champions_version)
my_matches = lol_watcher.match.matchlist_by_puuid('americas', me['puuid'])  # this guy right here is the problem child

j = 0
cont = 0
while cont < n_games:
    try:
        last_match = my_matches['matches'][cont]
        match_detail = lol_watcher.match.by_id('americas', last_match['gameId'])
        print("it made it this far")
        participants = []
        for row in match_detail['participants']:
            participants_row = {}
            participants_row['champion'] = row['championId']
            participants_row['win'] = row['stats']['win']
            participants_row['assists'] = row['stats']['assists']
            participants.append(participants_row)
        Games[j] = pd.DataFrame(participants)
        champ_dict = {}
        for key in static_champ_list['data']:
            row = static_champ_list['data'][key]
            champ_dict[row['key']] = row['id']

        summoners_dict = {}
        for key in static_summoners_list['data']:
            row = static_summoners_list['data'][key]
            summoners_dict[row['key']] = row['id']
        Summoner_name = []
        for row in match_detail['participantIdentities']:
            Summoner_name_row = {}
            Summoner_name_row = row['player']['summonerName']
            Summoner_name.append(Summoner_name_row)
        i = 0
        for row in participants:
            row['championName'] = champ_dict[str(row['champion'])]
            row['Summoner_name'] = Summoner_name[i]
            row['Summoner Spell 1'] = summoners_dict[str(row['spell1'])]
            row['Summoner Spell 2'] = summoners_dict[str(row['spell2'])]
            i += 1

        Games[j] = pd.DataFrame(participants)
        for index, row in Games[j].iterrows():
            if row['Summoner_name'] == summoner:
                Damage[j] = row['totalDamageDealt']
                # Gold[j] = row['goldEarned']
        time.sleep(10)
        j += 1
        cont += 1
    except:
        cont += 1

# Error Handler

# try:
# response = lol_watcher.summoner.by_name(my_region, summoner)
# except ApiError as err:
# if err.response.status_code == 429:
# print('We should retry in {} seconds.'.format(err.response.headers['Retry-After']))
##print('future requests wait until the retry-after time passes')
# elif err.response.status_code == 404:
# print('Summoner with that ridiculous name not found.')
# else:
# raise
