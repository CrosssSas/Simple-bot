import telebot
from telebot import types

token = <your_token>

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о Tesla?', reply_markup=keyboard)
    bot.send_message(message.chat.id, 'Напиши /help, чтобы узнать, что я умею')

@bot.message_handler(commands=['help'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    bot.send_message(message.chat.id, 'Я умею:\n'
                                      'Напиши слово "Хочу", чтобы перейти на официальный сайт Tesla\n'
                                      '/tradelist - Актуальные предложения о продаже.\n'
                                      '/charalist - Характеристики моделей\n'
                                      'Напиши слово "карта", чтобы увидеть мировую карту электрозаправок Tesla\n'
                                      'Напиши слово "список", чтобы увидеть список актуальности моделей Tesla\n'
                                      'Напиши слово "ремонт", чтобы увидеть топ автомастерских', reply_markup=keyboard)


@bot.message_handler(commands=['tradelist'])
def start_message1(message):
    bot.send_message(message.chat.id, '[Tesla Motors Model S](https://auto.ru/cars/tesla/model_s/all/)', parse_mode='Markdown')
    bot.send_message(message.chat.id, '[Tesla Motors Model 3](https://auto.ru/cars/tesla/model_3/all/)', parse_mode='Markdown')
    bot.send_message(message.chat.id, '[Tesla Motors Model X](https://auto.ru/cars/tesla/model_x/all//)', parse_mode='Markdown')

@bot.message_handler(commands=['charalist'])
def start_message2(message):
    bot.send_message(message.chat.id, 'Нажми на интересующую модель, чтобы узнать характеристики:')
    bot.send_message(message.chat.id, '/tesla_Motors_Model_S')
    bot.send_message(message.chat.id, '/tesla_Motors_Model_3')
    bot.send_message(message.chat.id, '/tesla_Motors_Model_X')

@bot.message_handler(commands=['tesla_Motors_Model_S'])
def start_message2(message):
    bot.send_message(message.chat.id, 'Тип батареи: литий-ионная\n'
                                      'Объем батареи: 85 / 60 кВт⋅ч*\n'
                                      'Запас хода до полной зарядки: 426 / 335 км*\n'
                                      'Ресурс: 7 лет или 160 тыс. км\n'
                                      'Габариты батареи: Длина — 2.1 м, Ширина — 1.2 м, Высота — 15 см\n'
                                      'Вес батареи:~450 кг\n'
                                      'Время зарядки от бытовой сети переменного тока 110В: за 1 час восполняется 8 км пути\n'
                                      'Время зарядки от бытовой сети переменного тока 220В: за 1 час восполняется 50 км пути\n'
                                      'Время полной зарядки на станции Tesla Supercharger: 30 минут и бесплатно')


@bot.message_handler(commands=['tesla_Motors_Model_3'])
def start_message2(message):
    bot.send_message(message.chat.id, 'LONG RANGE:\n'
                                      'Разгон от 0 до 100 км/ч - 4.4 сек\n'
                                      'Запас хода 614 км\n'
                                      'Мощность двигателя 460 л.с.\n'
                                      'Максимальная скорость 233 км/ч\n'
                                      'Привод AWD\n'
                                      'Стоимость в Москве 4 650 000 млн/рублей\n'
                                      'Perfomance:\n'
                                      'Разгон от 0 до 100 км/ч - 3.3 сек\n'
                                      'Запас хода 567 км\n'
                                      'Мощность двигателя 520 л.с.\n'
                                      'Максимальная скорость 261 км/ч\n'
                                      'Привод AWD\n'
                                      'Стоимость в Москве 10 300 000 млн/рублей')


@bot.message_handler(commands=['tesla_Motors_Model_X'])
def start_message2(message):
    bot.send_message(message.chat.id, 'Long Range\n'
                                      'два двигателя, полный привод\n'
                                      '580 километров — запас хода;\n'
                                      '3,9 секунды — разгон с 0 до 100 миль в час;\n'
                                      '250 км/ч — максимальная скорость.\n'
                                      '$89990 — цена базовой версии.\n'
                                      'Plaid\n'
                                      'три двигателя, полный привод, 1020 л.с.\n'
                                      '547 километров — запас хода;\n'
                                      '2,6 секунды — разгон с 0 до 100 миль в час;\n'
                                      '262 км/ч — максимальная скорость.\n'
                                      '$119990 — цена базовой версии.\n')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://www.tesla.com/')
    if message.text.lower() == "список":
        bot.send_message(message.chat.id, 'Tesla Motors Model S (2012 - сегодня)\n'
                                          'Tesla Motors Model 3 2016 - 2016\n'
                                          'Tesla Motors Model X 2017 - сегодня')
    if message.text.lower() == "карта":
        bot.send_message(message.chat.id, 'https://www.plugshare.com/ru')
    if message.text.lower() == "ремонт":
        bot.send_message(message.chat.id, 'https://www.x-tesla.ru/tesla-service\n'
                                          'https://teesla.ru/\n'
                                          'https://moscowteslaclub.ru/service/')




bot.infinity_polling()
