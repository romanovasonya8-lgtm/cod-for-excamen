USERS=[
    {"login":"admin", "password":"admin", "role":"Администратор", "full_name":"Администратор системы", "locked":False},
    {"login":"ivanov", "password":"1234", "role":"Пользователь", "full_name":"Иванов Иван", "locked":True},
    {"login":"petrov", "password":"petrov", "role":"Пользователь", "full_name":"Петров Петр", "locked":False},
]

def find_user(login, password):  
    for u in USERS:
        if u['login']==login and u['password']==password:
            return u
    return None