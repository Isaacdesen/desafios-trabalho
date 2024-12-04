god_of_war = {
    "KRATOS": {
        "Raça" : "Semideus (filho de zeus e calisto)",
        "Idade" : "5.000 anos apesar de parecer mais jovem devido à sua natureza divina",
        "Altura" : "12 metros",
        "Peso" : "1.200 kg",
        "habilidades" : "Força sobre-humana / Manipulação de Energia Cósmica / Regeneração Divina"
    },
    "ZEUS": {
        "Raça" : "Deus Olímpico (Filho de Cronos e Reia)",    
        "Idade" : "Imortal (com aparência jovem, mas de existência eterna)",
        "Altura" : "Varia (depende das representações, mas frequentemente é mostrado como imponente e de grande porte, mais alto que um ser humano comum)",
        "Peso" : "Não especificado, mas sua estrutura física é massiva e impressionante",
        "habilidades" : "Manipulação de Energia Cósmica / Regeneração Celestial / Imunidade a Ataques Físicos Comuns"
    },
    "HERCULES" : {
        "Nome" : "Hércules (Heracles, na mitologia grega)",
        "Raça" : "Semideus (Filho de Zeus e Alcmena)",
        "Idade" : "Aparentemente jovem, mas com uma vida longa devido à sua natureza semideusa e sua imortalidade adquirida após sua morte",
        "Altura" : "Aproximadamente 2,10 metros (depende da representação, mas ele é geralmente descrito como imenso e musculoso)",
        "Peso" : "Cerca de 200 kg (devido à sua musculatura massiva e força física)",
        "habilidades" : "Força Sobrehumana / Resistência e Durabilidade / Habilidades de Combate"
    },
    "POSEIDON" : {
        "Nome" : "Poseidon",
        "Raça" : "Deus Olímpico (Filho de Cronos e Reia)",
        "Idade" : "Imortal (embora tenha vivido desde os primórdios do mundo grego, ele não envelhece)",
        "Altura" : "Varia (geralmente descrito como de estatura imponente e aparência imensa, maior que qualquer mortal)",
        "Peso" : "Não especificado, mas sua estrutura física é robusta, com um corpo poderoso e atlético.",
        "habilidades" : "Controle sobre os Mares e Oceanos / Poderes Terrestres (Terremotos) / Imortalidade"
    },
    "ATENA" : {
        "Nome" : "atena",
        "Raça" : "Deusa Olímpica (Filha de Zeus e Métis)",
        "Idade" : "Imortal (não envelhece e permanece eterna devido à sua natureza divina)",
        "Altura" : "Varia dependendo da representação, mas geralmente é descrita como uma figura de porte imponente, embora não seja fisicamente tão musculosa quanto algumas outras divindades, ela exala autoridade e poder intelectual.",
        "Peso" : "Não especificado, mas sua constituição física é esbelta e atlética, adequada à sua habilidade em combate e sua natureza estratégica.",
        "habilidades" : "Sabedoria e Inteligência Sobrehumana / Habilidade em Estratégia e Guerra Justa / Imortalidade / Habilidade em Combate"
    },
    "ARES" : {
        "Nome" : "ares",
        "Idade" : "Eterno, imortal.",
        "Raça" : "Deus (Olimpiano)",
        "Peso" : "Peso: Pesado e robusto, refletindo sua força física e estrutura imponente.",
        "Altura e Força" : "Embora os jogos não especifiquem a altura exata de Ares, ele é retratado como um gigante, muito maior que humanos normais, demonstrando uma força descomunal típica dos deuses da guerra.",
        "habilidades" : "Poderes de Guerra / Manipulação de Fogo / Imortalidade / Transformação"
    },
    "AFRODITE" : {
        "Nome": "afrodite",
        "Raça": "Deusa do Amor e da Beleza, Afrodite é uma das divindades do panteão grego.",
        "Idade": "atemporal e eterna",
        "Peso": "Embora o jogo não forneça medidas específicas de força e altura, Afrodite é retratada como uma deusa poderosa, com a capacidade de influenciar emoções e desejos.",
        "habilidades" : "Encantamento/ Influência Emocional / Imortalidade / Magia"
    },
    "APOLO" : {
        "Nome": "apolo",
        "Idade": "Imortal, atemporal.",
        "Raça": "Deus grego, pertencente ao panteão olímpico.",
        "Peso": "O jogo não fornece medidas exatas de força e altura para Apolo. Contudo, como um deus, ele é geralmente considerado extremamente forte e poderoso, capaz de realizar feitos sobrenaturais.",
        "habilidades" : "Controle do Sol / Habilidades Musicais / Imortalidade / Profecia"
    },
    "HELIOS" : {
        "Nome" : "hélios",
        "Idade": "Imortal, atemporal.",
        "Peso" : "Não especificado, mas imenso devido à sua ligação com o sol.",
        "Raça" : "Deus grego (da mitologia grega), pertencente à raça dos deuses do Olimpo.",
        "habilidades" : "Poderes do SolPoderes do Sol / Iluminação e Visão / Imortalidade / Resistência e Imortalidade"
    },
    "HADES" : {
        "Nome" : "hades",
        "Idade": "Imortal, atemporal.",
        "Peso" : "Não especificado, mas de presença densa e imponente devido ao seu domínio sobre o submundo.",
        "Raça" : "Deus grego (da mitologia grega), membro da raça dos deuses do Olimpo.",
        "habilidades" : "Poder sobre os Mortos / Invocar Espíritos e Criar Armadas de Mortos / Imortalidade / Poder de Criar e Manipular Sombras e Escuridão"
}
}

def exibir(nome):
    if nome in god_of_war:
        personagem = god_of_war[nome]
        print(f"Nome: {nome}")
        print(f"Raça: {personagem['Raça']} ")
        print(f"Idade: {personagem['Idade']} ")
        print(f"Peso: {personagem['Peso']} ")
        print(f"Habilidades: {personagem['habilidades']} ")
    else:
        print("deus não enontrado")
def pesquisar_deuses():
    nome_deuses = input("\nProcurar deuses, digite o nome: ").upper()
    exibir(nome_deuses)


def perguntar_continuar():
    resposta = input("\nDeseja continuar a procurar deuses? (sim/não): ").lower()
    if resposta == "sim":
        return True
    elif resposta =="não":
        return False
    else:
        print("reposta invalida!!")
        return perguntar_continuar()
    
def procurar():
    while True:
        pesquisar_deuses()
        continuar = perguntar_continuar()
        if not continuar:
            print("\ndesistiu de procurar!")
            break
procurar()        