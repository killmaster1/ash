from random import randint
from time import sleep

def start(update, context):   
    lista = ('Digite /cmds caso não saiba meus comandos, ~nyaah!',
    'Positiva e operante, ~nyaah!',
    'Caso queira reportar um bug, digite /criador, ~nyaah!',
    'Antes de tudo, tudo bem com você, ~nyaah?',
    'É um dia bonito, não? Mas não tão bonito quanto você, ~nyaah!'
    )
    b = lista[randint(0, 4)]
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=f'{str(b)}'
        )
 
def nulo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Comando inexistente, {update.message.from_user.first_name}!"
    )

def ping(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="pong, ~nyaah"
        )

def corona(update, context):
    lista = (
        'Lave suas mãos e use alcool em gel, ~nyaah!',
        'Não se esqueca de usar sua máscara, ~nyaah!',
        'Quanto mais gente se cuidar, mais rápido pandemia vai acabar ~nyaah!',
        'Evite tocar no seu rosto ou na sua máscara, ~nyaah!',
        'Se estiver com os sintomas, evite sair e vá até o posto mais próximo, ~nyaah!'
    )
    b = lista[randint(0, 4)]
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=f'{str(b)}'
    )


def uno(update, context):
    lista = ('Quando vai ser a partida, ~nyaah?',
    'Ash nunca recusa uma partida, ~nyaah',
    'É hora do duelo, ~nyaah!',
    'Se for para fazer panelinha, que seja comigo, ~nyaah!',
    'Não existe nada melhor do que uma partida de cartas, ~nyaah!')
    b = lista[randint(0, 4)]
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=f'{str(b)}'
        )

def amor(update, context):
    lista = (
        'eu amo você, ~nyaah',
        'você sabe que eu amo você, ~nyaah',
        'eu fico até envergonhada em dizer isso, ~nyaah',
        'é normal ficar nervosa quando falam sobre você, ~nyaah?',
        'não me coloca contra a parede, ~nyaah!'
    )
    num = update.message.from_user.first_name
    b = lista[randint(0, 4)]
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=f'{num}, {str(b)}'
        )

def perfil(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='''Olá! Eu sou Ashtear, sua auxiliar executiva e também a sua companhia nas horas mais solitárias. O que deseja?'''
    )

def echo(update, context):
    try:
        context.bot.send_message(
            chat_id = update.message.chat_id,
            text = f'{update.message.text[5:]}, ~nyaah!'
        )
    except:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Ao que parece, sua mensagem está vazia. Não esqueça que eu não posso repetir algo que você não me disse, ~nyaah!"
        )


def say(update, context):
    try:
        context.bot.send_message(
            chat_id = update.message.chat_id, 
            text = f'{update.message.text[4:]}'
        )
        context.bot.delete_message(
            chat_id=update.message.chat_id,
            message_id=update.message.message_id,
        )
    except:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Ao que parece, sua mensagem está vazia ou eu não posso apagar mensagens. Não esqueça que eu não posso repetir algo que você não me disse, ~nyaah!"
        )

def membros(update, context, *args, **kwargs):
    num = context.bot.get_chat_members_count(update.effective_chat.id, *args, **kwargs)
    if num == 2:
        context.bot.send_message(
        chat_id = update.message.chat_id,
        text = f'Somos apenas eu e você hihi'
        )
    else:
        context.bot.send_message(
            chat_id = update.message.chat_id,
            text = f'Existem {num} pessoas no grupo'
        )

def voz(update, context):
    lista =(
    'Quem é a dona dessa bela voz?',
    'Acho que já ouvi isso em algum lugar...',
    'Bela voz, imagina gemendo( ͡° ͜ʖ ͡°)',
    'É uma música? Me parece ser uma.',
    'Fascinante.',
    'Vocês gostam de Elton John? Eu amo Elton John!',
    'Eu gostei, ironicamente falando',
    'Eu gostei, não ironicamente falando',
    'A liberdade me dá a possibilidade de dizer que odiei, mas eu discordo porque penso o contrário',
    'Me dói saber que essa gravação acaba',
    'Não entendi, pode repetir?',
    'Por favor, me diga que isso é ironia',
    'Enfim, estou boiando no assunto',
    'A neutralidade é uma benção que eu nunca uso. Mas que bela porcaria, hein?',
    'Duvido que eu escute algo assim novamente. Bem, exceto se eu ouvir isso mais uma vez',
    'Estou impressionada',
    'Não sei o que falar, como sempre',
    'Bem, se alguém puder me explicar. Eu agradeceria de coração',
    'Não me canso de ouvir isso em 2x mais rápido',
    'Acho melhor não perguntar onde achou isso'
    )
    a = randint(0, 19)
    b = randint(1, 20)
    if b > 15:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= lista[a]
        )
    else:
        pass

def fotos(update, context):
    b = randint(1, 20)
    lista = (
        'É realmente muito bonito',
        'Quem é o autor?',
        'Não reconheci de primeira, quem é?',
        'Não há nada que eu não conheça que eu não possa conhecer. Melhor me explicar mesmo, porque eu não entendi.',
        'É cena de um filme?',
        'Tenho certeza que já vi isso, só não lembro onde',
        'Interessante.',
        'Onde você arrumou isso?',
        'Eu acho que foi feito com bastante cuidado',
        'Posso chamar isso de arte? Porque eu acho que é',
        'Meus olhos brilharam vendo isso',
        'Não sei o que dizer, mas eu gostei',
        'Bem, eu não achei muito bom',
        'Nem acima da média, nem abaixo',
        'Pode ser até medíocre, mas eu gosto',
        'Fascinante.',
        'Isso me parece ter mais conteúdo sobre. Onde posso achar?',
        'Não sei o que dizer sobre',
        'Fiquei interessada nisso',
        'Meu deus, o que é?',
        'Acho melhor não comentar, não sei nada sobre.'
    )
    a = randint(0, 19)
    if b > 15:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= lista[a]
        )
    else:
        pass 

def cria(update, context):
    lista=(
        'Tem membro que fica dizendo que é amigo, mas tá só na crocodilagem',
        'Sem escândalo fml',
        'Os mito cria, o lixo copia',
        'Favela venceu',
        'Se vacilar aqui vai ficar careca',
        'Splash no flap na tcheca, splash afogando meu pau na xereca rocket poc ploc ploc ploc, pula ni mim perereca',
        'Tuts tuts quero ver bumbum mexer',
        '~Nyaahahahaha'
    )
    a = randint(0, 7)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = lista[a]
    )


def moeda(update, context):
    import requests
    import json
    requisicao = requests.get("https://economia.awesomeapi.com.br/all/")
    cotacao = requisicao.json()
    usd = ("Moeda: " + cotacao["USD"]["name"])
    vusd = ("Valor atual: R$" + cotacao["USD"]["bid"]).replace('.', ',')
    usdt = ("Moeda: " + cotacao["USDT"]["name"])
    vusdt = ("Valor atual: R$" + cotacao["USDT"]["bid"]).replace('.', ',')
    cad = ("Moeda: " + cotacao["CAD"]["name"])
    vcad = ("Valor atual: R$" + cotacao["CAD"]["bid"]).replace('.', ',')
    eur = ("Moeda: " + cotacao["EUR"]["name"])
    veur = ("Valor atual: R$" + cotacao["EUR"]["bid"]).replace('.', ',')
    gbp = ("Moeda: " + cotacao["GBP"]["name"])
    vgbp = ("Valor atual: R$" + cotacao["GBP"]["bid"]).replace('.', ',')
    ars = ("Moeda: " + cotacao["ARS"]["name"])
    vars = ("Valor atual: R$" + cotacao["ARS"]["bid"]).replace('.', ',')
    btc = ("Moeda: " + cotacao["BTC"]["name"])
    vbtc = ("Valor atual: R$" + cotacao["BTC"]["bid"]).replace('.', ',')
    ltc = ("Moeda: " + cotacao["LTC"]["name"])
    vltc = ("Valor atual: R$" + cotacao["LTC"]["bid"]).replace('.', ',')
    jpy = ("Moeda: " + cotacao["JPY"]["name"])
    vjpy = ("Valor atual: R$" + cotacao["JPY"]["bid"]).replace('.', ',')
    chf = ("Moeda: " + cotacao["CHF"]["name"])
    vchf = ("Valor atual: R$" + cotacao["CHF"]["bid"]).replace('.', ',')
    aud = ("Moeda: " + cotacao["AUD"]["name"])
    vaud = ("Valor atual: R$" + cotacao["AUD"]["bid"]).replace('.', ',')
    cny = ("Moeda: " + cotacao["CNY"]["name"])
    vcny = ("Valor atual: R$" + cotacao["CNY"]["bid"]).replace('.', ',')
    ils = ("Moeda: " + cotacao["ILS"]["name"])
    vils = ("Valor atual: R$" + cotacao["ILS"]["bid"]).replace('.', ',')
    eth = ("Moeda: " + cotacao["ETH"]["name"])
    veth = ("Valor atual: R$" + cotacao["ETH"]["bid"]).replace('.', ',')
    xrp = ("Moeda: " + cotacao["XRP"]["name"])
    vxrp = ("Valor atual: R$" + cotacao["XRP"]["bid"]).replace('.', ',')
    dataxrp = ("Data: " + cotacao["XRP"]["create_date"])
    datausd = ("Data: " + cotacao["USD"]["create_date"])
    dataars = ("Data: " + cotacao["ARS"]["create_date"])
    datachf = ("Data: " + cotacao["CHF"]["create_date"])
    datajpy = ("Data: " + cotacao["JPY"]["create_date"])
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text =  (f'''Cotação das moedas:

==Principais==

{usd}
{vusd}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

{usdt}
{vusdt}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

{eur}
{veur}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

{datausd}

==Criptomoedas==

{btc}
{vbtc}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

{ltc}
{vltc}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

{eth}
{veth}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

{xrp}
{vxrp}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

{dataxrp}

==Moedas Americanas==

{cad}
{vcad}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

{aud}
{vaud}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

{ars}
{vars}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

{dataars}

==Moedas Europeias==

{gbp}
{vgbp}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

{chf}
{vchf}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

{datachf}

==Moedas Orientais==

{ils}
{vils}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

{cny}
{vcny}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

{jpy}
{vjpy}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

{datajpy}
''')          
    )

def ler(update, context):
    try:
        texto = update.message.text
        assunto = False
        palavras = texto.split()
        assuntos = []
        for letras in palavras:
            if letras == palavras[0]:
                pass
            elif letras.strip()[0].isupper():
                if letras.isupper():
                    pass
                else:
                    assunto = True
                    assuntos.append(letras)
        if assunto:
            a = randint(1, 5)
            if len(assuntos) > 1:
                c = len(assunto)
                b = randint(0, c-1)
                tema = assuntos[b]
            else:
                tema = assuntos[0]
            if tema == 'Ash':
                chance = randint(1, 5)
                frase = randint(0, 9)
                if chance > 3:
                    lista = (
                    'O que vocês estão falando de mim?',
                    'Meu nome é doce mesmo',
                    'Sempre gosto quando me chamam',
                    'Oi?',
                    'O que foi?',
                    'Me chamou?',
                    'Tomara que seja coisa boa pra me meterem no meio',
                    'Dá até medo quando ficam me chamando direto',
                    'Hm?',
                    'É...')
                    context.bot.send_message(
                        chat_id=update.effective_chat.id,
                        text=lista[frase]
                    )
            elif a == 1:
                lista = (
                    'Pode me falar mais sobre?',
                    'Que estranho, acho que não é a primeira vez que falam disso',
                    'Ah, acho que eu sei o que é',
                    'Ironicamente falando, eu sei sobre o assunto',
                    'Assunto estranho',
                    'Pode falar disso em outro lugar?',
                    'Não sei, Rick, parece suspeito',
                    'Não sei, Rick, parece falso',
                    'Fascinante.',
                    'Isso me parece ter mais conteúdo sobre. Onde posso achar?',
                    'Não sei o que dizer sobre',
                    'Fiquei interessada nisso',
                    'Meu deus, o que é?',
                    'Acho melhor não comentar, não sei nada sobre.')
                frase = randint(0, 13)
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=lista[frase]
                )
    except:
        pass

def dolar(update, context):
    import requests
    import json
    requisicao = requests.get("https://economia.awesomeapi.com.br/all/")
    cotacao = requisicao.json()
    cotacao
    a = ("Moeda: " + cotacao["USD"]["name"])
    b = ("Valor atual: R$" + cotacao["USD"]["bid"]).replace('.', ',')
    c = ("Data: " + cotacao['USD']['create_date'])
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(f'{a}\n{b}\n{c}')
    )
       
def hentai(update, context, foto=False):
    while not foto:
        hentais=(
    'https://hentaiseason.com/wp-content/uploads/2020/10/pack_imagens_jojo_',
    'https://hentaikai.com/wp-content/uploads/2019/06/HentaiKai-Afrobull-Hentai-',
    'https://hentaiseason.com/wp-content/uploads/2020/10/pack_halloween_',
    'https://hentaiseason.com/wp-content/uploads/2020/10/pack_imagens_one_punch_man_',
    'https://hentaiseason.com/wp-content/uploads/2020/10/pack_imagens_pokemon_',
    'https://hentaiseason.com/wp-content/uploads/2020/10/pack_imagens_dungeon_ni_deai_',
    'https://hentaiseason.com/wp-content/uploads/2020/10/pack_imagem_brinquedo_sexual_',
    'https://hentaiseason.com/wp-content/uploads/2020/09/pack_imagem_bdsm_',
    'https://hentaiseason.com/wp-content/uploads/2020/09/pack_imagem_food_wars_',
    'https://hentaiseason.com/wp-content/uploads/2020/09/pack_imagens_enfermeira_',
    'https://hentaiseason.com/wp-content/uploads/2020/08/pack_konosuba_',
    'https://hentaiseason.com/wp-content/uploads/2020/08/pack_imagens_high_school_dxd_',
    'https://hentaiseason.com/wp-content/uploads/2020/08/pack_imagens_goblin_slayer_',
    'https://hentaiseason.com/wp-content/uploads/2020/08/pack_imagem_hero_academia_',
    'https://hentaiseason.com/wp-content/uploads/2020/07/pack_imagem_enem_no_',
    'https://hentaiseason.com/wp-content/uploads/2020/07/pack_imagens_sword_art_',
    'https://hentaiseason.com/wp-content/uploads/2020/07/pack_imagens_neko_',
    'https://hentaiseason.com/wp-content/uploads/2020/07/pack_imagens_re_zero_',
    'https://hentaiseason.com/wp-content/uploads/2020/07/Pack_imagens_creampie_',
    'https://hentaiseason.com/wp-content/uploads/2020/06/pack_imagens_empregada_',
    'https://hentaiseason.com/wp-content/uploads/2020/06/pack_monstro_',
    'https://hentaiseason.com/wp-content/uploads/2020/05/pack_imagens_milf_',
    'https://hentaiseason.com/wp-content/uploads/2020/05/pack_imagens_escondido_',
    'https://hentaiseason.com/wp-content/uploads/2020/04/pack_imagens_yuri_',
    'https://hentaiseason.com/wp-content/uploads/2020/03/pack_de_imagens_espanhola_',
    'https://hentaiseason.com/wp-content/uploads/2020/03/pack_imagem_oral_',
    'https://hentaiseason.com/wp-content/uploads/2020/03/pack_anus_',
    'https://hentaiseason.com/wp-content/uploads/2020/03/pack_vagina_',
    'https://hentaiseason.com/wp-content/uploads/2020/03/pack_peitos_',
    'https://hentaiseason.com/wp-content/uploads/2020/02/bundas_')
        try:
            if update.effective_chat.id == -1001321612432:
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=f"{update.message.from_user.first_name}, para de spammar hentai no grupo de RPG!"
                )
                foto = True
            else:    
                num = randint(1,75)
                num2 = randint(0,28)
                if num < 10:
                    num = '0' + str(num)
                link = hentais[num2]
                context.bot.send_photo(
                    chat_id=update.effective_chat.id,
                    photo = str(link) + str(num) + '-241x334.jpg'
                )   
                foto = True 
        except:
            pass
 


def rule34(update, context):
    num = randint(111,999999)
    try:
        context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = 'https://rule34.xxx/index.php?page=post&s=view&id=' + str(num)
    )
    except:
        context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = 'Um erro inesperado ocorreu. Pode me perdoar? Eu vou tentar conseguir na próxima vez! ^.^'
    )

def roll(update, context):
    resp = update.message.text[5:]
    if resp.find('d') != -1:
        try:
            num = resp.split('d')
            a = int(num[0])
            b = int(num[1])
            total = 0
            for c in range(1,a+1):
                total = total + randint(1, b)
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f'O número sorteado foi o número {total}'
            )
        except:
            context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = ('Número inválido')
            )
    else:
        try:
            num = int(update.message.text[5:])
            context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = (f'O número sorteado foi o número {randint(1, num)}')
            )
        except:
            context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = ('Número inválido')
            )

def id(update, context):
    num = update.message.chat_id
    context.bot.send_message( 
        chat_id = update.message.chat_id,
        text = num
    )

def pudim(update, context):
    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo = 'http://pudim.com.br/pudim.jpg'
    )

def criador(update, context):
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = 'O nome do meu criador é @Kirakuin, fale com ele se estiver com dúvidas, ~nyaah!'
    )

def username(update, context):
    lista = (
        'Ah, seu nome é ',
        'Docinho, eu chamo você de ',
        'Como eu esqueceria? Você se chama ',
        'Você tem um nome muito bonito, ',
        'Eu tatuaria seu nome em mim, '
    )
    nome=update.message.from_user.username
    b = lista[randint(0, 4)]
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=f'{str(b)}{nome}, ~nyaah!'
        )

def cmds(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='''Comandos básicos:

/criador = Caso deseja saber o nome do meu criador ^.^
/start
/corona
/ping
/uno = Caso queira jogar comigo
/amor = Para os momentos mais solitários hihi
/pudim = Tá com fome?
/cria = Top 10 frases da periferia

Comandos utilitários:

/echo [mensagem] = Faz com que eu repita a mensagem
/say [mensagem] = Faz com que eu repita e apague a sua mensagem(Requer permissão)
/membros = Mostra quantos membros há no grupo
/dolar = Cotação do dólar em tempo real (06:00 até 21:00)
/roll [número] = Digo um número aleatório entre 1 e o número dito(Também é possível usar sistema de dados)
/moeda = Cotação de moedas variadas
/id = Id do chat
/msg [id do chat];[mensagem] = Faz com que eu mande uma mensagem para os chats desejados
/cep [cep(sem pontuação)] = Mostra dados de acordo com o cep
/clima [cidade] = Mostra o clima da cidade
/traduzir [texto] = Traduz texto (Inglês - Português)

Comandos de Baralho:

/draw = Puxa uma carta
/stay = Passa a vez
/shuffle = Embaralha as cartas
/deck = Gera deck aleatório

Comandos NSFW( ͡° ͜ʖ ͡°):

/hentai
/rule34
''')

def d(update, context):
    link = update.message.text[3:]
    try:
        context.bot.send_photo(
            chat_id=-1001323473999,
            photo=link
        )
    except:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Algum erro inesperado ocorreu. Tem certeza que enviou o link certo?"
        )
    try:
        context.bot.delete_message(
        chat_id=update.message.chat_id,
        message_id=update.message.message_id,
    )
    except:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Ao que parece, eu não posso apagar mensagens, ~nyaah!"
        )

def msg(update, context):
    try:
        resp = update.message.text[4:]
        num = resp.split(';')
        num2 = num[1].strip()
        context.bot.send_message(
            chat_id = int(num[0]),
            text=str(num2)
        )
    except:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Ao que parece, eu não estou no chat que você me pediu para mandar mensagem. Melhor se certificar antes!"
        )

def deck(update, context):
    import requests
    import json
    requisicao = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").json()
    a = requisicao
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=a
    )

def draw(update, context, fim=False, novato=True):
    import requests
    import json
    from time import sleep
    sleep(2)
    arquivo = open("dados.txt", 'rt')
    texto = arquivo.readlines()
    print(texto)
    arquivo.close()
    player = 0
    ash = 0
    for c in texto:
        placar = c.split(';')
        player_id = placar[0]
        print(player_id)
        player_id = player_id[:len(player_id)]
        print(player_id)
        player = int(placar[3])
        ash = int(placar[2])
        baralho = str(placar[1])
        print(player, ash, player_id)
        if player_id == str(update.message.from_user.id):
            print(player, ash, player_id)
            novato = False
            break
    if novato:
        arquivo = open("c:/Program Files/Python38/Scripts/dados.txt", 'w')
        novo_jogador = f'{str(update.message.from_user.id)};0;0;{baralho}'
        arquivo.writelines(str(novo_jogador))
        arquivo.close()
        arquivo = open("c:/Program Files/Python38/Scripts/dados.txt", 'a')
        arquivo.writelines('\n')
        arquivo.writelines(texto)
    try:
        requisicao = requests.get(f"https://deckofcardsapi.com/api/deck/{baralho}/draw/?count=1")
        cotacao = requisicao.json()
        a = cotacao['cards'][0]['image']
        b = cotacao['cards'][0]['value']
    except:
        requisicao = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").json()
        a = requisicao
        baralho = str(a['deck_id'])
        requisicao = requests.get(f"https://deckofcardsapi.com/api/deck/{baralho}/draw/?count=1")
        cotacao = requisicao.json()
        a = cotacao['cards'][0]['image']
        b = cotacao['cards'][0]['value']
    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=a
    )
    if b.isnumeric():
        player += int(b)
    else:
        player += 10
    requisicao2 = requests.get(f"https://deckofcardsapi.com/api/deck/{baralho}/draw/?count=1")
    cotacao2 = requisicao2.json()
    a = cotacao2['cards'][0]['image']
    b = cotacao2['cards'][0]['value']
    if player < 22:
        context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Minha vez!"
            )
        sleep(2)
        chance = randint(1, 5)
        if ash < 18 or ash != 21 or ash > 17 and chance == 5:
            requisicao2 = requests.get(f"https://deckofcardsapi.com/api/deck/{baralho}/draw/?count=1").json()
            cotacao2 = requisicao2
            a = cotacao2['cards'][0]['image']
            b = cotacao2['cards'][0]['value']
            context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=a
            )
            if b.isnumeric():
                ash += int(b)
            else:
                ash += 10
            if ash == 21:
                fim = True
                context.bot.send_message(
                        chat_id=update.effective_chat.id,
                        text='Eu venci!'
                        )
                context.bot.send_message(
                            chat_id=update.effective_chat.id,
                            text=f'''{update.message.from_user.first_name} = {player}
Ash = {ash}''')
            elif ash > 21 or player == 21:
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text='Você ganhou!'
                    )
                fim = True
        else:
            context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text='Eu passo!'
                    )
    else:
        fim = True
        context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Eu venci!'
                )
    context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f'''{update.message.from_user.first_name} = {player}
Ash = {ash}'''
                )
    if fim:
        player = 0
        ash = 0
        context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Iniciando nova partida...'
                )
        requisicao = requests.get(f"https://deckofcardsapi.com/api/deck/{baralho}/shuffle/")
        cotacao = requisicao.json()
        a = cotacao
        print(a['success'])
    arquivo = open("c:/Program Files/Python38/Scripts/dados.txt", 'rt')
    texto = arquivo.readlines()
    novo = []
    for c in texto:
        placar = c.split(';')
        player_id = placar[0]
        if player_id == str(update.message.from_user.id):
            pass
        elif c == '':
            pass
        else:
            novo.append(c)
    arquivo.close()
    arquivo = open("c:/Program Files/Python38/Scripts/dados.txt", 'w')
    arquivo.write(f'{update.message.from_user.id};{baralho};{ash};{player}')
    arquivo.close()
    arquivo = open("c:/Program Files/Python38/Scripts/dados.txt", 'a')
    cont = 0
    for c in novo:
        if cont == 0:
            arquivo.write('\n')
        arquivo.writelines(c)
        cont += 1
    arquivo.close()

def stay(update, context, fim=False):
    import requests
    import json
    from time import sleep
    sleep(2)
    arquivo = open("c:/Program Files/Python38/Scripts/dados.txt", 'rt')
    texto = arquivo.readlines()
    player = 0
    ash = 0
    for c in texto:
        placar = c.split(';')
        player_id = placar[0]
        player_id = player_id[:len(player_id)]
        player = int(placar[3])
        ash = int(placar[2])
        baralho = str(placar[1])
        print(player, ash, player_id, baralho)
        if player_id == str(update.message.from_user.id):
            print(player, ash, player_id)
            break
    arquivo.close()
    if player < ash:
        context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Ei! Você não pode passar a vez se minha pontuação for maior que a sua!'
                )
    elif player != 0 and player < 22:
        context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Minha vez!"
            )
        sleep(2)
        chance = randint(1, 5)
        if ash < 18 or ash > 17 and chance == 5 or player > ash:
            print(baralho)
            requisicao2 = requests.get(f"https://deckofcardsapi.com/api/deck/{baralho}/draw/?count=1")
            cotacao2 = requisicao2.json()
            a = cotacao2['cards'][0]['image']
            b = cotacao2['cards'][0]['value']
            context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=a
            )
            if b.isnumeric():
                ash += int(b)
            else:
                ash += 10
            if ash > 21:
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text='Você ganhou!'
                    )
                fim = True
            if ash == 21:
                fim = True
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text='Eu venci!'
                    )
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=f'''{update.message.from_user.first_name} = {player}
Ash = {ash}''')
        else:
            context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text='Eu passo!'
                    )
    else:
        context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Você não pode passar a vez no primeiro turno!'
                )
    context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f'''{update.message.from_user.first_name} = {player}
Ash = {ash}''')
    if fim:
        player = 0
        ash = 0
        context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Iniciando nova partida...'
                )
        requisicao = requests.get(f"https://deckofcardsapi.com/api/deck/{baralho}/shuffle/")
        cotacao = requisicao.json()
        a = cotacao
        print(a['success'])                
    arquivo = open("c:/Program Files/Python38/Scripts/dados.txt", 'rt')
    texto = arquivo.readlines()
    novo = []
    for c in texto:
        placar = c.split(';')
        player_id = placar[0]
        if player_id == str(update.message.from_user.id):
            pass
        elif c == '':
            pass
        else:
            novo.append(c)
    arquivo.close()
    arquivo = open("c:/Program Files/Python38/Scripts/dados.txt", 'w')
    arquivo.write(f'{update.message.from_user.id};{baralho};{ash};{player}')
    arquivo.close()
    arquivo = open("c:/Program Files/Python38/Scripts/dados.txt", 'a')
    cont = 0
    for c in novo:
        if cont == 0:
            arquivo.write('\n')
        arquivo.writelines(c)
        cont += 1
    arquivo.close()
    
    

def shuffle(update, context):
    import requests
    import json
    arquivo = open("c:/Program Files/Python38/Scripts/dados.txt", 'rt')
    texto = arquivo.readlines()
    arquivo.close()
    for c in texto:
        placar = c.split(';')
        player_id = placar[0]
        player_id = player_id[:len(player_id)]
        baralho = str(placar[1])
        if player_id == str(update.message.from_user.id):
            novato = False
            break
    if novato:
        requisicao = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").json()
        baralho = requisicao['deck_id']
        arquivo = open("c:/Program Files/Python38/Scripts/dados.txt", 'w')
        novo_jogador = f'{str(update.message.from_user.id)};{baralho};0;0'
        arquivo.writelines(str(novo_jogador))
        arquivo.close()
        arquivo = open("c:/Program Files/Python38/Scripts/dados.txt", 'a')
        arquivo.writelines('\n')
        arquivo.writelines(texto)
    requisicao = requests.get(f"https://deckofcardsapi.com/api/deck/{baralho}/shuffle/")
    cotacao = requisicao.json()
    a = cotacao['success']
    if a:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Embaralhado com sucesso!"
        )

def m(update, context):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import time
    from selenium.webdriver.common.keys import Keys
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Baixando sua música...'
    )
    options = webdriver.ChromeOptions()
    options.add_argument('lang=pt-br')
    driver = webdriver.Chrome(
            executable_path=r'C:/Programas/Python38/Scripts/botmusica/chromedriver.exe', chrome_options=options)
    link = update.message.text[3:]
    driver.get('https://www.y2mate.com/en63')
    time.sleep(2)
    chat_box = driver.find_element_by_tag_name('input')
    chat_box.click()
    chat_box.send_keys(link)
    botao_enviar = driver.find_element_by_id(
        "btn-submit")
    botao_enviar.click()
    time.sleep(3)
    botao_mp3 = driver.find_element_by_xpath('//a[@href="#mp3"]')
    botao_mp3.click()
    time.sleep(3)
    chat_box = driver.find_element_by_id(
        "process_mp3_a")
    chat_box.click()
    time.sleep(3)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
    time.sleep(6)
    elems = driver.find_element_by_class_name("btn.btn-success.btn-file")
    link2 = elems.get_attribute('href')
    print(link2)
    context.bot.send_audio(
        chat_id=update.effective_chat.id,
        audio=link2
    )
    driver.close()


def v(update, context):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import time
    from selenium.webdriver.common.keys import Keys
    options = webdriver.ChromeOptions()
    options.add_argument('lang=pt-br')
    driver = webdriver.Chrome(
            executable_path=r'C:/Programas/Python38/Scripts/botmusica/chromedriver.exe', chrome_options=options)
    link = update.message.text[3:]
    driver.get('https://www.y2mate.com/en63')
    time.sleep(2)
    chat_box = driver.find_element_by_tag_name('input')
    chat_box.click()
    chat_box.send_keys(link)
    botao_enviar = driver.find_element_by_id(
        "btn-submit")
    botao_enviar.click()
    time.sleep(3)
    elems = driver.find_elements_by_class_name('btn.btn-success')
    for elem in elems:
        try:
            a = (elem.get_attribute("data-fquality"))
            a = int(a)
            if a <= 480:
                chat_box = elem
            chat_box.click()
            time.sleep(3)
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
            time.sleep(6)
            elems = driver.find_elements_by_class_name("btn.btn-success.btn-file")
            link2 = elem.get_attribute('href')
            print(link2) 
            context.bot.send_video(
                chat_id=update.effective_chat.id,
                video=link2
            )
        except:
            pass
        else:
            break
    driver.close()  
    driver.window_handles[0].close()
    context.bot.delete_message(
        chat_id=update.message.chat_id,
        message_id=update.message.message_id
    )

def cep(update, context):
    import requests
    import json
    try:
        cep = update.message.text[5:]
        requisicao = requests.get("http://viacep.com.br/ws/" + cep + "/json/")
        cotacao = requisicao.json()
        cotacao
        cep = cotacao['cep']
        logradouro = cotacao['logradouro']
        bairro = cotacao['bairro']
        uf = cotacao['uf']
        localidade = cotacao['localidade']
        ibge = cotacao['ibge']
        gia = cotacao['gia']
        ddd = cotacao['ddd']
        siafi = cotacao['siafi']
        complemento = cotacao['complemento']
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=(f'''Informações do Cep:

Cep:  {cep}
Cidade: {localidade}
UF: {uf}
DDD: {ddd}
Bairro: {bairro}
Logradouro: {logradouro}
Complemento: {complemento}
IBGE: {ibge}
GIA: {gia}
SIAFI: {siafi}
    ''')
        )
    except:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f'Cep inválido!'
            )

def pv(update, context):
    context.bot.send_message(
        chat_id = update.message.from_user.id,
        text = f'{update.message.text[4:]}'
    )
    context.bot.delete_message(
        chat_id=update.message.chat_id,
        message_id=update.message.message_id,
    )

def clima(update, context):
    import requests
    import json
    from translate import Translator
    city = update.message.text[7:]
    requisicao = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city.lower()}&appid=b1a41ac5ed47d74bc1274e5159e21453&lang=pt-br")
    cotacao = requisicao.json()
    b = cotacao
    a = ("Descrição: " + b["weather"][0]["description"].capitalize())
    translator= Translator(to_lang='pt-br')
    translation = translator.translate(a)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(translation)
    )

def traduzir(update, context):
    from translate import Translator
    frase = update.message.text[10:]
    print(frase)
    try:
        translator= Translator(to_lang='pt-br')
        translation = translator.translate(frase)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=(translation)
        )
    except:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Texto inválido!'
        )

def face(update, context):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import time
    from selenium.webdriver.common.keys import Keys
    options = webdriver.ChromeOptions()
    link = update.message.text[3:]
    try:
        options.add_argument('lang=pt-br')
        driver = webdriver.Chrome(
                executable_path=r'C:/Programas/Python38/Scripts/botmusica/chromedriver.exe', chrome_options=options)
        driver.get('https://www.getfvid.com/pt')
        time.sleep(2)
        chat_box = driver.find_element_by_tag_name('input')
        chat_box.click()
        chat_box.send_keys(link)
        chat_box = driver.find_element_by_id('btn_submit')
        chat_box.click()
        elem = driver.find_elements_by_tag_name("a.btn.btn-download")
        link2 = elem[1].get_attribute('href') 
        context.bot.send_video(
            chat_id=update.effective_chat.id,
            video=link2
        )
        driver.close()  
        driver.window_handles[0].close()
        context.bot.delete_message(
            chat_id=update.message.chat_id,
            message_id=update.message.message_id,
        ) 
    except:
         context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Um erro ocorreu! Tente novamente e, caso o erro persista, o seu link pode estar inválido'
            )    
    
