from colorama import Fore, init
import random
import time

# Initialisation de colorama
init()

# Définition du logo avec le texte "KEY GEN"
banner = (Fore.MAGENTA + """
  ▄████▄   ██▓     ██▓ ███▄    █   ▄████  ▒█████   ███▄    █ 
 ▒██▀ ▀█  ▓██▒    ▓██▒ ██ ▀█   █  ██▒ ▀█▒▒██▒  ██▒ ██ ▀█   █ 
 ▒▓█    ▄ ▒██░    ▒██▒▓██  ▀█ ██▒▒██░▄▄▄░▒██░  ██▒▓██  ▀█ ██▒
 ▒▓▓▄ ▄██▒▒██░    ░██░▓██▒  ▐▌██▒░▓█  ██▓▒██   ██░▓██▒  ▐▌██▒
 ▒ ▓███▀ ░░██████▒░██░▒██░   ▓██░░▒▓███▀▒░ ████▓▒░▒██░   ▓██░
 ░ ░▒ ▒  ░░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
   ░  ▒   ░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░  ░   ░   ░ ▒ ▒░ ░ ░░   ░ ▒░
 ░          ░ ░    ▒ ░   ░   ░ ░ ░ ░   ░ ░ ░ ░ ▒     ░   ░ ░ 
 ░ ░          ░  ░ ░           ░       ░     ░ ░           ░ 
 ░                                                          
""" + Fore.RESET)

def generate_license_key(segments=5, segment_length=5, separator="-"):
    """
    Génère une clé de licence aléatoire avec des segments et une longueur spécifiés.
    """
    allowed_characters = 'RTYPQDFGHJKMWXCVBN23456789'  # Lettres et chiffres autorisés pour la clé
    key_segments = [''.join(random.choices(allowed_characters, k=segment_length))
                    for _ in range(segments)]
    return separator.join(key_segments)

def generate_infinite_license_keys(segments=5, segment_length=5, separator="-", delay=1):
    """
    Génère et affiche une clé de licence aléatoire à l'infini avec un délai entre chaque génération.
    """
    try:
        print(banner)  # Affichage du logo
        while True:
            print(Fore.GREEN + "[+]" + Fore.RESET + " " + generate_license_key(segments, segment_length, separator))
            time.sleep(delay)  # Ajoute un délai entre chaque génération pour rendre la sortie gérable
    except KeyboardInterrupt:
        print("\nGénération de clés de licence arrêtée par l'utilisateur.")

# Exemple d'utilisation pour générer et afficher des clés de licence à l'infini
if __name__ == "__main__":
    generate_infinite_license_keys()
