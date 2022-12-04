import pandas as pd, numpy as np
import matplotlib.pyplot as plt

#H:\materias\probabilidade

# lendo planilha
a = pd.read_csv("Planilha sem título - Página1.csv")

# ## Gerando histograma da idade dos intrevistados
# a['Idade:'].value_counts().sort_index().plot.bar()
# plt.savefig("grafico idade")
# plt.close("all")

# ##grafico de quantidade de intervistados por sexo
# a['Sexo'].value_counts().plot.pie(autopct='%.02f%%')
# plt.savefig("sexo")
# plt.close("all")


# ## contando quantidade de intrevistados por idade por sexo ##
# #determinando vetor de idade de intrevistados por sexo
# idade_por_sexo={'Masculino':[],'Feminino':[]}
# for index in a.index:
#     idade_por_sexo[a['Sexo'].loc[index]].append(a['Idade:'].loc[index])
# #determinando quantidade de intrevistados por idade por sexo
# contagem_idade_por_sexo={'Masculino':{},'Feminino':{}}
# for sexo in idade_por_sexo:
#     for idade in idade_por_sexo[sexo]:
#         contagem_idade_por_sexo[sexo].setdefault(idade,0)
#         contagem_idade_por_sexo[sexo][idade]+=1
# print()
# print('Quantidade de intrevistados por idade por sexo:')
# print(pd.DataFrame(contagem_idade_por_sexo).sort_index().fillna(0))
# #gerando grafico
# fig, axs = plt.subplots(len(contagem_idade_por_sexo),figsize=(10,8))
# for n,sexo in enumerate(contagem_idade_por_sexo):
#     contagem = contagem_idade_por_sexo[sexo]
#     axs[n].bar(contagem.keys(),contagem.values())
#     axs[n].set_title(sexo)
# #salvando
# plt.savefig("idade por genero")
# #limpando grafico para uso futuro
# plt.close("all")



# ## plot da qtd de intrevistados por semestre
# print()
# print('Distribuição de entrevistados por semestre:')
# print(a['Cursando semestre:'].value_counts().sort_index())
# a['Cursando semestre:'].value_counts().sort_index().plot.bar()
# plt.savefig("intrevistados por semestre")
# plt.close("all")

# ##Graficos de Renda familiar dos intrevistados
# # ajustando dados de renda familiar para voltar para categorias em string
# a['Renda familiar'] = a['Renda familiar'].apply(lambda c: "Até 1 salário mínimo" if c == 1 
#                                                         else "De 1 a 3 salários mínimos" if c==2 
#                                                         else "De 3 a 5 salários mínimos" if c==3 
#                                                         else "De 5 a 7 salários mínimos" if c == 4 
#                                                         else "7+ salários mínimos" if c == 5 
#                                                         else "Não Respondeu")
# # grafico de quantidade de intrevistado por categoria em renda familiar
# a['Renda familiar'].value_counts().plot.barh(figsize=(16,9))
# plt.savefig("distribuição renda familiarrenda familiar")
# plt.close("all")
# print()
# print("distribuição renda familiar")
# print(a['Renda familiar'].value_counts().sort_index())


# ##grafico de pizza de dsipositivo mais usado
# a['Qual dispositivo você mais utiliza?'].value_counts().sort_index().plot.pie(autopct="%.2f%%")
# plt.savefig("dispositimo mais usado")
# plt.close("all")
# print()
# print('quantidade de intrevistados por aparelho:')
# print(a['Qual dispositivo você mais utiliza?'].value_counts().sort_index())

# ## grafico das peguntas sim ou nao ##
# # escolhendo perguntas
# perguntas_s_n_vet = ["Você utiliza a internet para trabalho?","Você utiliza a internet para conversar com amigos?",
#               "Você utiliza a internet para conversar com desconhecidos?","Você utiliza e-mail?",
#               "Você utiliza a internet para realizar Pesquisas Acadêmicas?","Você utiliza a internet para acessar noticias?",
#               "Você faz compras online?","Você assiste vídeos online?","Você utiliza a internet para participar de jogos online?",
#               "Você acredita que a internet atrapalha em sua formação?","Você considera as redes sociais um ambiente tóxico?",
#               "Você utiliza a internet para fazer download de conteúdo?"]
# #label do grafico para perguntas acima
# perguntas_s_n_labels_vet = ['Para trabalho','Converça com amigos','Conversa com estranhos','Usa email','Pesquisas academicas',
#                             'Ver noticias','Compras','Ver vidios','Jogar','Atraplahar formação','Redes sociais toxicas',
#                             'Download de conteudo']
# #criando blocos
# block_size = 3 # quantidade de perguntas por grafico
# blocos = [ 
#             [ (pergunta,label) for pergunta,label in zip(perguntas_s_n_vet[n*block_size:(n+1)*block_size],
#                                                          perguntas_s_n_labels_vet[n*block_size:(n+1)*block_size]) 
#             ] for n in range(int(len(perguntas_s_n_vet)/block_size)) 
#         ]
# for bloco_numero,pergunta_label in enumerate(blocos):
#     resp = [ a[pergunta].value_counts() for pergunta,label in pergunta_label ]
#     possiveis_resp = {"Sim":[],'Não':[]}
#     for n,b in enumerate(resp):
#         b = b.to_dict()
#         for key,value in possiveis_resp.items():
#             try:
#                 value.append(b[key])
#             except KeyError:
#                 value.append(0)

#     fig, ax = plt.subplots(figsize=(32,9))
#     fig.subplots_adjust(left=0,right=1)
#     plots = []
#     for n,(key,value) in enumerate(possiveis_resp.items()):
#         plot = ax.bar([label for pergunta,label in pergunta_label], value, 0.5, label=key,bottom= 0 if n==0 else temp)
#         plots.append(plot)
#         temp = value
#     for plot in plots:
#         ax.bar_label(plot, label_type='center', fontsize=50)
#         for item in ax.xaxis.get_ticklabels():
#             item.set_fontsize(40)
#     ax.legend(fontsize=30)
#     plt.savefig(f'perguntas_{bloco_numero}')
#     plt.close("all")

# ## Grafico das 2 ultimas pergutnas
def filter(v,f):
    return f[v]


# filtro = {'É um avanço da tecnologia que está melhorando a vida das pessoas':1,
#             'Um jeito mais rápido e eficiente para me comunicar com as pessoas':2,
#             "Só atrapalha a vida das pessoas que agora têm que aprender muito mais para poder fazer as mesmas coisas.":3}

# temp = pd.DataFrame()

# t = a["Dentre as opções, qual mais se assemelha ao que o computador representa para você?"].apply(filter,args=(filtro,))
# temp["Dentre as opções, qual mais se assemelha ao que o computador representa para você?"] = t
# t = t.value_counts()

# print()
# print('O que o compudor representa:')
# print(t)

# ## Relacionando o que o computador representa e como se sente em relação a informatica
# ax = plt.subplot(1,2,1)
# ax.set_title('O que o computador representa')
# t.plot.pie(ax = ax, ylabel ='',autopct='%.2f%%')

# filtro = {'Estou entusiasmado e quero saber muito mais':1,
#             'Acho tudo muito difícil e complicado':2,
#             "Sou obrigada a aprender para poder estudar e/ou trabalhar":3,
#             'Sou obrigado(a) a aprender para poder estudar e/ou trabalhar':3}

# t = a["Dentre as opções, qual mais se assemelha a como você se sente em relação a informática?"].apply(filter,args=(filtro,))
# temp["Dentre as opções, qual mais se assemelha a como você se sente em relação a informática?"] = t

# t = t.value_counts()
# print()
# print('Como se sente em relação a informatica:')
# print(t)

# ax = plt.subplot(1,2,2)
# ax.set_title('Como se sente em relação informatica')
# t.plot.pie(ax = ax, ylabel ='',autopct='%.2f%%')

# plt.subplots_adjust(left = 0.02 , right=.92,)

# plt.savefig('computador representa, sentimento informatica')
# print()
# print('Matrix de respostas das ultimas 2 perguntas:')
# print(temp.value_counts())


# ##Relação dispositivo mais usado e tempo de uso
# b = a[['Qual dispositivo você mais utiliza?',"Em geral, quanto tempo você permanece conectado à intenet diariamente?"]]
# # print(b)
# resp = {}
# for n in range(b.last_valid_index()):
#     t,y = b.iloc[n]
#     resp.setdefault(t,{})
#     resp[t].setdefault(y,0)
#     resp[t][y]+=1
# print('Dados de tempo de uso por dispositivo mais usado')
# print(pd.DataFrame(resp))
# fig, axs = plt.subplots(len(resp))
# for n,(disp,horas) in enumerate(resp.items()):
#     axs[n].pie(horas.values(),labels= horas.keys(),autopct='%.0f%%')
#     axs[n].set_title(disp)
# plt.savefig('Dispositivo X tempo de uso')

# ##Relação Semestre com tempo de uso
# a['acima_abaixo'] = [ "acima do 5º semestre" if b>5 else 'abaixo do 5º semestre' for b in a['Cursando semestre:']]
# b = a[['acima_abaixo',"Em geral, quanto tempo você permanece conectado à intenet diariamente?"]]
# # print(b)
# resp = {}
# for n in range(b.last_valid_index()):
#     t,y = b.iloc[n]
#     resp.setdefault(t,{})
#     resp[t].setdefault(y,0)
#     resp[t][y]+=1
# print(pd.DataFrame(resp))
# fig, axs = plt.subplots(len(resp))
# for n,(disp,horas) in enumerate(resp.items()):
#     axs[n].pie(horas.values(),labels= horas.keys(),autopct='%.0f%%')
#     axs[n].set_title(disp)
# plt.savefig('tempo de uso X semestre')

# ##intenet atrapalha x como se sente
# filtro = {'Estou entusiasmado e quero saber muito mais':1,
#             'Acho tudo muito difícil e complicado':2,
#             "Sou obrigada a aprender para poder estudar e/ou trabalhar":3,
#             'Sou obrigado(a) a aprender para poder estudar e/ou trabalhar':3}

# a["Dentre as opções, qual mais se assemelha a como você se sente em relação a informática?"] = a["Dentre as opções, qual mais se assemelha a como você se sente em relação a informática?"].apply(filter,args=(filtro,))
# resp = {}
# b = a[['Você acredita que a internet atrapalha em sua formação?',"Dentre as opções, qual mais se assemelha a como você se sente em relação a informática?"]]

# for n in range(b.last_valid_index()):
#     t,y = b.iloc[n]
#     resp.setdefault(t,{})
#     resp[t].setdefault(y,0)
#     resp[t][y]+=1
# print(pd.DataFrame(resp))
# fig, axs = plt.subplots(len(resp))
# for n,(disp,horas) in enumerate(resp.items()):
#     axs[n].pie(horas.values(),labels= horas.keys(),autopct='%.0f%%')
#     axs[n].set_title('Atrapalha' if  disp == 'Sim' else 'Não Atrapalha')
# plt.savefig('intenet atrapalha x como se sente')

## Como se sente em relação a computador X tempo de uso
filtro = {'É um avanço da tecnologia que está melhorando a vida das pessoas':1,
            'Um jeito mais rápido e eficiente para me comunicar com as pessoas':2,
            "Só atrapalha a vida das pessoas que agora têm que aprender muito mais para poder fazer as mesmas coisas.":3}

a["Dentre as opções, qual mais se assemelha ao que o computador representa para você?"] = a["Dentre as opções, qual mais se assemelha ao que o computador representa para você?"].apply(filter,args=(filtro,))
b = a[["Dentre as opções, qual mais se assemelha ao que o computador representa para você?","Em geral, quanto tempo você permanece conectado à intenet diariamente?"]] 

print(b.value_counts())



# #função que retorna o valores de t qando r == k ou NaN
# def f(r,t,k):
#     return [ f if  k == e else np.NaN for e,f in zip(r.values,t.values) ]

# vetor de sexo de alunos que estudam a noite
# t = f(a["Qual o turno do seu curso?"],a['Sexo'],'Noturno')

# # neste plote tera 2 graficos em cima a qtd de alunos que estudam a noite
# #  no de baixo a qtd de alunos que estudam noite + diurno

# # Fazendo subplot de do grafico dos alunos que estudam a noite
# ax = plt.subplot(2,1,1)
# ax.set_title('Alunos que estudam Noturno')
# t = pd.Series(t).dropna().value_counts()
# ax.bar(t.keys(),t.values)
# # pd.Series(t).dropna().value_counts().plot.barh()

# # vetor de sexo de alunos que estudam a noite + diurno
# t = f(a["Qual o turno do seu curso?"],a['Sexo'],'Diurno, Noturno')
# # pd.Series(t).dropna().value_counts().plot.barh()

# # subplot do grafico de qtd de alunos noite + diurno
# ax = plt.subplot(2,1,2)
# ax.set_title('Alunos que estudam Diurno + Noturno')
# t = pd.Series(t).dropna().value_counts()
# ax.bar(t.keys(),t.values)

# plt.show()
# plt.close("all")
# print(t)






# grafico de pizza de tempo de uso diario de internet
# a["Em geral, quanto tempo você permanece conectado à intenet diariamente?"].value_counts().sort_index().plot.bar()
# plt.ylabel('Tempo de uso da intenet diario')
# plt.show()
# plt.close("all")


# ## grafico de intrevistados por turno estudado
# a["Qual o turno do seu curso?"].value_counts().plot.barh()
# plt.savefig("qtd de intrevistado por turno estudado")
# plt.close("all")