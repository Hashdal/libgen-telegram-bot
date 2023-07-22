from libgen_api import LibgenSearch
import telebot

def search_by_title(title: str) -> list:
    search = LibgenSearch()
    return search.search_title(title)

def generate_message(result_list: list) -> str:
    message = ''
    count: int = 0
    for i in result_list:
        if count < 10:
            message += 'author: ' + i['Author'] + '\n'
            message += 'title: ' + i['Title'] + '\n'
            message += 'publishe: ' + i['Publisher'] + '\n'
            message += 'year: ' + i['Year'] + '\n'
            message += 'pages: ' + i['Pages'] + '\n'
            message += 'size: ' + i['Size'] + '\n'
            message += 'links:\n'+ i['Mirror_1'] + '\n' + i['Mirror_2'] + '\n' + i['Mirror_3']
            message += '\n\n\n'
            count += 1
    return message



bot = telebot.TeleBot("")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Enter book title:")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, len(search_by_title(message.text)))
    bot.reply_to(message, generate_message(search_by_title(message.text)))

bot.infinity_polling()
