# users.py

import os, json

DATA_PATH = '03/users.json'

def read_data():
    with open(DATA_PATH, encoding='utf-8') as file:
        return json.load(file)

def write_data(data):
    with open(DATA_PATH, mode="w", encoding='utf-8') as file:
        json.dump(data, file) # zapís do json

def check_password(password, password_repeat):
    if password != password_repeat:
        raise ValueError('Hesla se neshodují')

def check_username(data, username):
    if username in data:
        raise ValueError('Uživatel již existuje')

def register(username, password, password_repeat):
    check_password(password, password_repeat)
    data = read_data()
    check_username(data, username)
    data[username] = password
    write_data(data)

def login(username, password):
    data = read_data()
    try:
        assert data[username] == password, 'Chybné heslo'
        return True
    except (KeyError, AssertionError):
        return False

def change_password(old_password, password, password_repeat):
    pass

def delete_user(username, password):
    """
    1. načteme json 
    2. najdeme ho pokud ho najdeme
    3. smažeme
    4. uložíme json
    """
    data = read_data()
    if username in data and data[username] == password:
        del data[username]
        write_data(data)

#register('test123', 'heslo', 'heslo')

print(login('hello', 'Python'))
print(login('test', 'heslo'))
delete_user('test', 'hesloaaaaaaaaaa')