import requests
from telebot import types
import telebot
from time import sleep
import random
token = '5579108538:AAESRWqicjOXbPkdwf6yIohiAdUKf3Ve5NQ'
bot = telebot.TeleBot(token)
r=requests.session() 
co = types.InlineKeyboardButton(text ="- غنيلي",callback_data = 'check')
#----#


@bot.message_handler(commands=['start'])
def start(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(co)
    bjj = message.chat.id
    bot.send_message(message.chat.id,text=f"""<strong>
Hi <code>{fr}</code>, 
- - - - - - - - - - 
اهلا بك في بوت غنيلي  
اضغط غنيلي ليتم اختيار اغنية عشوائية 
- - - - - - - - - - 
۞︎ ᗪᗴᐯ : @G_D_I
</strong>
    """,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
    if call.data == 'check':
    	combo(call.message)   	
def combo(message):
		bot.send_message(message.chat.id,"<strong>يتم العثور الرجاء الانتظار... </strong>",parse_mode="html")
		rl = random.randint(74,154)
		url = f"https://t.me/song_bott/{rl}"
		bot.send_audio(message.chat.id,url,caption="<strong>الاغنية </strong>",parse_mode="html")
		
    
pass
#داشوفك تريد تخمط
bot.polling(True)