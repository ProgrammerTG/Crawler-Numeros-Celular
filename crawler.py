from bs4 import BeautifulSoup
from random import randint
import requests, re

alvov = "https://django-anuncios.solyd.com.br"
listanum = []
contador = 0
def obtertexto(passaporte):
    try:
        return BeautifulSoup(requests.get(f"{passaporte}").text, "html.parser")
    except:
        print("Ocorreu um erro, ejetando...")
        return

def salvar():
    nome = randint(1000, 9000000)
    print(f"Salvando os números em {nome}.csv")
    with open(f"{nome}.csv", "w") as arquivo:
        texto = "numero\n"
        for e in listanum:
            texto += f"{str(e)}\n"
        arquivo.write(texto)
        arquivo.close()
    print("Contatos salvos com sucesso!")


def obternumeros(coisas):
    global contador
    coisas = coisas.find_all("h3", class_="ui dividing header")
    for e in coisas:
        retorno = re.findall("\(?[0-9]{2}\+?\)?.?[0-9]{4,5}.?[0-9]{4}", e.parent.p.get_text())
        if retorno:
            for e in retorno:
                contador += 1
                print(f"Números capturados:{contador}")
                listanum.append(e)
            
if __name__ == "__main__":
    print("#"*20)
    print("Crawler de números")
    print("#"*20)
    alvo = obtertexto(f"{alvov}/automoveis/")
    if alvo:
        todos = alvo.find("div", class_="ui three doubling link cards")
        al = todos.find_all("a")
        for e in al:
            obternumeros(obtertexto(f"{alvov}{e['href']}"))
        if listanum:
            salvar()
        else:
            print("Não há números para salvar!")