def main():
    coluna(pegar_numero())

def coluna(colunas):
    print("🧱\n" * colunas, end="")



def pegar_numero():
    while True:
        coluna = int(input("quantas colunas você quer?"))
        if coluna > 0:
            return coluna

main()