from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher('RGAPI-33d11744-54bf-40fd-b34c-cf42d5f2b21b')

my_region = 'na1'

me = lol_watcher.summoner.by_name(my_region, 'Fęderico')
print(me)

my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)

versions = lol_watcher.data_dragon.versions_for_region(my_region)
champions_version = versions['n']['champion']

# current_champ_list = lol_watcher.data_dragon.champions(champions_version)
# print(current_champ_list)