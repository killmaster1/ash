from telegram.ext import *
import logging
from random import randint
from time import sleep
import urllib
import re 
import os
import time
import datetime
from defs import *
from translate import Translator
updater = Updater(token='1482991149:AAEZ6KBmzIXM0hsvtN18TsbfsQkqcTekXMM', use_context=True)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def now(update, context):
    from datetime import datetime
    nhe = str(datetime.today())
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'''Data: {nhe[:10]}
Hora: {nhe[11:19]}'''
    )

def agora(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=str(update.message.date)
    )

def times():
    from datetime import datetime
    minuto = datetime.today()
    return minuto.minute

dispatcher = updater.dispatcher
dp = updater.dispatcher.add_handler
dp(CommandHandler('reply', reply))
dp(CommandHandler('f', face))
dp(CommandHandler('prev', previsão))
dp(CommandHandler('stay', stay))
dp(CommandHandler('shuffle', shuffle))
dp(CommandHandler('clima', clima))
dp(CommandHandler('traduzir', traduzir))
dp(CommandHandler('pv', pv))
dp(CommandHandler('draw', draw))
dp(CommandHandler('deck', deck))
dp(CommandHandler('now', now))
dp(CommandHandler('agora', agora))
dp(CommandHandler('start', start))
dp(CommandHandler('afk', afk))
dp(CommandHandler('cep', cep))
dp(CommandHandler('gorfe', gorfe))
dp(CommandHandler('fake', fake))
dp(CommandHandler('jojo', jojo))
dp(CommandHandler('trap', trap))
dp(CommandHandler('msg', msg))
dp(CommandHandler('batman', batman))
dp(CommandHandler('cmds', cmds))
dp(CommandHandler('moeda', moeda))
dp(CommandHandler('username', username))
dp(CommandHandler('rule34', rule34))
dp(CommandHandler('xd', xd))
dp(CommandHandler('bola', bola))
dp(CommandHandler('id', id))
dp(CommandHandler('echo', echo))
dp(CommandHandler('corona', corona))
dp(CommandHandler('ping', ping))
dp(CommandHandler('uno', uno))
dp(CommandHandler('amor', amor))
dp(CommandHandler('perfil', perfil))
dp(CommandHandler('membros', membros))
dp(CommandHandler('dolar', dolar))
dp(CommandHandler('say', say))
dp(CommandHandler('hentai', hentai))
dp(CommandHandler('roll', roll))
dp(CommandHandler('pudim', pudim)) 
dp(CommandHandler('criador', criador))
dp(CommandHandler('pinto', pinto))
dp(CommandHandler('face', face))
dp(CommandHandler('cria', cria))
dp(CommandHandler('d', d))
dp(CommandHandler('v', v))
dp(CommandHandler('m', m))
dp(CommandHandler('mamaco', mamaco))
dp(MessageHandler(Filters.command, nulo))
dp(MessageHandler(Filters.text, ler))
dp(MessageHandler(Filters.audio, voz))
dp(MessageHandler(Filters.photo, fotos))
dp(MessageHandler(Filters.document.category("image"), fotos))
dp(MessageHandler(Filters.video, fotos))
dp(MessageHandler(Filters.voice, voz))
updater.start_polling()
updater.idle()
