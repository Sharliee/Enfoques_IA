import nltk
nltk.download('punkt')
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Preprocesamiento de texto
corpus = 

# Toma el texto de entrada y con la funcion sent_tokenize lo convierte a oraciones
sentences = nltk.sent_tokenize(corpus)
# Toma las oraciones guardadas en sentences y las guarda en una lista de palabras ademas de convertirlas a minusculas
word_list = [nltk.word_tokenize(sent.lower()) for sent in sentences]
# Filtra todas las palabras que no sean alfanumericas
word_list_clean = [[word for word in sent if word.isalnum()] for sent in word_list]

# Se crea un objeto y utiliza la técnica de ponderación tf-idf, que asigna un peso a cada palabra en función
# de la frecuencia de aparición en el texto y de la frecuencia de aparición en el conjunto de documentos.
vectorizer = TfidfVectorizer()

# Vectoriza las oraciones volviendo a juntar las palabras pero ahora agregandole peso a cada palabra
X = vectorizer.fit_transform([' '.join(sent) for sent in word_list_clean])

# Hacer una pregunta
query = input("¿Qué te gustaría saber sobre los chatbots? ")

#Convierte la entrada a letras minusculas y de igual manera que las funciones anteriores vectoriza las palabras para agregarles peso
query_vec = vectorizer.transform([query.lower()])

#A partir de la matriz donde se guardo cada palabra de la oracion y sus pesos calcula el vector con el coseno como el vector de entrada sobre los datos almacenados en x
# Como resultado entrega un nuevo vector con los puntajes de similitud
similarity_scores = cosine_similarity(X, query_vec).flatten()

# Obtener respuesta
# Busca el índice en la lista similarity_scores el valor máximo de similitud con la pregunta que se hizo
best_score_index = similarity_scores.argmax()
# Se asigna a la variable answers la respuesta correspondiente con mayor puntaje
answer = sentences[best_score_index]

print("\n\nPregunta: ", query)
print("\nRespuesta: ", answer)
