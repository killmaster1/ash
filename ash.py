from telegram.ext import *
import logging
from random import randint
from time import sleep
import urllib
import re 
import os
import time
import datetime
from def import *
from translate import Translator
updater = Updater(token='1482991149:AAEZ6KBmzIXM0hsvtN18TsbfsQkqcTekXMM', use_context=True)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

dispatcher = updater.dispatcher
dp = updater.dispatcher.add_handler
dp(CommandHandler('f', face))
dp(CommandHandler('stay', stay))
dp(CommandHandler('shuffle', shuffle))
dp(CommandHandler('clima', clima))
dp(CommandHandler('traduzir', traduzir))
dp(CommandHandler('pv', pv))
dp(CommandHandler('draw', draw))
dp(CommandHandler('deck', deck))
dp(CommandHandler('start', start))
dp(CommandHandler('afk', afk))
dp(CommandHandler('cep', cep))
dp(CommandHandler('msg', msg))
dp(CommandHandler('cmds', cmds))
dp(CommandHandler('moeda', moeda))
dp(CommandHandler('username', username))
dp(CommandHandler('rule34', rule34))
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
dp(CommandHandler('cria', cria))
dp(CommandHandler('d', d))
dp(CommandHandler('v', v))
dp(CommandHandler('m', m))
dp(MessageHandler(Filters.command, nulo))
dp(MessageHandler(Filters.text, ler))
dp(MessageHandler(Filters.audio, voz))
dp(MessageHandler(Filters.photo, fotos))
dp(MessageHandler(Filters.document.category("image"), fotos))
dp(MessageHandler(Filters.video, fotos))
dp(MessageHandler(Filters.voice, voz))
updater.start_polling()
updater.idle()
