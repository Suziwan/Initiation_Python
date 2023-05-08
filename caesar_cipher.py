# créer une fonction caesar_cipher qui prend en paramètres un string et une clé de chiffrement 
# (nombre de lettres à décaler) pour en sortir le string modifié.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(message, key):
    message = message.lower()
    encrypted_message = ''
    for letter in message:
        if letter not in alphabet:
            encrypted_message += letter
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + key
            encrypted_message += alphabet[new_position]
    print(encrypted_message)
    
caesar_cipher('What a string!', 5)