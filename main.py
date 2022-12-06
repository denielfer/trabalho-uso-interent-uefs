import pandas as pd, numpy as np
import matplotlib.pyplot as plt

# lendo planilha
a = pd.read_csv("Planilha sem título - Página1.csv")

## Gerando histograma da idade dos intrevistados
a['Idade:'].value_counts().sort_index().plot.bar()
plt.savefig("img//grafico idade")
plt.close("all")

##grafico de quantidade de intervistados por sexo
a['Sexo'].value_counts().plot.pie(autopct='%.02f%%')
plt.savefig("img//sexo")
plt.close("all")


## contando quantidade de intrevistados por idade por sexo ##
#determinando vetor de idade de intrevistados por sexo
idade_por_sexo={'Masculino':[],'Feminino':[]}
for index in a.index:
    idade_por_sexo[a['Sexo'].loc[index]].append(a['Idade:'].loc[index])
#determinando quantidade de intrevistados por idade por sexo
contagem_idade_por_sexo={'Masculino':{},'Feminino':{}}
for sexo in idade_por_sexo:
    for idade in idade_por_sexo[sexo]:
        contagem_idade_por_sexo[sexo].setdefault(idade,0)
        contagem_idade_por_sexo[sexo][idade]+=1
print()
print('Quantidade de intrevistados por idade por sexo:')
print(pd.DataFrame(contagem_idade_por_sexo).sort_index().fillna(0))
#gerando grafico
fig, axs = plt.subplots(len(contagem_idade_por_sexo),figsize=(10,8))
for n,sexo in enumerate(contagem_idade_por_sexo):
    contagem = contagem_idade_por_sexo[sexo]
    axs[n].bar(contagem.keys(),contagem.values())
    axs[n].set_title(sexo)
#salvando
plt.savefig("img//idade por genero")
#limpando grafico para uso futuro
plt.close("all")



## plot da qtd de intrevistados por semestre
print()
print('Distribuição de entrevistados por semestre:')
print(a['Cursando semestre:'].value_counts().sort_index())
b = a["Cursando semestre:"]
print('Semestre medio:',b.mean(),', Mediana: ',b.median())
print('Desvio padrao:',b.std(),', Variancia: ',b.var())
print()
a['Cursando semestre:'].value_counts().sort_index().plot.bar()
plt.savefig("img//intrevistados por semestre")
plt.close("all")

##Graficos de Renda familiar dos intrevistados
# ajustando dados de renda familiar para voltar para categorias em string
a['Renda_familiar_filtrado'] = a['Renda familiar'].apply(lambda c: "Até 1 salário mínimo" if c == 1 
                                                        else "De 1 a 3 salários mínimos" if c==2 
                                                        else "De 3 a 5 salários mínimos" if c==3 
                                                        else "De 5 a 7 salários mínimos" if c == 4 
                                                        else "7+ salários mínimos" if c == 5 
                                                        else "Não Respondeu")
# grafico de quantidade de intrevistado por categoria em renda familiar
a['Renda_familiar_filtrado'].value_counts().plot.barh(figsize=(16,9), fontsize=(30))
plt.subplots_adjust(left = 0.35 , right=.98)
plt.savefig("img//Renda familiar")
plt.close("all")
print()
print("distribuição renda familiar")
print(a['Renda_familiar_filtrado'].value_counts().sort_index())


##grafico de pizza de dsipositivo mais usado
a['Qual dispositivo você mais utiliza?'].value_counts().sort_index().plot.pie(autopct="%.2f%%")
plt.savefig("img//dispositimo mais usado")
plt.close("all")
print()
print('quantidade de intrevistados por aparelho:')
print(a['Qual dispositivo você mais utiliza?'].value_counts().sort_index())

## grafico das peguntas sim ou nao ##
# escolhendo perguntas
perguntas_s_n_vet = ["Você utiliza a internet para trabalho?","Você utiliza a internet para conversar com amigos?",
              "Você utiliza a internet para conversar com desconhecidos?","Você utiliza e-mail?",
              "Você utiliza a internet para realizar Pesquisas Acadêmicas?","Você utiliza a internet para acessar noticias?",
              "Você faz compras online?","Você assiste vídeos online?","Você utiliza a internet para participar de jogos online?",
              "Você acredita que a internet atrapalha em sua formação?","Você considera as redes sociais um ambiente tóxico?",
              "Você utiliza a internet para fazer download de conteúdo?"]
#label do grafico para perguntas acima
perguntas_s_n_labels_vet = ['Para trabalho','Conversa com os amigos','Conversa com estranhos','Usa email','Pesquisas academicas',
                            'Ver noticias','Compras','Ver vídeos','Jogar','Atrapalha a formação','Redes sociais tóxicas',
                            'Download de conteúdo']
#criando blocos de pergutnas
block_size = 3 # quantidade de perguntas por grafico
blocos = [ 
            [ (pergunta,label) for pergunta,label in zip(perguntas_s_n_vet[n*block_size:(n+1)*block_size],
                                                         perguntas_s_n_labels_vet[n*block_size:(n+1)*block_size]) 
            ] for n in range(int(len(perguntas_s_n_vet)/block_size)) 
        ]
# Para cada bloco
for bloco_numero,pergunta_label in enumerate(blocos):
    # separando as respostas das pergutnas
    resp = [ a[pergunta].value_counts() for pergunta,label in pergunta_label ]
    possiveis_resp = {"Sim":[],'Não':[]}
    for n,b in enumerate(resp):
        b = b.to_dict()
        for key,value in possiveis_resp.items():
            try:
                value.append(b[key])
            except KeyError:
                value.append(0)
    #criando plot do bloco
    fig, ax = plt.subplots(figsize=(32,9))
    fig.subplots_adjust(left=0,right=1)
    plots = []
    #plotando 
    for n,(key,value) in enumerate(possiveis_resp.items()):
        plot = ax.bar([label for pergunta,label in pergunta_label], value, 0.5, label=key,bottom= 0 if n==0 else temp)
        plots.append(plot)
        temp = value
    #ajustando plot
    for plot in plots:
        ax.bar_label(plot, label_type='center', fontsize=50)
        for item in ax.xaxis.get_ticklabels():
            item.set_fontsize(40)
    ax.legend(fontsize=30)
    #salvando
    plt.savefig(f'img//perguntas_{bloco_numero}')
    plt.close("all")

## Grafico das 2 ultimas pergutnas
#filtro para passar no dataframe
def filter(v,f):
    return f[v]


filtro = {'É um avanço da tecnologia que está melhorando a vida das pessoas':1,
            'Um jeito mais rápido e eficiente para me comunicar com as pessoas':2,
            "Só atrapalha a vida das pessoas que agora têm que aprender muito mais para poder fazer as mesmas coisas.":3}

temp = pd.DataFrame()

t = a["Dentre as opções, qual mais se assemelha ao que o computador representa para você?"].apply(filter,args=(filtro,))
temp["Dentre as opções, qual mais se assemelha ao que o computador representa para você?"] = t
t = t.value_counts()

print()
print('O que o compudor representa:')
print(t)

## Relacionando o que o computador representa e como se sente em relação a informatica
ax = plt.subplot(1,2,1)
ax.set_title('O que o computador representa')
t.plot.pie(ax = ax, ylabel ='',autopct='%.2f%%')

filtro = {'Estou entusiasmado e quero saber muito mais':1,
            'Acho tudo muito difícil e complicado':2,
            "Sou obrigada a aprender para poder estudar e/ou trabalhar":3,
            'Sou obrigado(a) a aprender para poder estudar e/ou trabalhar':3}

t = a["Dentre as opções, qual mais se assemelha a como você se sente em relação a informática?"].apply(filter,args=(filtro,))
temp["Dentre as opções, qual mais se assemelha a como você se sente em relação a informática?"] = t

t = t.value_counts()
print()
print('Como se sente em relação a informatica:')
print(t)

ax = plt.subplot(1,2,2)
ax.set_title('Como se sente em relação informatica')
t.plot.pie(ax = ax, ylabel ='',autopct='%.2f%%')

plt.subplots_adjust(left = 0.02 , right=.92,)

plt.savefig('img//computador representa, sentimento informatica')
plt.close("all")
print()
print('Matrix de respostas das ultimas 2 perguntas:')
print(temp.value_counts())


def graf_coluna(resp):
    '''
        Função para geração de graficos em coluna, 1 linha para cada grafico com 1 unica coluna
    '''
    fig, axs = plt.subplots(len(resp))
    for n,(disp,horas) in enumerate(resp.items()):
        axs[n].pie(horas.values(),labels= horas.keys(),autopct='%.0f%%')
        axs[n].set_title(disp)

def graficos_pizza_para_2_perguntas(pergutna1:str,pergunta2:str,dataframe:pd.DataFrame,nome_arquivo:str,show:bool=False, grafico = graf_coluna):
    '''
        Faz a matriz de respostas para pergunta1 e pergunta2 presentes no dataframe, chamando a função grafico que recebera 
            o objeto contendo a matriz de respsotas. Sendo printado o dataframe resultante da matriz de respostas.

        grafico-> função que gera o grafico a ser salvo

        nome_arquivo -> nome que o plot sera salvo, na mesma pasta de execução
        show-> mostra o plot ( acontece antes de salvar )
    '''
    b = dataframe[[pergutna1,pergunta2]]
    resp = {}
    for n in range(b.last_valid_index()+1):
        t,y = b.iloc[n]
        resp.setdefault(t,{})
        resp[t].setdefault(y,0)
        resp[t][y]+=1
    print()
    print(nome_arquivo)
    print(pd.DataFrame(resp))
    grafico(resp)
    if show:
        plt.show()
    if nome_arquivo is not None and nome_arquivo != '':
        plt.savefig('img//'+nome_arquivo)
    plt.close("all")


##Relação dispositivo mais usado e tempo de uso
graficos_pizza_para_2_perguntas('Qual dispositivo você mais utiliza?',
    "Em geral, quanto tempo você permanece conectado à intenet diariamente?",a,'Dispositivo X tempo de uso')

##Relação Semestre com tempo de uso
#filtro para semestre que sera usado para este grafico
a['acima_abaixo'] = [ "acima do 5º semestre" if b>5 else 'abaixo do 5º semestre' for b in a['Cursando semestre:']]

graficos_pizza_para_2_perguntas("acima_abaixo",
    "Em geral, quanto tempo você permanece conectado à intenet diariamente?",a,"tempo de uso X semestre")

##intenet atrapalha x como se sente
filtro = {'Estou entusiasmado e quero saber muito mais':1,
            'Acho tudo muito difícil e complicado':2,
            "Sou obrigada a aprender para poder estudar e/ou trabalhar":3,
            'Sou obrigado(a) a aprender para poder estudar e/ou trabalhar':3}

a["se_sente_informatica_filtro1"] = a["Dentre as opções, qual mais se assemelha a como você se sente em relação a informática?"].apply(filter,args=(filtro,))
resp = {}
b = a[['Você acredita que a internet atrapalha em sua formação?',"se_sente_informatica_filtro1"]]

for n in range(b.last_valid_index()):
    t,y = b.iloc[n]
    resp.setdefault(t,{})
    resp[t].setdefault(y,0)
    resp[t][y]+=1
print()
print(pd.DataFrame(resp))
fig, axs = plt.subplots(len(resp))
for n,(disp,horas) in enumerate(resp.items()):
    axs[n].pie(horas.values(),labels= horas.keys(),autopct='%.0f%%')
    axs[n].set_title('Atrapalha' if  disp == 'Sim' else 'Não Atrapalha')
plt.savefig('img//intenet atrapalha x como se sente')
plt.close("all")

## Como se sente em relação a computador X tempo de uso
#filtros para o que o computador representa
filtro = {'É um avanço da tecnologia que está melhorando a vida das pessoas':'É um avanço da tecnologia que está melhorando a vida das pessoas',
            'Um jeito mais rápido e eficiente para me comunicar com as pessoas':'Um jeito mais rápido e eficiente para me comunicar com as pessoas',
            "Só atrapalha a vida das pessoas que agora têm que aprender muito mais para poder fazer as mesmas coisas.":"Só atrapalha a vida das pessoas"}
# filtrando no dataframe de resposta
a["comp_representa_filtro2"] = a["Dentre as opções, qual mais se assemelha ao que o computador representa para você?"].apply(filter,args=(filtro,))
# montando grafico
graficos_pizza_para_2_perguntas("comp_representa_filtro2",
    "Em geral, quanto tempo você permanece conectado à intenet diariamente?",a,"Computador representa x temp de estudo")


##sexo por dispositivo mais usado
graficos_pizza_para_2_perguntas("Sexo","Qual dispositivo você mais utiliza?",a,"Sexo x Dispositivo")

##sexo por dispositivo mais usado
graficos_pizza_para_2_perguntas("Sexo","Você utiliza a internet para participar de jogos online?",a,"Sexo x joga online")

#sexo por dispositivo mais usado
graficos_pizza_para_2_perguntas("Sexo","Em geral, quanto tempo você permanece conectado à intenet diariamente?",a,'Sexo x Tempo uso')


def grafico_3_2(resp):
    '''
        Realiza o plot dos graficos de piza em uma disposição de 3 linhas e 2 colunas
    '''
    fig, axs = plt.subplots(3,2)
    for n,(disp,horas) in enumerate(resp.items()):
        x , y = n if n-3 < 0 else n-3,0 if n-3 < 0 else 1
        axs[x,y].pie(horas.values(),labels= horas.keys(),autopct='%.0f%%')
        axs[x,y].set_title(disp)
##Renda familiar x dispositivo
b = a[['Renda_familiar_filtrado',"Qual dispositivo você mais utiliza?"]]
graficos_pizza_para_2_perguntas('Renda_familiar_filtrado',"Qual dispositivo você mais utiliza?",a,
                                'Renda familiar X Dispositivo',grafico = grafico_3_2)
##Renda x Tempo de uso diario
graficos_pizza_para_2_perguntas('Renda_familiar_filtrado',"Em geral, quanto tempo você permanece conectado à intenet diariamente?"
                                ,a,'Renda familiar X Tempo conectado',grafico = grafico_3_2)
# # Renda por sexo
# graficos_pizza_para_2_perguntas('Renda_familiar_filtrado',"Sexo"
#                                 ,a,None,True,grafico = grafico_3_2)