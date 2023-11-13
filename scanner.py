import requests
from  bs4 import BeautifulSoup

bad_char = ["'","<",">","(",")",";"]


def  spider_inputs(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    form = soup.find('form')
    
    if not form:
        print("No forms was found")
        return []
    
    return form.find_all('input')

def  test_inputs(url):

def main():
    url = input("Enter url to Scan")
    
    inputs = spider_inputs(url)
    
    if not  inputs 
        return
    
    


if __name__="__main__":
    main()