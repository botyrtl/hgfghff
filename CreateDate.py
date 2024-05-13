from telebot import TeleBot
import requests
import json

bot = TeleBot(token="6196647198:AAHQFa1vIXEfHgx8pIt_3h0Z0mwwifYChng")
print(bot)
headers = {
    'Host': 'restore-access.indream.app',
    'Connection': 'keep-alive',
    'x-api-key': 'e758fb28-79be-4d1c-af6b-066633ded128',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Length': '25',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
}

    
    
@bot.message_handler(regexp='^/start$')
def start_message(message):
    bot.reply_to(message, f'• مرحبا بك {message.from_user.first_name} \n\n• انا بوت معرفة وقت انشاء حسابك علي تليجرام ، رجاء ارسل ايدي حسابك')
    
@bot.message_handler(func=lambda message: True)
def ids(msg):
    try:
        idd = int(msg.text)
    except:
        bot.reply_to(msg, '• رجاء ارسل ID حسابك بطريقة صحيحة')
        return
    data_Pyro = '{"telegramId":' + str(idd) + '}'
    PyroRobots = requests.post('https://restore-access.indream.app/regdate', headers=headers, data=data_Pyro)

    Pyro = json.loads(PyroRobots.text)
    date = Pyro['data']['date']

    if date:
        bot.reply_to(msg, f'• تاريخ انشاء حسابك علي تليجرام هو {date}')
    else:
        bot.reply_to(msg, 'حدث خطا ، تاكد من ارسال الايدي الخاص بك بشكل صحيح')


bot.infinity_polling()

#Follow us for more : https://t.me/PyroRobots