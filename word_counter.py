# Écris une fonction intitulée word_counter qui prend en paramètres 2 éléments :
# - le corpus, string dans lequel tu devras checker le nombre d'occurrences de différents strings
# - la référence, une liste de mots (strings) qui seront recherchés dans le corpus 
# La fonction devra renvoyer le nombre d'occurrences de chaque mot de la référence dans le corpus sous la forme 
# d'un dictionnaire. 

def word_counter(corpus, word_list):
    dictionary = {}
    occurrence = 0
    for word in word_list:
        if corpus.lower().find(word) >= 0:
            occurrence = 1
            dictionary[word] = occurrence
    print(dictionary)
    
reference = ["below", "down", "go", "going", "horn", "how", "howdy", "it", "i", "low", "own", "part", "partner", "sit"]

word_counter("below", reference)
# => {"below" : 1, "low" : 1}

word_counter("Howdy partner, sit down! How's it going?", reference)
# => {"down" : 1, "go" : 1, "going" : 1, "how" : 2, "howdy" : 1, "it" : 2, "i" : 3, "own" : 1, "part" : 1, 
# "partner" : 1, "sit" : 1}