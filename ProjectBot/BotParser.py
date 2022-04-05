from pyrogram import Client, filters  # телеграм клиент

# взегда можно сделать print(message) // и увидеть список информации которую можно извлечь
Gmessage = ""

API_ID = 7906995
API_HASH = '6d2cf947c1caaece9fb2fb50db17a363'

#Bot_ID_ADM = 1793275901 # для отправления себе в избранное
CHENAL_ID = -1001428325485

PUBLIC_PUBLIC = 'IT Энергия'  # паблик куда будем репостить

SOURCE_PUBLICS = [
    # список пабликов-доноров, откуда бот будет пересылать посты
    'andro-price.com',
    'Alexandr Semak - СКИДКИ и ОБЗОРЫ на гаджеты',
]
PHONE_NUMBER = '89170493967'  # номер зарегистрованный в телеге

# создаем клиент телеграм
app = Client("cyberpunk", api_id=API_ID, api_hash=API_HASH,
             phone_number=PHONE_NUMBER)

@app.on_message()
def echo(client, message):
    # "-1001253787508" or "-1001426377751" or
    if message.chat.id == "-1001701624730" or "850434834":
        #app.send_message(CHENAL_ID, message.text)
        app.send_message(CHENAL_ID, reply_to_message_id=message.message_id)

if __name__ == "__main__":
    app.run()

''' Дневник фитч:
    app.send_poll(CHENAL_ID, "Is this a poll question?", ["Yes", "No", "Maybe"]) # для отправки опросников
'''
