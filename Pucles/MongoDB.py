import pymongo
import datetime
import time
import threading
import requests

class MongoClient:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://mongo:XdBnLOwoTIxEBJnRKBAWHkVALkdyrGFP@junction.proxy.rlwy.net:10004")
        self.db = self.client["Tumbado"]
        self.users = self.db["users"]
        self.grupo = self.db["grupo"]
        self.keys = self.db["keys"]
        self.collection_cuatro = self.db['gates']

    def command_query(self, command_name):
        return self.collection_cuatro.find_one({"comando": command_name})

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def user_query(self, user_id):
        return self.users.find_one({"user_id": user_id})

    def grupo_query(self, id: int = None):
        return self.grupo.find_one({"id": id})

    def grupo_eliminar(self, id: int = None):
        return self.grupo.delete_one({"id": id})

    def key_query(self, key):
        return self.keys.find_one({"key": key})

    def register_user(self, id: int = None, rango: str = 'User', creditor: int = 0, antispam: int = 60, dias: int = 0, bin_lasted: str = None, fecha_registro=None):
        data = {
            'user_id': id,
            'rango': rango,
            'plan': 'Free',
            'creditos': creditor,
            'antispam': antispam,
            'dias': dias,
            'bin_lasted': bin_lasted,
            'fecha_registro': fecha_registro,
            'since': None
        }
        self.users.insert_one(data)

    def save_grupos(self, id, dias):
        tiempo_futuro = datetime.datetime.now() + datetime.timedelta(days=dias)
        times = tiempo_futuro.timestamp()
        data = {'id': id, 'dias': times}
        self.grupo.insert_one(data)

    def save_key(self, key, dias):
        data = {'key': key, 'dias': dias}
        self.keys.insert_one(data)

    def addcr(self, id, addcr):
        query = self.users.find_one({"user_id": id})
        self.users.update_one({'user_id': id}, {'$set': {'creditos': query['creditos'] + addcr}})

    def removecr(self, id, addcr):
        query = self.users.find_one({"user_id": id})
        self.users.update_one({'user_id': id}, {'$set': {'creditos': query['creditos'] - addcr}})

    def rango(self, id, rango):
        self.users.update_one({'user_id': id}, {'$set': {'rango': rango}})

    def addpremium(self, id, dia):
        tiempo_futuro = datetime.datetime.now() + datetime.timedelta(days=dia)
        times = tiempo_futuro.timestamp()
        self.users.update_one({'user_id': id}, {'$set': {'plan': 'Premium', 'antispam': 10, 'since': times}})

    def delete_key(self, key):
        result = self.keys.delete_one({'key': key})
        if result.deleted_count > 0:
            print(f"𝑲𝒆𝒚 𝒆𝒍𝒊𝒎𝒊𝒏𝒂𝒅𝒂 𝒅𝒆 𝒌𝒆𝒚𝒔 '𝒌𝒆𝒚𝒔': '{key}'")
            return True

        user_with_key = self.users.find_one({'key': key})
        if user_with_key:
            self.users.update_one({'user_id': user_with_key['user_id']}, {'$unset': {'key': ''}})
            print(f"Clave eliminada exitosamente del usuario en 'users': '{key}'")
            return True

        print(f"𝑵𝒐 𝒔𝒆 𝒆𝒏𝒄𝒐𝒏𝒕𝒓𝒐 𝒍𝒂 𝒌𝒆𝒚 𝒑𝒂𝒓𝒂 𝒆𝒍𝒊𝒎𝒊𝒏𝒂𝒓: '{key}'")
        return False

    def ban(self, id):
        self.users.update_one({'user_id': id}, {'$set': {'rango': 'Baneado'}})
    
    def unban(self, id):
        self.users.update_one({'user_id': id}, {'$set': {'rango': 'Free'}})

    def seller(self, id):
        query = self.users.find_one({"user_id": id})
        if query:
            return any(role in query['rango'] for role in ['Owner', 'Admin', 'Co-funder', 'Seller'])
        return False

def expulse_user():
    client = MongoClient()
    
    while True:
        for user in client.grupo.find({"dias": {"$lt": time.time()}}):
            client.grupo_eliminar(user['id'])
            url = 'https://api.telegram.org/bot7525326531:AAF8TClx_5BBLipsThktc7nJ01KmxQqb9pc/sendMessage'
            params = {'chat_id': user['id'], 'text': '<b>𝑺𝒆 𝒉𝒂 𝒕𝒆𝒓𝒎𝒊𝒏𝒂𝒅𝒐 𝒆𝒍 𝒂𝒄𝒄𝒆𝒔𝒐 𝒂𝒍 𝒈𝒓𝒖𝒑𝒐 𝒅𝒆 𝒏𝒖𝒆𝒔𝒕𝒓𝒐 𝑩𝒐𝒕.❗️</b>', 'parse_mode': 'HTML'}
            requests.post(url=url, params=params)
            url = 'https://api.telegram.org/bot7525326531:AAF8TClx_5BBLipsThktc7nJ01KmxQqb9pc/sendMessage'
            params = {'chat_id': -4599741972, 'text': f'<b>𝑺𝒆 𝒉𝒂 𝒕𝒆𝒓𝒎𝒊𝒏𝒂𝒅𝒐 𝒆𝒍 𝒂𝒄𝒄𝒆𝒔𝒐 𝒅𝒆 𝒅𝒊𝒂𝒔 𝒂𝒍 𝒄𝒉𝒂𝒕 𝑰𝑫: {user["id"]}❗️</b>', 'parse_mode': 'HTML'}
            requests.post(url=url, params=params)

    
        for user in client.users.find({"since": {"$lt": time.time()}}):
            client.users.update_one({"user_id": user["user_id"]}, {"$set": {"plan": "free", "antispam": 40, "key": None, "since": None}})
            client.grupo_eliminar(user['user_id'])
            url = 'https://api.telegram.org/bot7525326531:AAF8TClx_5BBLipsThktc7nJ01KmxQqb9pc/sendMessage'
            params = {'chat_id': user['user_id'], 'text': '<b>𝑺𝒆 𝒉𝒂 𝒕𝒆𝒓𝒎𝒊𝒏𝒂𝒅𝒐 𝒕𝒖 𝒂𝒄𝒄𝒆𝒔𝒐 𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝒆𝒏 𝒏𝒖𝒆𝒔𝒕𝒓𝒐 𝒃𝒐𝒕.❗️</b>', 'parse_mode': 'HTML'}
            requests.post(url=url, params=params)
            url = 'https://api.telegram.org/bot7525326531:AAF8TClx_5BBLipsThktc7nJ01KmxQqb9pc/sendMessage'
            params = {'chat_id': -4599741972, 'text': f'<b>𝑺𝒆 𝒉𝒂 𝒕𝒆𝒓𝒎𝒊𝒏𝒂𝒅𝒐 𝒆𝒍 𝒂𝒄𝒄𝒆𝒔𝒐 𝒅𝒆𝒍 𝒃𝒐𝒕 𝒂𝒍 𝒖𝒔𝒆𝒓: {user["user_id"]}❗️</b>', 'parse_mode': 'HTML'}
            requests.post(url=url, params=params)

        time.sleep(3600)

thread2 = threading.Thread(target=expulse_user)
thread2.start()
