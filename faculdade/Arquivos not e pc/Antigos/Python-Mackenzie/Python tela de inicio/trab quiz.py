lista1= ['1','2','3','4','5']
def msg():
    print("Bem vindo ao quiz sobre Fake News ")
    print("Você responderá algumas perguntas sobre fake news e se acertar a questão ganhará alguns pontos" )


def quest1():
    print("  Questao 1: Para evitar noticiais falsas, voce deve:")
    print("   1- Não conferir o endereço URL")
    print("   2- Pesquisar em outros sites de noticias ")
    print("   3- Confiar em grupos de WhatsApp da família")
    print("   4- Não saber quem escreveu o texto")
    print("   5- Não ver a notícia somente pelo título")
    soma = 0
    for i in lista1:
        alter1 = int(input("    Alternativa escolhida: "))
        if alter1 == 1:
            print("  Errada!")
            print("Explicação:")
            print("  O endereço URL é uma das coisas que devem ser chegadas para ver se o site é confiável")
            print("Outras questoes:")
            print("  (Alternativa2)- Correta!!!É algo mais certo a se fazer, pois pesquisando em outros sites é possível ver se é verdade ou não ")
            print("  (Alternativa3)- Errado!!Grupo da familia tem muitas circulações de noticias e uma delas podem ser falsas")
            print("  (Alternatica4) -Errado!!Para saber se o texto é verdade, deve ser pesquisado o nome do autor para ver se o mesmo escreve noticias reais")
            print("  (Alternativa5)- Errado!!As vezes o título pode te enganar falando de uma coisa porem a notícia não tem nada a ver com o assunto")
            print("*************************************************************************************")
            break
        
        elif alter1 ==2:
            print("  Correta!!")
            print("Explicação:")
            print("  É algo mais certo a se fazer, pois pesquisando em outros sites é possível ver se é verdade ou não ")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!O endereço URL é uma das coisas que devem ser chegadas para ver se o site é confiável")
            print("  (Alternativa3)- Errado!!Grupo da familia tem muitas circulações de noticias e uma delas podem ser falsas")
            print("  (Alternatica4) -Errado!!Para saber se o texto é verdade, deve ser pesquisado o nome do autor para ver se o mesmo escreve noticias reais")
            print("  (Alternativa5)- Errado!!As vezes o título pode te enganar falando de uma coisa porem a notícia não tem nada a ver com o assunto")
            soma +=200
            print("*************************************************************************************")
            break
            
        elif alter1 ==3:
            print("  Errado!!")
            print("Explicação:")
            print("  Grupo da familia tem muitas circulações de noticias e uma delas podem ser falsas")
            print("Outras questoes:")
            print("  (Alternativa1)- Errada!!O endereço URL é uma das coisas que devem ser chegadas para ver se o site é confiável")
            print("  (Alternativa2)- Correta!!É algo mais certo a se fazer, pois pesquisando em outros sites é possível ver se é verdade ou não ")
            print("  (Alternatica4)- Errado!!Para saber se o texto é verdade, deve ser pesquisado o nome do autor para ver se o mesmo escreve noticias reais")
            print("  (Alternativa5)- Errado!!As vezes o título pode te enganar falando de uma coisa porem a notícia não tem nada a ver com o assunto")
            print("*************************************************************************************")
            break
        
            
            
        elif alter1 ==4:
            print("  Errado!!")
            print("Explicação:")
            print("  Para saber se o texto é verdade, deve ser pesquisado o nome do autor para ver se o mesmo escreve noticias reais")
            print("Outras questoes:")
            print("  (Alternativa1)- Errada!!O endereço URL é uma das coisas que devem ser chegadas para ver se o site é confiável")
            print("  (Alternativa2)- Correta!!É algo mais certo a se fazer, pois pesquisando em outros sites é possível ver se é verdade ou não ")
            print("  (Alternativa3)- Errado!!Grupo da familia tem muitas circulações de noticias e uma delas podem ser falsas")
            print("  (Alternativa5)- Errado!!As vezes o título pode te enganar falando de uma coisa porem a notícia não tem nada a ver com o assunto")
            print("*************************************************************************************")
            break

            
        elif alter1 ==5:
            print("  Errado!!")
            print("Explicação:")
            print("  As vezes o título pode te enganar falando de uma coisa porem a notícia não tem nada a ver com o assunto")
            print("Outras questoes:")
            print("  (Alternativa1)- Errada!!O endereço URL é uma das coisas que devem ser chegadas para ver se o site é confiável")
            print("  (Alternativa2)- Correta!!É algo mais certo a se fazer, pois pesquisando em outros sites é possível ver se é verdade ou não ")
            print("  (Alternativa3)- Errado!!Grupo da familia tem muitas circulações de noticias e uma delas podem ser falsas")
            print("  (Alternatica4)- Errado!!Para saber se o texto é verdade, deve ser pesquisado o nome do autor para ver se o mesmo escreve noticias reais")
            print("*************************************************************************************")
            break  
        else:
            if alter1<=0 or alter1>=6:
                alter1 = input("Valor invalido, digite novamente: ")


    #questao 2

    print("  Questao 2: Oque você deve fazer se recebe uma notícia no seu celular, mas não tem certeza?")
    print("   1- Enchaminhar para outros sem pesquisar")
    print("   2- Acreditar na pessoa por ser alguém próximo")
    print("   3- Não pergunta para a pessoa sobre a noticia")
    print("   4- Ver se a noticia é verdade")
    print("   5- Você defende o que leu por um curto período de tempo")
    for i in lista1: 
        alter1 = int(input("    Alternativa escolhida: "))
        if alter1 == 1:
            print("  Errada!!")
            print("Explicação:")
            print("  Seria algo precipitado onde você deveria ler para ter certeza dela")
            print("Outras questoes:")
            print("  (Alternativa2)- Errado!!Não faça isso pois elas podem te enviar notícias falsas")
            print("  (Alternativa3)- Errado!!Perguntando para a pessoa, você teria ideia de que tipo de notícia seria ")
            print("  (Alternatica4)- Correta!!Está verificando a notícia antes de compartilhar")
            print("  (Alternativa5)- Errado!!Você defendendo a notícia sem ler, poderá trazer alguns problemas para você")
            print("*************************************************************************************")
            break

        
        elif alter1 ==2:
            print("  Errada!!")
            print("Explicação:")
            print("  Não faça isso pois elas podem te enviar notícias falsas")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!Seria algo precipitado onde você deveria ler para ter certeza dela")
            print("  (Alternativa3)- Errado!!Perguntando para a pessoa, você teria ideia de que tipo de notícia seria ")
            print("  (Alternatica4)- Correta!!Está verificando a notícia antes de compartilhar")
            print("  (Alternativa5)- Errado!!Você defendendo a notícia sem ler, poderá trazer alguns problemas para você")
            soma +=200
            print("*************************************************************************************")
            break


        elif alter1 ==3:
            print("  Errado!!")
            print("Explicação:")
            print("  Perguntando para a pessoa, você teria ideia de que tipo de notícia seria ")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!Seria algo precipitado onde você deveria ler para ter certeza dela")
            print("  (Alternativa2)- Errada!!Não faça isso pois elas podem te enviar notícias falsas")
            print("  (Alternatica4)- Correta!!Está verificando a notícia antes de compartilhar")
            print("  (Alternativa5)- Errado!!Você defendendo a notícia sem ler, poderá trazer alguns problemas para você")
            print("*************************************************************************************")
            break


        elif alter1 ==4:
            print("  Correta!!")
            print("Explicação:")
            print("  Está verificando a notícia antes de compartilhar")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!Seria algo precipitado onde você deveria ler para ter certeza dela")
            print("  (Alternativa2)- Errada!!Não faça isso pois elas podem te enviar notícias falsas")
            print("  (Alternativa3)- Errado!!Perguntando para a pessoa, você teria ideia de que tipo de notícia seria")
            print("  (Alternativa5)- Errado!!Você defendendo a notícia sem ler, poderá trazer alguns problemas para você")
            soma +=200
            print("*************************************************************************************")
            break


        elif alter1 ==5:
            print("  Errado!!")
            print("Explicação:")
            print("  Você defendendo a notícia sem ler, poderá trazer alguns problemas para você")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!Seria algo precipitado onde você deveria ler para ter certeza dela")
            print("  (Alternativa2)- Errada!!Não faça isso pois elas podem te enviar notícias falsas")
            print("  (Alternativa3)- Errado!!Perguntando para a pessoa, você teria ideia de que tipo de notícia seria")
            print("  (Alternatica4)- Correta!!Está verificando a notícia antes de compartilhar")
            print("*************************************************************************************")
            break
        else:
            if alter1<=0 or alter1>=6:
                alter1 = input("Valor invalido, digite novamente: ")
    
    #questao 3

    print("  Questao 3: Nas eleições de Donald Trump, no Brexit do Reino Unido e nas pronunciações públicas do presidente brasileiro;")
    print("é comum encontrar notícias, que de uma certa medida, foram modificadas para atender um propósito contra o bem-estar social,")
    print("privilegiando iniciativas individualizadas. Acerca desse conhecimento, pode-se afirmar que Fake News, impactam na(o):")
    print("   1- Não influenciam a forma com pensam sobre o determinado assunto")
    print("   2- Das pessoas que leram, 100% acreditou nela")
    print("   3- Serve para estudos científicos")
    print("   4- São disseminadas principalmente em um específico assunto")
    print("   5- Manipulam certos discursos e sustentam uma certa ideologia")
    for i in lista1: 
        alter1 = int(input("    Alternativa escolhida: "))
        if alter1 == 1:
            print("  Errada!!")
            print("Explicação:")
            print("  Elas influenciam sim, pois algumas pessoas sempre acreditam que o que está na internet está correto")
            print("Outras questoes:")
            print("  (Alternativa2)- Errada!!Muitas pessoas à leram  e foram atrás de fontes para ver se estava ou não correta")
            print("  (Alternativa3)- Errado!!Não servem como estudo, pois são notícias falsas e estudos científicos são notícias reais")
            print("  (Alternatica4)- Errada!!Está errado, pois ela dissemina em várias outras áreas como ciência, política, economia...")
            print("  (Alternativa5)- Correto!!Manipulam as ideias das pessoas e fazem com que possam mudar de lado por algo que realmente não aconteceu")
            print("*************************************************************************************")
            break

        
        elif alter1 ==2:
            print("  Errada!!")
            print("Explicação:")
            print("  Muitas pessoas à leram  e foram atrás de fontes para ver se estava ou não correta")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!Elas influenciam sim, pois algumas pessoas sempre acreditam que o que está na internet está correto")
            print("  (Alternativa3)- Errado!!Não servem como estudo, pois são notícias falsas e estudos científicos são notícias reais")
            print("  (Alternatica4)- Errado!!Está errado, pois ela dissemina em várias outras áreas como ciência, política, economia...")
            print("  (Alternativa5)- Correto!!Manipulam as ideias das pessoas e fazem com que possam mudar de lado por algo que realmente não aconteceu")
            print("*************************************************************************************")
            break


        elif alter1 ==3:
            print("  Errado!!")
            print("Explicação:")
            print("  Não servem como estudo, pois são notícias falsas e estudos científicos são notícias reais")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!Elas influenciam sim, pois algumas pessoas sempre acreditam que o que está na internet está correto")
            print("  (Alternativa2)- Errada!!Muitas pessoas à leram  e foram atrás de fontes para ver se estava ou não correta")
            print("  (Alternatica4)- Errada!!Está errado, pois ela dissemina em várias outras áreas como ciência, política, economia...")
            print("  (Alternativa5)- Correto!!Manipulam as ideias das pessoas e fazem com que possam mudar de lado por algo que realmente não aconteceu")
            print("*************************************************************************************")
            break


        elif alter1 ==4:
            print("  Errada!!")
            print("Explicação:")
            print("  Está errado, pois ela dissemina em várias outras áreas como ciência, política, economia...")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!Elas influenciam sim, pois algumas pessoas sempre acreditam que o que está na internet está correto")
            print("  (Alternativa2)- Errada!!Muitas pessoas à leram  e foram atrás de fontes para ver se estava ou não correta")
            print("  (Alternativa3)- Errado!!Não servem como estudo, pois são notícias falsas e estudos científicos são notícias reais")
            print("  (Alternativa5)- Correto!!Manipulam as ideias das pessoas e fazem com que possam mudar de lado por algo que realmente não aconteceu")
            print("*************************************************************************************")
            break


        elif alter1 ==5:
            print("  Correta!!")
            print("Explicação:")
            print("  Manipulam as ideias das pessoas e fazem com que possam mudar de lado por algo que realmente não aconteceu")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!Elas influenciam sim, pois algumas pessoas sempre acreditam que o que está na internet está correto")
            print("  (Alternativa2)- Errada!!Muitas pessoas à leram  e foram atrás de fontes para ver se estava ou não correta")
            print("  (Alternativa3)- Errado!!Não servem como estudo, pois são notícias falsas e estudos científicos são notícias reais")
            print("  (Alternatica4)- Errada!!Está errado, pois ela dissemina em várias outras áreas como ciência, política, economia...")
            soma += 800
            print("*************************************************************************************")
            break
        else:
            if alter1<=0 or alter1>=6:
                alter1 = input("Valor invalido, digite novamente: ")


            #questao 4    
    print("  Questao 4: No período da Alemanha nazista, os associados e apoiadores desse governo nazifascista era responsável pela disseminação de opiniões e notícias caluniosas, que alteravam e manipulavam os pensamentos do público receptor, alienando-os da realidade. Na contemporaneidade, pode-se perceber que a utilização da pós-verdade em discursos por partidos e figuras públicas permanecerem presentes nas relações sociais. Veja quais impactos que as Fake News podem exercer sobre a população e escolha a verdadeira: o bem-estar social,")
    print("   1- Fazer com que o presidente sempre seja o vilão da historia")
    print("   2- Não resgatam o orgulho nacional")
    print("   3- Fazem com que mudem de lado politico")
    print("   4- Paixão ao partido oposto ")
    print("   5- Para revelar roubos ou alguns crimes do próprio partido")
    for i in lista1: 
        alter1 = int(input("    Alternativa escolhida: "))
        if alter1 == 1:
            print("  Errada!!")
            print("Explicação:")
            print("  Se estão fazendo alguma Fake News ‘e porque querem que o personagem sempre seja o herói")
            print("Outras questoes:")
            print("  (Alternativa2)- Errado!! A maioria das Fake News são para tentar retomar o orgulho nacional fazendo com que retomem o passado")
            print("  (Alternativa3)- Correto!! Essas notícias tem a intenção de mudar a pessoa de lado para ter mais apoio populacional")
            print("  (Alternatica4)- Errado!! Sempre fazem notícias contra o partido oposto para terem menos apoio")
            print("  (Alternativa5)- Errado!! Tentam encobertar as falas ou atitudes ruins para se darem bem")
            print("*************************************************************************************")
            break

        elif alter1 ==2:
            print("  Errada!!")
            print("Explicação:")
            print("   A maioria das Fake News são para tentar retomar o orgulho nacional fazendo com que retomem o passado")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!! Se estão fazendo alguma Fake News ‘e porque querem que o personagem sempre seja o herói")
            print("  (Alternativa3)- Correto!! Essas notícias tem a intenção de mudar a pessoa de lado para ter mais apoio populacional")
            print("  (Alternatica4)- Errado!! Sempre fazem notícias contra o partido oposto para terem menos apoio")
            print("  (Alternativa5)- Errado!! Tentam encobertar as falas ou atitudes ruins para se darem bem")
            print("*************************************************************************************")
            break


        elif alter1 ==3:
            print("  Correta!!")
            print("Explicação:")
            print("  Essas notícias tem a intenção de mudar a pessoa de lado para ter mais apoio populacional")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!! Se estão fazendo alguma Fake News ‘e porque querem que o personagem sempre seja o herói")
            print("  (Alternativa2)- Errado!! A maioria das Fake News são para tentar retomar o orgulho nacional fazendo com que retomem o passado")
            print("  (Alternatica4)- Errado!! Sempre fazem notícias contra o partido oposto para terem menos apoio")
            print("  (Alternativa5)- Errado!! Tentam encobertar as falas ou atitudes ruins para se darem bem")
            print("*************************************************************************************")
            soma += 1000
            break


        elif alter1 ==4:
            print("  Errado!!")
            print("Explicação:")
            print("  Sempre fazem notícias contra o partido oposto para terem menos apoio")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!! Se estão fazendo alguma Fake News ‘e porque querem que o personagem sempre seja o herói")
            print("  (Alternativa2)- Errado!! A maioria das Fake News são para tentar retomar o orgulho nacional fazendo com que retomem o passado")
            print("  (Alternatica3)- Correto!! Essas notícias tem a intenção de mudar a pessoa de lado para ter mais apoio populacional")
            print("  (Alternativa5)- Errado!! Tentam encobertar as falas ou atitudes ruins para se darem bem")
            print("*************************************************************************************")
            break


        elif alter1 ==5:
            print("  Errado!!")
            print("Explicação:")
            print("  Tentam encobertar as falas ou atitudes ruins para se darem bem")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!! Se estão fazendo alguma Fake News ‘e porque querem que o personagem sempre seja o herói")
            print("  (Alternativa2)- Errado!! A maioria das Fake News são para tentar retomar o orgulho nacional fazendo com que retomem o passado")
            print("  (Alternatica3)- Correto!! Essas notícias tem a intenção de mudar a pessoa de lado para ter mais apoio populacional")
            print("  (Alternativa4)- Errado!! Sempre fazem notícias contra o partido oposto para terem menos apoio")
            print("*************************************************************************************")
            break
        else:
            if alter1<=0 or alter1>=6:
                alter1 = input("Valor invalido, digite novamente: ")


            #questao 5
                
    print("  Questao 5: Os Coronavírus existem há muitos anos, mas uma nova mutação com alto poder de infecção (COVID-19) surgiu no final de 2019, causando pânico por todo o mundo. E é claro que logo se tornou alvo de inúmeras fake news por aí. Será que você foi influenciado por alguma delas?")
    print("  Selecione qual a opção que NÃO é uma forma de contaminação do Coronavírus:")
    print("   1- Sopa de Morcego")
    print("   2- Contado co superficies contaminadas")
    print("   3- Aperto de mão com pessoas infectadas")
    print("   4- Tosse")
    print("   5- Espirro")
    for i in lista1: 
        alter1 = int(input("    Alternativa escolhida: "))
        if alter1 == 1:
            print("  Correto!!")
            print("Explicação:")
            print("  A sopa de morcego é algo que se come porem não consegue espalhar a doença")
            print("Outras questoes:")
            print("  (Alternativa2)- Errado!!O vírus pode ser obtido por passar a mão em alguma superfície contamina e depois passar nos olhos ou boca, sendo uma forma de contaminação")
            print("  (Alternativa3)- Errado!!Ao entrar em contato com alguém contam ido, suas chances de obter o vírus são altas ")
            print("  (Alternatica4)- Errado!!A tosse é aonde o vírus sai e vai para o ar, quando a pessoa respira, essa pessoa fica contaminada")
            print("  (Alternativa5)- Errado!!Assim como a tosse, o espiro também solta os vírus no ar e ao respirar a pessoa fica contamina")
            soma +=200
            print("*************************************************************************************")
            break

        
        elif alter1 ==2:
            print("  Errada!!")
            print("Explicação:")
            print("  O vírus pode ser obtido por passar a mão em alguma superfície contamina e depois passar nos olhos ou boca, sendo uma forma de contaminação")
            print("Outras questoes:")
            print("  (Alternativa1)- Correto!!A sopa de morcego é algo que se come porem não consegue espalhar a doença")
            print("  (Alternativa3)- Errado!!Ao entrar em contato com alguém contam ido, suas chances de obter o vírus são altas ")
            print("  (Alternatica4)- Errado!!A tosse é aonde o vírus sai e vai para o ar, quando a pessoa respira, essa pessoa fica contaminada")
            print("  (Alternativa5)- Errado!!Assim como a tosse, o espiro também solta os vírus no ar e ao respirar a pessoa fica contamina")
            print("*************************************************************************************")
            break


        elif alter1 ==3:
            print("  Errado!!")
            print("Explicação:")
            print("  Ao entrar em contato com alguém contam ido, suas chances de obter o vírus são altas ")
            print("Outras questoes:")
            print("  (Alternativa1)- Correto!!A sopa de morcego é algo que se come porem não consegue espalhar a doença")
            print("  (Alternativa2)- Errada!!O vírus pode ser obtido por passar a mão em alguma superfície contamina e depois passar nos olhos ou boca, sendo uma forma de contaminação")
            print("  (Alternatica4)- Errado!!A tosse é aonde o vírus sai e vai para o ar, quando a pessoa respira, essa pessoa fica contaminada")
            print("  (Alternativa5)- Errado!!Assim como a tosse, o espiro também solta os vírus no ar e ao respirar a pessoa fica contamina")
            print("*************************************************************************************")
            break


        elif alter1 ==4:
            print("  Errado!!")
            print("Explicação:")
            print("  A tosse é aonde o vírus sai e vai para o ar, quando a pessoa respira, essa pessoa fica contaminada")
            print("Outras questoes:")
            print("  (Alternativa1)- Correto!!A sopa de morcego é algo que se come porem não consegue espalhar a doença")
            print("  (Alternativa2)- Errada!!O vírus pode ser obtido por passar a mão em alguma superfície contamina e depois passar nos olhos ou boca, sendo uma forma de contaminação")
            print("  (Alternativa3)- Errado!!Ao entrar em contato com alguém contam ido, suas chances de obter o vírus são altas ")
            print("  (Alternativa5)- Errado!!Assim como a tosse, o espiro também solta os vírus no ar e ao respirar a pessoa fica contamina")
            print("*************************************************************************************")
            break


        elif alter1 ==5:
            print("  Errado!!")
            print("Explicação:")
            print("  Assim como a tosse, o espiro também solta os vírus no ar e ao respirar a pessoa fica contamina")
            print("Outras questoes:")
            print("  (Alternativa1)- Correto!!A sopa de morcego é algo que se come porem não consegue espalhar a doença")
            print("  (Alternativa2)- Errada!!O vírus pode ser obtido por passar a mão em alguma superfície contamina e depois passar nos olhos ou boca, sendo uma forma de contaminação")
            print("  (Alternativa3)- Errado!!Ao entrar em contato com alguém contam ido, suas chances de obter o vírus são altas ")
            print("  (Alternatica4)- Errado!!A tosse é aonde o vírus sai e vai para o ar, quando a pessoa respira, essa pessoa fica contaminada")
            print("*************************************************************************************")
            break
        else:
            if alter1<=0 or alter1>=6:
                alter1 = input("Valor invalido, digite novamente: ")

        #questao 6
    print("  Questao 6: O micro-ondas é presença obrigatória nas casas de milhões de famílias por aí. Será que as ondas radioativas emitidas por ele não fazem mal à saúde?")
    print("  São várias opiniões acerca desse assunto. E você, o que pensa sobre o micro-ondas?")
    print("   1- Ele pode causar câncer, porque emite ondas eletromagnéticas no ambiente")
    print("   2- A água que é aquecida no micro-ondas pode matar peixes e plantas")
    print("   3- Os alimentos absorvem a radiação do micro-ondas, podendo se tornar prejudiciais")
    print("   4- O micro-ondas é comprovadamente seguro para uso, e não faz mal nenhum à saúde")
    print("   5- Olhar pela porto do micro-ondas enquanto ele esta ligado causa cegueira")
    for i in lista1: 
        alter1 = int(input("    Alternativa escolhida: "))
        if alter1 == 1:
            print("  Errado!!")
            print("Explicação:")
            print("  Ele emite micro-ondas porem elas não fazem mal nenhum, são feitos dentro dos padrões de segurança")
            print("Outras questoes:")
            print("  (Alternativa2)- Errado!!Ele emite uma baixa radiação que absorve as moléculas de agua dos alimentos, mas não pode matar")
            print("  (Alternativa3)- Errado!!Os alimentos nao sao aquecidos da mesma maneira que a agua, nao causando nenhum problema ou doenca")
            print("  (Alternatica4)- Correto!!O micro-ondas não faz mal nenhum a ninguém, pois está sendo no padrão de segurança")
            print("  (Alternativa5)- Errado!!As ondas que o micro-ondas emite não podem causar problema a pessoa, por serem ondas fracas")
            print("*************************************************************************************")
            break

        
        elif alter1 ==2:
            print("  Errada!!")
            print("Explicação:")
            print("  Ele emite uma baixa radiação que absorve as moléculas de agua dos alimentos, mas não pode matar")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!Ele emite micro-ondas porem elas não fazem mal nenhum, são feitos dentro dos padrões de segurança")
            print("  (Alternativa3)- Errado!!Os alimentos nao sao aquecidos da mesma maneira que a agua, nao causando nenhum problema ou doenca")
            print("  (Alternatica4)- Correto!!O micro-ondas não faz mal nenhum a ninguém, pois está sendo no padrão de segurança")
            print("  (Alternativa5)- Errado!!As ondas que o micro-ondas emite não podem causar problema a pessoa, por serem ondas fracas")
            print("*************************************************************************************")
            break


        elif alter1 ==3:
            print("  Errado!!")
            print("Explicação:")
            print("  Os alimentos nao sao aquecidos da mesma maneira que a agua, nao causando nenhum problema ou doenca")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!Ele emite micro-ondas porem elas não fazem mal nenhum, são feitos dentro dos padrões de segurança")
            print("  (Alternativa2)- Errado!!Ele emite uma baixa radiação que absorve as moléculas de agua dos alimentos, mas não pode matar")
            print("  (Alternatica4)- Correto!!O micro-ondas não faz mal nenhum a ninguém, pois está sendo no padrão de segurança")
            print("  (Alternativa5)- Errado!!As ondas que o micro-ondas emite não podem causar problema a pessoa, por serem ondas fracas")
            print("*************************************************************************************")
            break


        elif alter1 ==4:
            print("  Errado!!")
            print("Explicação:")
            print("  A tosse é aonde o vírus sai e vai para o ar, quando a pessoa respira, essa pessoa fica contaminada")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!Ele emite micro-ondas porem elas não fazem mal nenhum, são feitos dentro dos padrões de segurança")
            print("  (Alternativa2)- Errado!!Ele emite uma baixa radiação que absorve as moléculas de agua dos alimentos, mas não pode matar")
            print("  (Alternativa3)- Errado!!Os alimentos nao sao aquecidos da mesma maneira que a agua, nao causando nenhum problema ou doenca")
            print("  (Alternativa5)- Errado!!As ondas que o micro-ondas emite não podem causar problema a pessoa, por serem ondas fracas")
            print("*************************************************************************************")
            soma +=200
            break


        elif alter1 ==5:
            print("  Errado!!")
            print("Explicação:")
            print("  Assim como a tosse, o espiro também solta os vírus no ar e ao respirar a pessoa fica contamina")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!Ele emite micro-ondas porem elas não fazem mal nenhum, são feitos dentro dos padrões de segurança")
            print("  (Alternativa2)- Errado!!Ele emite uma baixa radiação que absorve as moléculas de agua dos alimentos, mas não pode matar")
            print("  (Alternativa3)- Errado!!Os alimentos nao sao aquecidos da mesma maneira que a agua, nao causando nenhum problema ou doenca")
            print("  (Alternatica4)- Correto!!O micro-ondas não faz mal nenhum a ninguém, pois está sendo no padrão de segurança")
            print("*************************************************************************************")
            break
        else:
            if alter1<=0 or alter1>=6:
                alter1 = input("Valor invalido, digite novamente: ")
                

                #questao 7
    print("  Questao 7: O HIV foi diagnosticado a quase 40 anos atrás, mas segue sendo tabu na sociedade. Ainda tem muita gente desinformada sobre os sintomas, o tratamento e as formas de transmissão")
    print("  Você sabe tudo sobre o HIV? Então selecione a opção que não configura uma forma de contágio")
    print("   1- A mãe pode passar o vírus para o filho durante a gestação ou amamentação")
    print("   2- As relações sexuais desprotegidas podem transmitir a doença")
    print("   3- O HIV é transmitido também pelo contato com a saliva e lágrimas da pessoa infectada;")
    print("   4- É possível contrair o HIV por instrumentos não esterilizados, como as ferramentas da manicure ou utensílios médicos")
    print("   5- Por doação de sangue")
    for i in lista1: 
        alter1 = int(input("    Alternativa escolhida: "))
        if alter1 == 1:
            print("  Errado!!")
            print("Explicação:")
            print("  A mãe pode passar para o filho por meio do leite, pois é algo que o corpo esta produzindo")
            print("Outras questoes:")
            print("  (Alternativa2)- Errado!!Se uma pessoa que já tem HIV e faz relações sexuais sem proteção, o outro parceiro contrai a doença")
            print("  (Alternativa3)- Correto!!HIV não é transmitido pela saliva ou por lágrimas da pessoa infectada. Esses fluidos não contêm uma quantidade suficiente do vírus para contaminar outra pessoa")
            print("  (Alternatica4)- Errado!!É possível pegar de agulhas ou objetos que furam, pois em contado com o sangue da pessoa")
            print("  (Alternativa5)- Errado!!A doação de sangue para pessoa que tem HIV não é permitido, pois podem espalhar a doença")
            print("*************************************************************************************")
            break

        
        elif alter1 ==2:
            print("  Errada!!")
            print("Explicação:")
            print("  Se uma pessoa que já tem HIV e faz relações sexuais sem proteção, o outro parceiro contrai a doença")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!A mãe pode passar para o filho por meio do leite, pois é algo que o corpo esta produzindo")
            print("  (Alternativa3)- Correto!!HIV não é transmitido pela saliva ou por lágrimas da pessoa infectada. Esses fluidos não contêm uma quantidade suficiente do vírus para contaminar outra pessoa")
            print("  (Alternatica4)- Errado!!É possível pegar de agulhas ou objetos que furam, pois em contado com o sangue da pessoa")
            print("  (Alternativa5)- Errado!!A doação de sangue para pessoa que tem HIV não é permitido, pois podem espalhar a doença")
            print("*************************************************************************************")
            break


        elif alter1 ==3:
            print("  Correto!!")
            print("Explicação:")
            print("  Os alimentos nao sao aquecidos da mesma maneira que a agua, nao causando nenhum problema ou doenca")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!A mãe pode passar para o filho por meio do leite, pois é algo que o corpo esta produzindo")
            print("  (Alternativa2)- Errado!!Se uma pessoa que já tem HIV e faz relações sexuais sem proteção, o outro parceiro contrai a doença")
            print("  (Alternatica4)- Errado!!É possível pegar de agulhas ou objetos que furam, pois em contado com o sangue da pessoa")
            print("  (Alternativa5)- Errado!!A doação de sangue para pessoa que tem HIV não é permitido, pois podem espalhar a doença")
            print("*************************************************************************************")
            soma += 800
            break


        elif alter1 ==4:
            print("  Errado!!")
            print("Explicação:")
            print("  A tosse é aonde o vírus sai e vai para o ar, quando a pessoa respira, essa pessoa fica contaminada")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!A mãe pode passar para o filho por meio do leite, pois é algo que o corpo esta produzindo")
            print("  (Alternativa2)- Errado!!Se uma pessoa que já tem HIV e faz relações sexuais sem proteção, o outro parceiro contrai a doença")
            print("  (Alternativa3)- Correto!!HIV não é transmitido pela saliva ou por lágrimas da pessoa infectada. Esses fluidos não contêm uma quantidade suficiente do vírus para contaminar outra pessoa")
            print("  (Alternativa5)- Errado!!A doação de sangue para pessoa que tem HIV não é permitido, pois podem espalhar a doença")
            print("*************************************************************************************")
            break


        elif alter1 ==5:
            print("  Errado!!")
            print("Explicação:")
            print("  Assim como a tosse, o espiro também solta os vírus no ar e ao respirar a pessoa fica contamina")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!A mãe pode passar para o filho por meio do leite, pois é algo que o corpo esta produzindo")
            print("  (Alternativa2)- Errado!!Se uma pessoa que já tem HIV e faz relações sexuais sem proteção, o outro parceiro contrai a doença")
            print("  (Alternativa3)- Correto!!HIV não é transmitido pela saliva ou por lágrimas da pessoa infectada. Esses fluidos não contêm uma quantidade suficiente do vírus para contaminar outra pessoa")
            print("  (Alternatica4)- Errado!!É possível pegar de agulhas ou objetos que furam, pois em contado com o sangue da pessoa")
            print("*************************************************************************************")
            break
        else:
            if alter1<=0 or alter1>=6:
                alter1 = input("Valor invalido, digite novamente: ")




        #questao 8
    print("  Questao 8: Na idade média, ocorreu uma pandemia que teve como nome Peste Negra, onde milhares de pessoas morreram por conta dela. Em um certo momento dela, os judeus foram acusados de serem responsáveis pela peste, sendo acusados de pôr veneno em poços.  Sabendo disso, o impacto desse julgamento foi de: ")
    print("   1- A procura de judeus por toda Europa")
    print("   2- Diminuicao de mortes")
    print("   3- A melhora da pandemia")
    print("   4- A união de todas pessoas do mesmo feudo ")
    print("   5- A igreja não fazer nada com os judeus ")
    for i in lista1: 
        alter1 = int(input("    Alternativa escolhida: "))
        if alter1 == 1:
            print("  Correto!!")
            print("Explicação:")
            print("  A procura de judeus pela Europa foi grande, pois segundo a igreja foram eles que espalharam a peste")
            print("Outras questoes:")
            print("  (Alternativa2)- Errado!!Os números de mortes só subiram, tantos por guerras entre vilarejos quanto pela peste")
            print("  (Alternativa3)- Errado!!Não aconteceu melhora pois acabou ocorrendo mais mortes e piorando a pandemia")
            print("  (Alternatica4)- Errado!!As pessoas se afastaram por conta da peste e por conta dos judeus")
            print("  (Alternativa5)- Errado!!A igreja matou alguns judeus para que pagassem pelos seus pegados")
            print("*************************************************************************************")
            soma +=200
            break

        
        elif alter1 ==2:
            print("  Errada!!")
            print("Explicação:")
            print("  Os números de mortes só subiram, tantos por guerras entre vilarejos quanto pela peste")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!A procura de judeus pela Europa foi grande, pois segundo a igreja foram eles que espalharam a peste")
            print("  (Alternativa3)- Errado!!Não aconteceu melhora pois acabou ocorrendo mais mortes e piorando a pandemia")
            print("  (Alternatica4)- Errado!!As pessoas se afastaram por conta da peste e por conta dos judeus")
            print("  (Alternativa5)- Errado!!A igreja matou alguns judeus para que pagassem pelos seus pegados")
            print("*************************************************************************************")
            break


        elif alter1 ==3:
            print("  Correto!!")
            print("Explicação:")
            print("  Não aconteceu melhora pois acabou ocorrendo mais mortes e piorando a pandemia")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!A procura de judeus pela Europa foi grande, pois segundo a igreja foram eles que espalharam a peste")
            print("  (Alternativa2)- Errado!!Os números de mortes só subiram, tantos por guerras entre vilarejos quanto pela peste")
            print("  (Alternatica4)- Errado!!As pessoas se afastaram por conta da peste e por conta dos judeus")
            print("  (Alternativa5)- Errado!!A igreja matou alguns judeus para que pagassem pelos seus pegados")
            print("*************************************************************************************")
            break


        elif alter1 ==4:
            print("  Errado!!")
            print("Explicação:")
            print("  A tosse é aonde o vírus sai e vai para o ar, quando a pessoa respira, essa pessoa fica contaminada")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!A procura de judeus pela Europa foi grande, pois segundo a igreja foram eles que espalharam a peste")
            print("  (Alternativa2)- Errado!!Os números de mortes só subiram, tantos por guerras entre vilarejos quanto pela peste")
            print("  (Alternativa3)- Errado!!Não aconteceu melhora pois acabou ocorrendo mais mortes e piorando a pandemia")
            print("  (Alternativa5)- Errado!!A igreja matou alguns judeus para que pagassem pelos seus pegados")
            print("*************************************************************************************")
            break


        elif alter1 ==5:
            print("  Errado!!")
            print("Explicação:")
            print("  Assim como a tosse, o espiro também solta os vírus no ar e ao respirar a pessoa fica contamina")
            print("Outras questoes:")
            print("  (Alternativa1)- Errado!!A procura de judeus pela Europa foi grande, pois segundo a igreja foram eles que espalharam a peste")
            print("  (Alternativa2)- Errado!!Os números de mortes só subiram, tantos por guerras entre vilarejos quanto pela peste")
            print("  (Alternativa3)- Errado!!Não aconteceu melhora pois acabou ocorrendo mais mortes e piorando a pandemia")
            print("  (Alternatica4)- Errado!!As pessoas se afastaram por conta da peste e por conta dos judeus")
            print("*************************************************************************************")
            break
        else:
            if alter1<=0 or alter1>=6:
                alter1 = input("Valor invalido, digite novamente: ")


    print("O total de pontos foi:", soma,"/ 3600")

def main():
    msg()
    quest1()


main()
