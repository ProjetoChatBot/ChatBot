#Importando bibliotecas para funcionalidades do ChatBot.
import nltk 
from nltk.chat.util import Chat, reflections 
import datetime as Dt 
from tkinter import * 
import random 

# Opções para interação com o usuário.
comidas = ["Pizza", "Hambúrguer", "Sushi", "Salada", "Churrasco", "Tacos"]
lugares = ["Cinemas", "Restaurantes italianos", "Parques", "Praias", "Shopping", "Museus", "Bares"]
jogos = ["Final Fantasy VII Remake", "Elden Ring", "Uno", "Clue"]
nome_bot = random.choice(["ELLYE", "EMET", "SORA", "WALL"])

def hora_data():
    #Retorna a hora e data atuais no Brasil.
    hora = Dt.datetime.now().strftime("%H:%M:%S")
    data = Dt.datetime.now().strftime("%d/%m/%Y")
    return f"A data e hora atuais no Brasil são: {data} e {hora}."

def sugestao_de_comidas():
    #Sugere uma comida aleatória.
    return f"O que acha de comer {random.choice(comidas)} hoje?"

def sugestao_de_lugares():
    #Sugere um lugar aleatório para visitar.
    return f"Que tal sair para um(a) {random.choice(lugares)} hoje?"

def sugestao_de_jogo():
    #Sugere um jogo aleatório para jogar.
    return f"Por que não jogar {random.choice(jogos)} hoje?"

# Padrões de interação com o chatbot.
patterns = [
    (r'que horas são ?', [hora_data()]),
    (r'oi|olá|bom dia|boa tarde|boa noite', ['Olá! Como posso ajudar você hoje?']),
    (r'como você está ?', ['Estou bem, obrigado! E você?']),
    (r'quem é você ?', [f'Eu sou {nome_bot}, seu assistente virtual.']),
    (r'qual é a sua função ?', ['Minha função é ajudar com informações e responder perguntas.']),
    (r'(.*)(ajuda|preciso de ajuda|me ajude|socorro|emergência)', ['Claro! Como posso te ajudar?']),
    (r'(.*)', ['Desculpe, não entendi. Você pode reformular a pergunta?'])
]

chatbot = Chat(patterns, reflections)

# Função de interação com o usuário.
def speak():
    entrada_usuario = entry.get().strip().lower()
    entry.delete(0, END)
    
    if entrada_usuario == "sair":
        chat_log.insert(END, "ChatBot: Até logo!\n")
        janela.quit()
    else:
        chat_log.insert(END, f"Você: {entrada_usuario}\n")

        if any(palavra in entrada_usuario for palavra in ["comer", "jantar", "almoço"]):
            resposta = sugestao_de_comidas()
        elif any(palavra in entrada_usuario for palavra in ["onde ir", "diversão"]):
            resposta = sugestao_de_lugares()
        elif any(palavra in entrada_usuario for palavra in ["jogo", "jogar", "o que jogar"]):
            resposta = sugestao_de_jogo()
        else:
            resposta = chatbot.respond(entrada_usuario)
        
        chat_log.insert(END, f"ChatBot: {resposta}\n")

# Interface gráfica do chatbot.
janela = Tk()
janela.title("ChatBot")
janela.geometry("600x400")

chat_log = Text(janela, height=20, width=70, wrap=WORD)
chat_log.pack(pady=10)

entry = Entry(janela, width=50)
entry.pack(pady=5)

send_button = Button(janela, text="Enviar", command=speak)
send_button.pack()

# Mensagem inicial do chatbot.
chat_log.insert(END, f"ChatBot: Olá! Me chamo {nome_bot} e estou aqui para ajudar. Digite 'Sair' para encerrar.\n")
chat_log.insert(END, "ChatBot: Posso responder perguntas como: 'Que horas são?', 'Quem é você?', 'Qual é a sua função?'.\n")
chat_log.insert(END, "ChatBot: Para sugestões, tente perguntar 'o que comer', 'onde ir' ou 'o que jogar'.\n")

janela.mainloop()
