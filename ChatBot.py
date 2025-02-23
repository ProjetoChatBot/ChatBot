#Importando bibliotecas para funcionalidades do ChatBot.
import nltk 
from nltk.chat.util import Chat, reflections 
import datetime as Dt 
from tkinter import * 
import random 

#Opções para interação com o usuário.
comidas = ["Pizza", "Hambúrguer", "Sushi", "Salada", "Churrasco", "Tacos"]
lugares = ["Cinemas", "Restaurantes italianos", "Parques", "Praias", "Shopping", "Museus", "Bares"] 
jogos = ["Final Fantasy VII Remake", "Elden Ring", "Uno", "Clue"] 
nome = ["ELLYE", "EMET", "SORA", "WALL"]

#Colocando algumas funções como Hora, Comidas, Jogos, lugares para ir. 
def hora_data(): 
    hora = Dt.datetime.now().strftime("%H:%M:%S") 
    data = Dt.datetime.now().strftime("%d/%m/%Y") 
    return f"A hora e data atuais no Brasil são: {data} e {hora}" 

def sugestao_de_comidas(): 
    return f"O que acha de comer {random.choice (comidas)} hoje ?"

def sugestao_de_lugares(): 
    return f"Que tal sair para um(a) {random.choice(lugares)} hoje ?"

def sugestao_de_jogo(): 
    return f"Por que não jogar um {random.choice(jogos)} hoje ?"

def sugestao_de_nome(): 
    return f"Eu me chamo {random.choice(nome)}."
#Formas de perguntas e respostas. 
patterns = [ 
    (r'Que horas são ?', [hora_data()]),
    (r'oi|olá|bom dia|boa tarde|boa noite', ['Olá! Como posso ajudar você hoje?']),
    (r'como você está ?', ['Estou bem, obrigado! E você?']),
    (r'quem é você ?', ['Eu sou um assistente virtual, com a função de ajudar.']),
    (r'(.*)(ajuda|preciso de ajuda|me ajude|socorro|emergência)', ['Claro! Como posso te ajudar?']),
    (r'qual é a sua função ?', ['Minha função é ajudar com informações e responder perguntas.']),
    (r'(.*)', ['Desculpe, não entendi. Você pode reformular a pergunta?'])
] 

chatbot = Chat(patterns,reflections) 
#Colocando a interação entre usuário e ChatBot
def speak(): 
    entrada_usuario = entry.get() 
    if entrada_usuario.lower() == "sair": 
        chat_log.insert(END, "chatbot: Até logo. ") 
        janela.quit() 
    else:
        chat_log.insert(END, f"Você: {entrada_usuario}\n")

        if "comer" in entrada_usuario or "jantar" in entrada_usuario or "almoço" in entrada_usuario:
            resposta = sugestao_de_comidas()
        elif "onde ir" in entrada_usuario or "diversão" in entrada_usuario:
            resposta = sugestao_de_lugares()
        elif "jogo" in entrada_usuario or "jogar" in entrada_usuario or "o que jogar" in entrada_usuario:
            resposta = sugestao_de_jogo()
        else:
            resposta = chatbot.respond(entrada_usuario) 
        
        chat_log.insert(END, f"chatbot: {resposta}\n") 
        entry.delete(0, END) 
#ChatBot Iniciando interação e explicando o que pode ser perguntado e respondido. 
def interação_com_usuario(): 
    chat_log.insert(END, f"ChatBot: Olá. Me chamo {sugestao_de_nome()} e estou aqui para ajudar. Digite 'Sair' para encerrar.\n" ) 
    chat_log.insert(END, f"ChatBot:No momento posso responder perguntas como: 'Que horas são' 'como você está ?' 'quem é você ?' 'qual é a sua função ?' Caso precise de ajuda digite 'ajuda'.\n")
    chat_log.insert(END, f"ChatBot:Se quiser uma sugestão de comida digite 'comer', Caso queira uma sugestão de jogos digite 'jogo'. Caso queira uma sugestão para onde ir digite 'onde ir'.\n")
    chat_log.insert(END, "ChatBot: Como posso ajudar hoje ?.\n" )

#Tela de interação. 
janela = Tk() 
janela.title("ChatBot") 

chat_log = Text(janela, height=35, width=170)
chat_log.pack() 

entry = Entry(janela, width=170)
entry.pack() 

send_button = Button(janela, text="Enviar", command=speak)
send_button.pack() 

interação_com_usuario()
#Loop para manter a interface até o momento onde o usuário digita "Sair". 
janela.mainloop()