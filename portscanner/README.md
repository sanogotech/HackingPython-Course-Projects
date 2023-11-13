
## Voici le code complet du script portscanner.py :

```python
import socket

def main():
    # Demander à l'utilisateur l'adresse IP ou le nom de domaine à scanner
    host = input("Adresse IP ou nom de domaine à scanner : ")

    # Créer un socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Scanner les ports de 1 à 65535
    for port in range(1, 65535):
        # Essayer de se connecter au port
        try:
            s.connect((host, port))
        except socket.error:
            # Le port est fermé
            pass
        else:
            # Le port est ouvert
            print("Port {} ouvert".format(port))

    s.close()

if __name__ == "__main__":
    main()
```

Utilisez le code avec précaution. En savoir plus
Ce script fonctionne de la manière suivante :

Il demande à l'utilisateur l'adresse IP ou le nom de domaine à scanner.
Il crée un socket TCP.
Il scanne les ports de 1 à 65535.
Pour chaque port, il essaie de se connecter au port.
Si la connexion est réussie, le port est ouvert.
Le script affiche la liste des ports ouverts.

Voici un exemple d'exécution du script :
```
Adresse IP ou nom de domaine à scanner : 192.168.1.1
Port 22 ouvert
Port 80 ouvert
Port 443 ouvert
```

Ce script peut être amélioré de plusieurs manières, par exemple :

Il peut être rendu plus rapide en utilisant des threads ou des processus.
Il peut être rendu plus précis en utilisant des techniques de scan plus sophistiquées, comme le scan SYN ou le scan UDP.
Il peut être rendu plus versatile en permettant à l'utilisateur de spécifier les ports à scanner.
