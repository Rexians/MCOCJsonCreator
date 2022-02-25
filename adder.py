from src.utils import Utils
from src.champs import ChampsInfo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
utils = Utils()
champs = ChampsInfo

cluster = MongoClient(os.environ.get('cluster'))
db = cluster["MCOC"]["Champs"]  

champ = input('Write the champname')

champ_json = {}
error_list = []
for tier in range(2,7):
    ranks = utils.get_ranks_list(tier)
    for rank in ranks:
        try:
            print(f'Going for {tier}* {champ} of rank {rank}')
            champs.get_champ_info(champ, tier, rank)
            champ_json[f"{tier}+{rank}"]= champs.champsjson
            print(f'Scraped {tier}* {champ} of rank {rank}')        
            #await asyncio.sleep(15)                
        except LookupError:
            print(f'Got A Error from {tier}* {champ} of {rank}. \n Document in DB will be created but data will have to be entered manually.')    
            error_list.append(f'{tier}* {champ}, Rank {rank}')
            
champ_json = {'champid':champ, 'data':champ_json}
db.insert_one(champ_json)             
print('DATA ADDED')


cluster = MongoClient(os.environ.get('cluster'))
db = cluster["MCOC"]["Champs"]  

