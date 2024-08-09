
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
from nltk.chat.util import Chat, reflections

# Defina pares de padrões e respostas
pares = [
    [
        r"meu nome é (.*)",
        ["Olá %1, é um prazer conhecer você!",]
    ],
    [
        r"qual é o seu nome?",
        ["Eu sou um chatbot, não tenho um nome.",]
    ],
    [
        r"como você está?",
        ["Eu sou apenas um programa, então não tenho sentimentos, mas estou aqui para ajudá-lo!",]
    ],
    [
        r"sair",
        ["Tchau!", "Até mais tarde.",]
    ]
]

def main():
    print("Olá! Eu sou um chatbot. Digite algo para iniciar uma conversa.")
    print("Para sair, digite 'sair'")
    
    # Crie um objeto Chat com os pares de padrões e respostas
    chat = Chat(pares, reflections)
    chat.converse()

if __name__ == "__main__":
    main()



