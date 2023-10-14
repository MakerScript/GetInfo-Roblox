## pip install requests

import requests

data = {}

choice = int(input('(1) RU or (2) US >>> '))
def Choice():
    if choice == 1:
        data['[Бан]'] = zapros['isBanned']
        data['[Ник]'] = zapros['name']
        data['[Дисплей ник]'] = zapros['displayName']
        data['[Айди]'] = zapros['id']
        data['[Когда был создан]'] = zapros['created']
        data['[Имеит-ли бейдж вереф]'] = zapros['hasVerifiedBadge']
    elif choice == 2:
        data['[Ban]'] = zapros['isBanned']
        data['[Name]'] = zapros['name']
        data['[Display Name]'] = zapros['displayName']
        data['[User Id]'] = zapros['id']
        data['[Created]'] = zapros['created']
        data['[Has verified badge]'] = zapros['hasVerifiedBadge']

if choice == 1:
    id_profile = int(input('Введите айди пользователя >>> '))
elif choice == 2:
    id_profile = int(input('Enter userID >>> '))

zapros = requests.get(url=f'https://users.roblox.com/v1/users/{id_profile}').json()

Choice()

with open(f'UserInfo-{id_profile}.txt', "w", encoding='utf-8') as f:
    for k, v in data.items():
        f.write(f'\n{k} : {v}')

with open(f'UserInfo-{id_profile}.txt', "r", encoding='utf-8') as f:
    content = f.read()
    if f'[Айди] : {id_profile}' or f'[User Id] : {id_profile}' in content:
        if choice == 1:
            print('Получилось!')
        elif choice == 2:
            print('Saved!')
    else:
        if choice == 1:
            print('Не получилось')
        elif choice == 2:
            print('Not saved')
