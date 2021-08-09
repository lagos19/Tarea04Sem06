
import time
import typing

import telebot
from telebot import types

TOKEN = '1936558355:AAFll2oK0vxucYPqEzh0pf7Ljlc3c0U2Stk'

knownUsers = [] 
userStep = {}  

commands = { 
    
    'start'         : 'Iniciar el bot\n\n',
    'help'          : 'Muestra los comandos disponibles\n\n',
    'conversion'    : 'Use este comando para mostrar el teclado de conversión de unidades\n\n',
    
}

imageSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)  
imageSelect.add('Milímetro', 'Centímetro', 'Metro', 'Kilómetro','Pulgada' ,'Yarda','Milla')

hideBoard = types.ReplyKeyboardRemove()  


def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("Nuevo usuarios detectado, pero no ha usado \"/start\" ")
        return 0


def listener(messages):
    for m in messages:
        if m.content_type == 'text':
                    print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)


bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener) 


@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid not in knownUsers: 
        
        knownUsers.append(cid)  
        userStep[cid] = 0 
        bot.send_message(cid, '¡Hola!')
        bot.send_chat_action(cid, 'typing')  
        time.sleep(1)
        bot.send_message(cid, "Estoy acá para ayudarte")
        bot.send_chat_action(cid, 'typing')  
        time.sleep(1)
        command_help(m) 
    else:
        bot.send_message(cid, "Ya usaste el comando /start, usa el comando /help para visualizar más comandos\n\nÓ bien puedes usar el comando /conversion para realizar una conversion de unidad\n\n")
        bot.send_chat_action(cid, 'typing')  
        time.sleep(4)

@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "Los siguientes comandos están disponibles:\n\n\n"
    bot.send_chat_action(cid, 'typing')  
    time.sleep(5)
    for key in commands: 
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  


@bot.message_handler(commands=['conversion'])
def command_image(m):
    cid = m.chat.id
    bot.send_message(cid, "Presiona la tecla de tu preferencia para mostrar la conversion de la opcion seleccionada a las demas unidades de area ", reply_markup=imageSelect)  
    userStep[cid] = 1 



@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 1)
def msg_image_select(m):
    cid = m.chat.id
    text = m.text

   
    if text == 'Milímetro':
        bot.send_message(cid, "Has seleccionado la unidad: \nMilímetro")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la conversion de la unidad Milímetro a otras unidades de area")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('mm\mm a cm.png', 'rb'),
                       reply_markup=hideBoard)  
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('mm\mm a km.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('mm\mm a m.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('mm\mm a milla.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('mm\mm a mm.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('mm\mm a plg.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('mm\mm a yarda.png', 'rb'),
                       reply_markup=hideBoard) 
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usa el comando /conversion para realizar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "😁")
        userStep[cid] = 0 

    elif text == 'Centímetro':
        bot.send_message(cid, "Has seleccionado la unidad: \nCentímetro")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la conversion de la unidad Centímetro a otras unidades de area")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('cm\cm a cm.png', 'rb'),
                       reply_markup=hideBoard)  
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('cm\cm a km.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('cm\cm a m.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('cm\cm a milla.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('cm\cm a mm.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('cm\cm a plg.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('cm\cm a yarda.png', 'rb'),
                       reply_markup=hideBoard) 

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usa el comando /conversion para realizar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "😁")
        userStep[cid] = 0 

    elif text == 'Metro':
        bot.send_message(cid, "Has seleccionado la unidad: \nMetro")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la conversion de la unidad Metro a otras unidades de area")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('m\m a cm.png', 'rb'),
                       reply_markup=hideBoard)  
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('m\m a km.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('m\m a m.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('m\m a milla.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('m\m a mm.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('m\m a plg.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('m\m a yarda.png', 'rb'),
                       reply_markup=hideBoard) 
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usa el comando /conversion para realizar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "😁")
        userStep[cid] = 0 

    elif text == 'Kilómetro':
        bot.send_message(cid, "Has seleccionado la unidad: \nKilometro")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la conversion de la unidad Kilometro a otras unidades de area")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('km\km a cm.png', 'rb'),
                       reply_markup=hideBoard)  
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('km\km a km.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('km\km a m.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('km\km a milla.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('km\km a mm.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('km\km a plg.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('km\km a yarda.png', 'rb'),
                       reply_markup=hideBoard) 
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usa el comando /conversion para realizar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "😁")
        userStep[cid] = 0 

    elif text == 'Pulgada':
        bot.send_message(cid, "Has seleccionado la unidad: \nPulgada")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la conversion de la unidad Pulgada a otras unidades de area")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('plg\plg a cm.png', 'rb'),
                       reply_markup=hideBoard)  
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('plg\plg a km.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('plg\plg a m.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('plg\plg a milla.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('plg\plg a mm.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('plg\plg a plg.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('plg\plg a yarda.png', 'rb'),
                       reply_markup=hideBoard) 

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usa el comando /conversion para realizar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "😁")
        userStep[cid] = 0 

    elif text == 'Yarda':
        bot.send_message(cid, "Has seleccionado la unidad: \nYarda")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la conversion de la unidad Yarda a otras unidades de area")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('yarda\yarda a cm.png', 'rb'),
                       reply_markup=hideBoard)  
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('yarda\yarda a km.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('yarda\yarda a m.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('yarda\yarda a mila.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('yarda\yarda a mm.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('yarda\yarda a plg.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('yarda\yarda a yarda.png', 'rb'),
                       reply_markup=hideBoard) 

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usa el comando /conversion para realizar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "😁")
        userStep[cid] = 0   

    elif text == 'Milla':
        bot.send_message(cid, "Has seleccionado la unidad: \nMilla")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la conversion de la unidad Milla a otras unidades de area")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('milla\milla a cm.png', 'rb'),
                       reply_markup=hideBoard)  
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('milla\milla a m.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('milla\milla a milla.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('milla\milla a mm.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('milla\milla a yarda.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('milla\milla km.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('milla\milla plg.png', 'rb'),
                       reply_markup=hideBoard) 
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usa el comando /conversion para realizar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "😁")
        userStep[cid] = 0 
     
       
    else:
        bot.send_message(m.chat.id, "No entiendo el texto:\"" + m.text + "\"\nIntenta usar /help para visualizar la lista de comandos disponibles")
        bot.send_message(cid, "Vamos, intentalo de nuevo. ")
        bot.send_message(cid, "😄👍")

@bot.message_handler(func=lambda message: True, content_types=['text'])

def command_default(m):
    bot.send_message(m.chat.id,"No entiendo el texto:\"" + m.text + "\"\nIntenta usar /help para visualizar la lista de comandos disponibles")
    bot.send_message(m, "Vamos, intentalo de nuevo. ")
    bot.send_message(m, "😄👍")

bot.infinity_polling()