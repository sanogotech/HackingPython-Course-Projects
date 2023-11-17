
import zapapi

def main():
    # Demander à l'utilisateur l'adresse URL du site Web à scanner
    url = input("Adresse URL du site Web à scanner : ")

    # Se connecter à OWASP ZAP
    zap = zapapi.Zap()
    zap.open()

    # Lancer un scan ZAP
    scan = zap.spider.scan(url)
    scan.wait()

    # Analyser la réponse HTTP pour détecter les vulnérabilités
    vulnerabilities = scan.get_results()
    for vulnerability in vulnerabilities:
        print("Le site Web {} est vulnérable à {}".format(url, vulnerability.name))

if __name__ == "__main__":
    main()
