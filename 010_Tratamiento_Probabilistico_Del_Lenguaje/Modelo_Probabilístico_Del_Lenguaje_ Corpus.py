import nltk
from nltk.corpus import brown

#Natural Language Tool Kit(nltk) como lo dice en su nombre sirve para trabajar con datos que se usa en el lenguaje humano

nltk.download('brown')
corpus = brown.sents(categories='news')

from nltk.util import ngrams
from nltk.probability import FreqDist

n = 2 # número de palabras en cada secuencia
ngram_freq = FreqDist(ngrams([word.lower() for sent in corpus for word in sent], n))

def probability_of_sequence(sequence):
    seq_freq = ngram_freq[tuple(sequence)]
    total_freq = sum(ngram_freq.values())
    return seq_freq / total_freq
#Aqui se busca la probabilidad en que dos palabras aparezcan en Brown, nosotros podemos escoger las palabras que queremos que nos encuentre la probabilidad

print(probability_of_sequence(['the', 'people']))
#Imprime las posibilidades de que estas dos palabras esten juntas
