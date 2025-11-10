def crypter_message(message, clef):
    """
    Chiffre un message selon la clé fournie.
    """
    message_crypte = ""
    for lettre in message.lower():
        if lettre in clef:
            message_crypte += clef[lettre]
        else:
            message_crypte += lettre  # garde espaces et ponctuation
    return message_crypte

# === À TOI DE JOUER ===
# Écris la fonction suivante :
def decrypter_message(message_crypte, clef):
    """
    Déchiffre un message codé à l’aide de la clé fournie.
    """
    message_decode = ""
    for lettre_chiffree in message_crypte.lower():
        trouve = False
        for key, val in clef.items():
            if val == lettre_chiffree:
                message_decode += key
                trouve = True
                break
        if not trouve:
            # si aucun code ne correspond, on conserve le caractère (espace, ponctuation, etc.)
            message_decode += lettre_chiffree
    return message_decode

# Dictionnaire de cryptage du Club Sandwich (décalage de 10)
clef_espion = {
    'a': 'k', 'b': 'l', 'c': 'm', 'd': 'n', 'e': 'o', 'f': 'p', 'g': 'q',
    'h': 'r', 'i': 's', 'j': 't', 'k': 'u', 'l': 'v', 'm': 'w', 'n': 'x',
    'o': 'y', 'p': 'z', 'q': 'a', 'r': 'b', 's': 'c', 't': 'd', 'u': 'e',
    'v': 'f', 'w': 'g', 'x': 'h', 'y': 'i', 'z': 'j'
}

# Exemple de message intercepté :
message_secret = "ckved mvel ckxngsmr!"
print("Message secret :", message_secret)

# Utilise ta fonction pour décrypter le message secret
message_original = decrypter_message(message_secret, clef_espion)
print("Message décodé :", message_original)

