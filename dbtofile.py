from pymongo import MongoClient
import json
import os
from dotenv import load_dotenv

load_dotenv()


def get_json_from_db():
    cluster = MongoClient(os.environ.get('cluster'))
    db = cluster["MCOC"]["Champs"]

    champsjson = db.find(None,{'_id':0})
    return champsjson

def get_data(champid):
    cluster = MongoClient(os.environ.get('cluster'))
    db = cluster["MCOC"]["Champs"]

    champsjson = db.find_one({'champid':champid},{'_id':0})
    if champsjson is not None:
        return champsjson   
    else:
        return False     

def create_json(name:str, data:dict):
    try:    
        with open(f'./files/{name}.json', 'w') as f:
            json.dump(data, f, indent=4)
            return True
    except:
        return False

def db_to_json():
    data = get_json_from_db()
    datalist = []
    for champsdata in data:
        datalist.append(champsdata)
    with open('./files/champs.json', 'w') as f:
        json.dump(datalist, f)    

def main():
    champid = input('Write the name of newly added champ: ')
    data = get_data(champid)
    if data is False:
        print('champid is wrong or data not found.')
    else:    
        with open('./files/champs.json', 'r') as f:
            pre_data = json.load(f)

        if data in pre_data:
            print('Data already exists.')
        else:
            new_data = pre_data.append(data)
            with open('./files/champs.json', 'w') as f:
                json.dump(new_data, f)
                print('Data added!')



if __name__ == '__main__':
    op = input('Add champdata in files folder or update?(add/update): ')
    if op == 'add':
        db_to_json()
    elif op == 'update':
        main()    
    else:
        print('Wrong option.')

