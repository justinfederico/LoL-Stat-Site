import numpy as np
from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher('RGAPI-33d11744-54bf-40fd-b34c-cf42d5f2b21b')  # do NOT share this or post this anywhere.

my_region = 'na1'  # I don't care about other regions atm
me = lol_watcher.summoner.by_name(my_region, summoner)
n_games = 5  # just for testing, keep it under 5
Games = {}  # data container
Game_duration = np.zeros(n_games)
Damage = np.zeros(n_games)

versions = lol_watcher.data_dragon.versions_for_region(my_region)
champions_version = versions['n']['champion']
summoner_spells_version = versions['n']['summoner']
items_version = versions['n']['item']
current_champ_list = lol_watcher.data_dragon.champions(champions_version)
my_matches = lol_watcher.match.matchlist_by_account(my_region, me['accountId'])


# Error Handler

try:
    response = lol_watcher.summoner.by_name(my_region, summoner)
except ApiError as err:
    if err.response.status_code == 429:
        print('We should retry in {} seconds.'.format(err.response.headers['Retry-After']))
        print('this retry-after is handled by default by the RiotWatcher library')
        print('future requests wait until the retry-after time passes')
    elif err.response.status_code == 404:
        print('Summoner with that ridiculous name not found.')
    else:
        raise