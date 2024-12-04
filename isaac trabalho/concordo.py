def main():
    resposta = input ("você concorda? ").lower()
    concordo(resposta)

def concordo(resposta):
    if resposta == "sim" or resposta == "s" or resposta == "si" or resposta == "yes":
        print("Eu concordo")
    elif resposta == "n" or resposta == "não" or resposta == "n":
     print("Eu não concordo")
main()