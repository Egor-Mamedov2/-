import requests


URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "2ed6713cc00f5460651ba615635a2689"
HEADER = {"Content-Type" : "application/json", "trainer_token" : TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "egor.mamedov2015@yandex.ru",
    "password": "3452009Xxyyzz"
}
body_confirmation ={
    "trainer_token": "2ed6713cc00f5460651ba615635a2689"
}
body_create = {
    "name": "Жук",
    "photo_id": 12
}
body_add = {
    "pokemon_id": "322610"
}


'''response = requests.post(url = f"{URL}/trainers/reg", headers= HEADER, json = body_registration)
print(response.text)'''


'''response_confirmation = requests.post(url = f"{URL}/trainers/confirm_email", headers= HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f"{URL}/pokemons", headers= HEADER, json = body_create)
print(response_create.text)
message = response_create.json() ["message"]
print(message)'''

response_add = requests.post(url = f"{URL}/trainers/add_pokeball", headers= HEADER, json = body_add)
print(response_add.text)