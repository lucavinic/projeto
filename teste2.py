import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Carregar os dados de treinamento
train_data = [
    ("Olá, como posso ajudar?", "saudacao"),
    ("Eu tenho uma pergunta sobre o produto.", "pergunta"),
    ("Eu quero saber mais sobre a empresa.", "informacao"),
    ("Eu estou tendo um problema com o produto.", "problema"),
    ("Eu quero falar com um agente humano.", "agente"),
]

# Pré-processar os dados de treinamento
lemmatizer = WordNetLemmatizer()
vectorizer = CountVectorizer()

X = []
y = []
for texto, etiqueta in train_data:
    palavras = word_tokenize(texto)
    palavras = [lemmatizer.lemmatize(palavra) for palavra in palavras]
    X.append(" ".join(palavras))
    y.append(etiqueta)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
clf = MultinomialNB()
clf.fit(vectorizer.fit_transform(X_train), y_train)

# Definir a função de chatbot
def chatbot(texto):
    palavras = word_tokenize(texto)
    palavras = [lemmatizer.lemmatize(palavra) for palavra in palavras]
    texto = " ".join(palavras)
    texto_vector = vectorizer.transform([texto])
    etiqueta = clf.predict(texto_vector)
    
    if etiqueta == "saudacao":
        return "Olá! Como posso ajudar?"
    elif etiqueta == "pergunta":
        return "Claro! Qual é a sua pergunta?"
    elif etiqueta == "informacao":
        return "A empresa foi fundada em 2010 e oferece produtos de alta qualidade."
    elif etiqueta == "problema":
        return "Sinto muito que você esteja tendo um problema. Posso ajudar a resolver?"
    elif etiqueta == "agente":
        return "Vou direcionar você para um agente humano. Por favor, aguarde."

# Testar o chatbot
print(chatbot("Olá!"))
print(chatbot("Eu tenho uma pergunta sobre o produto."))
print(chatbot("Eu quero saber mais sobre a empresa."))
print(chatbot("Eu estou tendo um problema com o produto."))
print(chatbot("Eu quero falar com um agente humano."))