import hashlib
import json

def sauvegarder_mots_passes(dict_mots_passes):
    with open("mots_passes.csv", "w") as f:
        for mot, value in dict_mots_passes.items():
            f.write(mot + ", " + ", ".join(value) + "\n")


def hasher_mots(mots: list[str]) -> dict:
    """
    Fonction qui reçoit une liste de mots et qui génère les hash md5, sha256 et sha512 de chaque mot à
    l'aide du module hashlib.
    La fonction génère ainsi un dictionnaire dont les clés sont les mots et les valeurs sont
    une liste des 3 hash calculés auparavant.
    :param mots: La liste des mots à hasher
    :return: Le dictionnaire généré contenant les hash de chaque mot
    """
    hash_dict = {}

    # TODO: Complétez cette fonction pour qu'elle génère un dictionnaire contenant les 3 hash demandés (md5, sha256, sha512)
    #   pour chacun des mots dans la liste des mots non chiffrés fournie dans le programme principal.
    # pseudocode
    # créer dictionnaire
    # boucle pour les mots
        # hasher les mots
        # les mettre dans le dictionnaire avec le mot comme clé et une liste de hash comme valeur

    for mot in mots:
        # Référence : Notes de cours
        # https://projets420.gitbook.io/notes-de-cours/cryptographie/introduction-a-la-cryptographie
        mot_en_bytes = mot.encode()  # Encodage en bytes (par défaut UTF-8)
        hash_md5 = hashlib.md5(mot_en_bytes).hexdigest()

        # Référence : documentation module hashlib
        # https://docs.python.org/3/library/hashlib.html#usage
        hash_sha256 = hashlib.sha256(mot_en_bytes).hexdigest()
        hash_sha512 = hashlib.sha512(mot_en_bytes).hexdigest()

        hash_dict[mot] = [hash_md5, hash_sha256, hash_sha512]

    return hash_dict


def chiffrement_cesar(chaine: str, nb_cesar: int) -> str:
    """
    Cette fonction reçoit un mot ainsi que le nombre de rotation pour chiffrer le mot. Elle en fait le chiffrement
    de césar en utilisant le nombre reçu pour transformer le mot.
    :param chaine: Le mot ou chaîne de caractères à chiffrer
    :param nb_cesar: Le nombre de rotations à faire pour le chiffrement.
    :return: La chaine chiffrée résultante
    """
    caracteres_remplacement = "abcdefghijklmnopqrstuvwxyz"
    chaine_chiffree = ""

    # TODO: à l'aide des caractères de remplacement, du nombre de César et de la chaine originale, faire le chiffrement
    #   de césar et retournez la chaîne ainsi générée

    # pseudocode
    # pour chaque caractère dans chaine
    for i in range(len(chaine)):
        # position = trouver caractère dans caracteres_remplacement
        position = caracteres_remplacement.index(chaine[i])
        position += nb_cesar
        position = position % len(caracteres_remplacement)
        chaine_chiffree += caracteres_remplacement[position]

    return chaine_chiffree

def sauvegarder(dict_mots_passes: dict) -> None:
    """
    Fonction pour sauvegarder un dictionnaire de mots de passes avec ses hash
    :param dict_mots_passes: dictionnaire contenant les mots de passes et leur listes de hash
    """
    with open("mots_passes.json", "w", encoding="utf-8") as f:
        json.dump(dict_mots_passes, f, ensure_ascii=False)

if __name__ == '__main__':

    mots_aleatoires = [
        "arbre", "bateau", "chat", "drapeau", "elephant", "fleur", "glace", "horizon", "iguane", "jonquille",
        "kangourou", "lumiere", "montagne", "nuage", "porte", "quiche", "requin", "soleil", "tigre",
        "univers", "vague", "wagon", "xylophone", "yeti", "zebre", "abeille", "ballon", "canard", "dejeuner",
        "etoile", "fromage", "girafe", "horloge", "internet", "joie", "karaoke", "livre", "magie", "neige",
        "orange", "parapluie", "quartz", "riz", "sable", "telephone", "uniforme", "velo", "weekend", "xylocope",
        "yaourt", "zeste", "amour", "banane", "cerise", "dent", "enfant", "fete", "guitare", "herisson",
        "idee", "jardin", "koala", "lune", "maison", "nature", "oiseau", "pomme", "quai", "riviere",
        "serpent", "tomate", "ulysse", "vent", "whisky", "xenon", "yeux", "zen", "avion", "boulangerie",
        "cerf", "dromadaire", "epinard", "fusil", "grange", "hameau", "ilot", "jongleur", "kilogramme",
        "lavoir", "muguet", "navire", "ours", "pierre", "quatre", "renard", "scie", "trousseau", "universite"
    ]

    mots_cesar = [
        "ozsxkbn",
        "thecqtqyhu",
        "diozmizo"
    ]

    mots_hash = [
        'dc0add0b9d59afd7f5d38ee814f85c37',
        '3378673b4755b9c5d291a295aade6ed10ab531e77cdb96b92e531e3b4be1aa260e34507681117cd8212341e2a37d31540af25302584bb489b5614f805883e2ff',
        'ceac214f32b3bc28669d0e09487d82a171fbc38f7b48140e50279e7774c079ae',
        'ef0738953fcb9fbfedc6795a7c5e8a7d5894d3534adc346e0f9f1bf0a3017f87a21ef14bac9340b7d1fcdc9579906ae1bde0bd514b9b8c1e2e091d1314abf528'
    ]

    mots_cesar_hash = [
        '95b7aa774ee5d86302c89ef3bc6e3fcd',
        '059f79fbb20a17eb6c7dc12883fb6105eca60071034ac32ae201a57762020e07'
    ]

    # tester que hasher 2 fois la même chose donne le même résultat
    dict1 = hasher_mots(mots_aleatoires)
    sauvegarder_mots_passes(dict1)
    dict2 = hasher_mots(mots_aleatoires)
    sauvegarder(dict2)

    if dict1 == dict2:
        print("C'est pareil")
    else:
        print("C'est pas pareil")

    # TODO : Tout décrypter le contenu des 3 listes : mots_cesar, mots_hash et mots_cesar_hash
    # Indice : les mots à trouver devrait exister dans la liste mots_aleatoires
    print()
    # Déchiffrer les mots césar
    for mot_chiffre in mots_cesar:
        for i in range(26):
            mot_dechiffre = chiffrement_cesar(mot_chiffre, i)
            if mot_dechiffre in mots_aleatoires:
                print(mot_dechiffre)
                break # termine le for in in range(26), passe au mot suivant
    print()
    # Retrouver les mots hachés
    for hash in mots_hash:
        for mot, liste_hash in dict1.items():
            if hash in liste_hash:
                print(mot)
                break
    print()
    # Retrouver les mots hachés et crytpés
    # Pseudocode
    # Trouver tous les mots chiffrés possibles
    mots_chiffres = []
    for mot in mots_aleatoires:
        for i in range(26):
            mot_chiffre = chiffrement_cesar(mot, i)
            mots_chiffres.append(mot_chiffre)
    # hasher tous les mots chiffrés
    dict3 = hasher_mots(mots_chiffres)
    # pour chaque élément dans la liste de mots_cesar_hahs
        # vérifier si l'élément existe dans le dictionnaire
            # le mot est trouvé mais il faut le déchiffrer
    for code in mots_cesar_hash:
        for mot_chiffre, liste_hash in dict3.items():
            if code in liste_hash:
                for i in range(26):
                    mot_dechiffre = chiffrement_cesar(mot_chiffre, i)
                    if mot_dechiffre in mots_aleatoires:
                        print(mot_dechiffre)
                        break  # termine le for in in range(26), passe au mot suivant



