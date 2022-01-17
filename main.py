import sys
import time
from src.utils import Utils
from src.champs import ChampsInfo
import json
import os

champs_list = ['abomination', 'abomination_immortal', 'aegon', 'agentvenom', 'airwalker', 'americachavez', 'angela', 'annihilus', 'antman', 'antivenom', 'apocalypse', 'archangel', 'beast', 'bishop', 'blackbolt', 'blackpanther', 'blackpanther_cw', 'blackwidow', 'blackwidow_timely', 'blackwidow_movie', 'blade', 'cable', 'captainamerica', 'captainamerica_movie', 'captainamerica_ww2', 'captainmarvel_movie', 'captainmarvel', 'carnage', 'civilwarrior', 'colossus', 'corvusglaive', 'ghostrider_cosmic', 'crossbones', 'cullobsidian', 'cyclops_90s', 'cyclops', 'daredevil', 'daredevil_netflix', 'darkhawk', 'deadpool', 'deadpool_xforce', 'diablo', 'doctordoom', 'doc_ock', 'drstrange', 'brothervoodoo', 'domino', 'dormammu', 'dragonman', 'drax', 'ebonymaw', 'electro', 'elektra', 'elsabloodstone', 'emmafrost', 'falcon', 'gambit', 'gamora', 'ghost', 'ghostrider', 'deadpool_gold', 'green_goblin', 'groot', 'guardian', 'guillotine', 'guillotine_2099', 'gwenpool', 'havok', 'hawkeye', 'heimdall', 'hela', 'hercules', 'hitmonkey', 'howardmech', 'hulk', 'hulk_immortal', 'hulk_ragnarok', 'hulkbuster_movie', 'humantorch', 'hyperion', 'iceman', 'ikaris', 'invisiblewoman', 'ironfist', 'ironfist_white', 'ironman', 'ironman_movie', 'ironpatriot', 'blackpanther_realm', 'joefixit', 'jubilee', 'juggernaut', 'kang', 'karnak', 'killmonger', 'groot_king', 'kingpin', 'kittypryde', 'knull', 'korg', 'kraven', 'loki', 'longshot', 'lukecage', 'modok', 'magik', 'magneto', 'magneto_marvelnow', 'manthing', 'mangog', 'masacre', 'medusa', 'mephisto', 'mrfantastic', 'misternegative', 'mistersinister', 'mojo', 'moleman', 'moonknight', 'karlmordo', 'morningstar', 'msmarvel', 'msmarvel_kamala', 'mysterio', 'namor', 'nebula', 'nickfury', 'nightthrasher', 'nightcrawler', 'nimrod', 'nova', 'odin', 'wolverine_oldman', 'omegared', 'peniparker', 'phoenix', 'deadpool_platinum', 'professorx', 'proximamidnight', 'psychoman', 'psylocke', 'punisher', 'punisher_2099', 'purgatory', 'quake', 'red_goblin', 'redguardian', 'hulk_red', 'redskull', 'rhino', 'rocket', 'rogue', 'ronan', 'ronin', 'sabretooth', 'sasquatch', 'sauron', 'scarletwitch_current', 'scarletwitch', 'sentinel', 'sentry', 'sersi', 'shangchi', 'shehulk', 'ironman_silvercenturion', 'silversurfer', 'drstrange_realm', 'spidergwen', 'spiderham', 'spiderman', 'spiderman_morales', 'spiderman_movie', 'spiderman_stealth', 'spiderman_black', 'spiderman_2099', 'squirrelgirl', 'starlord', 'storm', 'storm_realm', 'stryfe', 'sunspot', 'skrull_super', 'ironman_superior', 'symbiotesupreme', 'taskmaster', 'terrax', 'thanos', 'champion', 'hood', 'maestro_overseer', 'thing', 'thor', 'thor_janefoster', 'thor_ragnarok', 'tigra', 'toad', 'ultron', 'ultron_prime', 'colossus_unstoppable', 'venom', 'venomtheduck', 'venompool', 'vision', 'vision_timely', 'vision_movie', 'void', 'vulture_movie', 'warmachine', 'warlock', 'wasp', 'wintersoldier', 'wolverine', 'wolverine_weaponx', 'x23', 'yellowjacket', 'yondu']
error_list = []

utils = Utils()
champs = ChampsInfo()

print('''\033[1;32m 
  _____ _                                      _  _____  ____  _   _    _____                _             
 / ____| |                                    | |/ ____|/ __ \| \ | |  / ____|              | |            
| |    | |__   __ _ _ __ ___  _ __  ___       | | (___ | |  | |  \| | | |     _ __ ___  __ _| |_ ___  _ __ 
| |    | '_ \ / _` | '_ ` _ \| '_ \/ __|  _   | |\___ \| |  | | . ` | | |    | '__/ _ \/ _` | __/ _ \| '__|
| |____| | | | (_| | | | | | | |_) \__ \ | |__| |____) | |__| | |\  | | |____| | |  __/ (_| | || (_) | |   
 \_____|_| |_|\__,_|_| |_| |_| .__/|___/  \____/|_____/ \____/|_| \_|  \_____|_|  \___|\__,_|\__\___/|_|   
                             | |                                                                           
                             |_|                                                                           
''')

start_input = input('Type to start! (Y/N)')
start_input = start_input.upper()
if start_input == 'Y':

    dir_exist = os.path.isdir('./files')
    if dir_exist:
        print('/files directory found. All jsons will be stored there.')
    else:
        print('\033[1;31m/files directory doesn\'t exist, creating one.')
        os.makedirs('./files')    


    for champ in champs_list:
        champ_list = []
        champ_json = {}
        for tier in range(2,7):
            ranks = utils.get_ranks_list(tier)
            for rank in ranks:
                sigs = utils.get_sig_list(tier)
                for signature in sigs:
                    try:
                        print(f'\033[1;34m Going for {tier}* {champ} of rank {rank} and sig {signature}')
                        champs.get_champ_info(champ, tier, rank, signature)
                        champ_json[f"{tier}+{rank}+{signature}"]= champs.champsjson
                    except LookupError:
                        print(f'\033[1;31m Got A Error from {tier}* {champ} of {rank} and sig {signature}. \n File will be created but data will have to be entered manually.')    
                        error_list.append(f'{tier}* {champ}, Rank {rank}, Sig {signature}')
                    except KeyboardInterrupt:
                        print('\033[1;31m Okay Stopping')
                        time.sleep(5)
                        sys.exit()
        f = open(f"./files/{champ}.json", "x")     
        with open(f"./files/{champ}.json",'r+') as file: 
            json.dump(champ_json, file, indent = 4)

    if len(error_list) == 0:
        print('\033[1;32m No Errors came :D #Winning!')
    else:
        print('\033[1;31m At last, the errors that came were-')
        for error in error_list:
            print(error)     
        list_input = input('Want the Error list to be printed? (Y/N)')
        list_input = list_input.upper()
        if list_input == "Y":
            print(error_list)
            print('\033[1;31m Shutting down! ')
        else:
            print('I will take this as a No :(')                
else:
    print('\033[1;31m Okay then! Exiting!')
    time.sleep(5)
    sys.exit()

