import pandas as pd, numpy as np
import matplotlib.pyplot as plt


def filter(v,f):
    return f[v]

# lendo planilha
a = pd.read_csv("Planilha sem título - Página1.csv")

# #sexo X se joga
# b = a[["Dentre as opções, qual mais se assemelha ao que o computador representa para você?","Dentre as opções, qual mais se assemelha a como você se sente em relação a informática?"]]
# b.fillna('Não Respondeu',inplace=True)
# filtro = {'É um avanço da tecnologia que está melhorando a vida das pessoas':'É um avanço da tecnologia que está melhorando a vida das pessoas',
#             'Um jeito mais rápido e eficiente para me comunicar com as pessoas':'Um jeito mais rápido e eficiente para me comunicar com as pessoas',
#             "Só atrapalha a vida das pessoas que agora têm que aprender muito mais para poder fazer as mesmas coisas.":"Só atrapalha"}

# b["Dentre as opções, qual mais se assemelha ao que o computador representa para você?"] = b["Dentre as opções, qual mais se assemelha ao que o computador representa para você?"].apply(filter,args=(filtro,))

# filtro = {'Estou entusiasmado e quero saber muito mais':1,
#             'Acho tudo muito difícil e complicado':2,
#             "Sou obrigada a aprender para poder estudar e/ou trabalhar":3,
#             'Sou obrigado(a) a aprender para poder estudar e/ou trabalhar':3}

# b["Dentre as opções, qual mais se assemelha a como você se sente em relação a informática?"] = b["Dentre as opções, qual mais se assemelha a como você se sente em relação a informática?"].apply(filter,args=(filtro,))

# # print(b)
# resp = {}
# for n in range(b.last_valid_index()):
#     t,y = b.iloc[n]
#     resp.setdefault(t,{})
#     resp[t].setdefault(y,0)
#     resp[t][y]+=1
# print(resp)
# print(pd.DataFrame(resp))
# fig, axs = plt.subplots(len(resp))
# for n,(disp,horas) in enumerate(resp.items()):
#     axs[n].pie(horas.values(),labels= horas.keys(),autopct='%.0f%%')
#     axs[n].set_title(disp)
# plt.savefig('Computador representa x informatica representa')


# #sexo X se joga
# b = a[['Sexo',"Você utiliza a internet para participar de jogos online?"]]
# b.fillna('Não Respondeu',inplace=True)
# # print(b)
# resp = {}
# for n in range(b.last_valid_index()):
#     t,y = b.iloc[n]
#     resp.setdefault(t,{})
#     resp[t].setdefault(y,0)
#     resp[t][y]+=1
# print(resp)
# print(pd.DataFrame(resp))
# fig, axs = plt.subplots(len(resp))
# for n,(disp,horas) in enumerate(resp.items()):
#     axs[n].pie(horas.values(),labels= horas.keys(),autopct='%.0f%%')
#     axs[n].set_title(disp)
# plt.savefig('Sexo x joga')

# #sexo x tempo de uso
# b = a[['Sexo',"Em geral, quanto tempo você permanece conectado à intenet diariamente?"]]
# b.fillna('Não Respondeu',inplace=True)

# # print(b)
# resp = {}
# for n in range(b.last_valid_index()):
#     t,y = b.iloc[n]
#     resp.setdefault(t,{})
#     resp[t].setdefault(y,0)
#     resp[t][y]+=1
# print(resp)
# print(pd.DataFrame(resp))
# fig, axs = plt.subplots(len(resp))
# for n,(disp,horas) in enumerate(resp.items()):
#     axs[n].pie(horas.values(),labels= horas.keys(),autopct='%.0f%%')
#     axs[n].set_title(disp)
# plt.savefig('Sexo x Tempo uso')

# #sexo por dispositivo mais usado
# b = a[['Sexo',"Qual dispositivo você mais utiliza?"]]

# b.fillna('Não Respondeu',inplace=True)

# resp = {}
# for n in range(b.last_valid_index()):
#     t,y = b.iloc[n]
#     resp.setdefault(t,{})
#     resp[t].setdefault(y,0)
#     resp[t][y]+=1
# print(resp)
# print(pd.DataFrame(resp))
# fig, axs = plt.subplots(len(resp))
# for n,(disp,horas) in enumerate(resp.items()):
#     axs[n].pie(horas.values(),labels= horas.keys(),autopct='%.0f%%')
#     axs[n].set_title(disp)
# plt.savefig('Sexo x Dispositivo')




# #Renda familiar x dispositivo
# b = a[['Renda familiar',"Qual dispositivo você mais utiliza?"]]
# b.fillna('Não Respondeu',inplace= True)
# b['Renda familiar'] = ["Até 1 salário mínimo" if c == 1 else "De 1 a 3 salários mínimos" if c==2 else "De 3 a 5 salários mínimos" if c==3 else "De 5 a 7 salários mínimos" if c == 4 else "7+ salários mínimos" if c == 5 else "Não Respondeu" for c in b['Renda familiar']]
# # print(b)
# resp = {}
# for n in range(b.last_valid_index()):
#     t,y = b.iloc[n]
#     resp.setdefault(t,{})
#     resp[t].setdefault(y,0)
#     resp[t][y]+=1
# print(pd.DataFrame(resp).fillna(0))
# fig, axs = plt.subplots(3,2)
# for n,(disp,horas) in enumerate(resp.items()):
#     x , y = n if n-3 < 0 else n-3,0 if n-3 < 0 else 1
#     axs[x,y].pie(horas.values(),labels= horas.keys(),autopct='%.0f%%')
#     axs[x,y].set_title(disp)
# plt.savefig('Renda familiar X Dispositivo')

# #Renda familiar x tempo de uso diario
# b = a[['Renda familiar',"Em geral, quanto tempo você permanece conectado à intenet diariamente?"]]
# b.fillna('Não Respondeu',inplace= True)

# b['Renda familiar'] = ["Até 1 salário mínimo" if c == 1 else "De 1 a 3 salários mínimos" if c==2 else "De 3 a 5 salários mínimos" if c==3 else "De 5 a 7 salários mínimos" if c == 4 else "7+ salários mínimos" if c == 5 else "Não Respondeu" for c in b['Renda familiar']]

# # print(b)
# resp = {}
# for n in range(b.last_valid_index()):
#     t,y = b.iloc[n]
#     resp.setdefault(t,{})
#     resp[t].setdefault(y,0)
#     resp[t][y]+=1
# print(pd.DataFrame(resp).fillna(0))
# fig, axs = plt.subplots(3,2)
# for n,(disp,horas) in enumerate(resp.items()):
#     x , y = n if n-3 < 0 else n-3,0 if n-3 < 0 else 1
#     axs[x,y].pie(horas.values(),labels= horas.keys(),autopct='%.0f%%')
#     axs[x,y].set_title(disp)
# plt.savefig('Renda familiar X Tempo conectado')
# a = pd.read_csv("Planilha sem título - Página1.csv")



# Frazendo grafico ultima 2 perguntas
def filter(v,f):
    return f[v]


filtro = {'É um avanço da tecnologia que está melhorando a vida das pessoas':1,
            'Um jeito mais rápido e eficiente para me comunicar com as pessoas':2,
            "Só atrapalha a vida das pessoas que agora têm que aprender muito mais para poder fazer as mesmas coisas.":3}

t = a["Dentre as opções, qual mais se assemelha ao que o computador representa para você?"].apply(filter,args=(filtro,))
t = t.value_counts()
ax = plt.subplot(1,2,1)
ax.set_title('O que o computador representa')
t.plot.pie(ax = ax, ylabel ='',autopct='%.2f')

filtro = {'Estou entusiasmado e quero saber muito mais':1,
            'Acho tudo muito difícil e complicado':2,
            "Sou obrigada a aprender para poder estudar e/ou trabalhar":3,
            'Sou obrigado(a) a aprender para poder estudar e/ou trabalhar':3}

t = a["Dentre as opções, qual mais se assemelha a como você se sente em relação a informática?"].apply(filter,args=(filtro,))

t = t.value_counts()

ax = plt.subplot(1,2,2)
ax.set_title('Como se sente em relação informatica')
t.plot.pie(ax = ax, ylabel ='',autopct='%.2f')

plt.subplots_adjust(left = 0.05 , right=.95,)

plt.savefig('computador representa, sentimento informatica')


# # grafico das peguntas sim ou nao
# perguntas_s_n_vet = ["Você utiliza a internet para trabalho?","Você utiliza a internet para conversar com amigos?",
#               "Você utiliza a internet para conversar com desconhecidos?","Você utiliza e-mail?",
#               "Você utiliza a internet para realizar Pesquisas Acadêmicas?","Você utiliza a internet para acessar noticias?",
#               "Você faz compras online?","Você assiste vídeos online?","Você utiliza a internet para participar de jogos online?",
#               "Você acredita que a internet atrapalha em sua formação?","Você considera as redes sociais um ambiente tóxico?",
#               "Você utiliza a internet para fazer download de conteúdo?"]
# perguntas_s_n_labels_vet = ['Para trabalho','Converça com amigos','Conversa com estranhos','Usa email','Pesquisas academicas',
#                             'Ver noticias','Compras','Ver vidios','Jogar','Atraplahar formação','Redes sociais toxicas',
#                             'Download de conteudo']
# #criando blocos
# block_size = 3
# # pergunta_pergunta_label = zip(perguntas_s_n_labels_vet,perguntas_s_n_vet)
# # bloco_atual = 0
# # contador = 0
# # for item in pergunta_pergunta_label:
# #     blocos[bloco_atual].append(item)
# #     contador +=1
# #     if(contador == block_size):
# #         bloco_atual = 0
# #         contador = 0
# print([ 
#             [ [nmumero for nmumero in range(n*3,(n+1)*3)]
#             ] for n in range(int(len(perguntas_s_n_vet)/block_size)) 
#         ])
# blocos = [ 
#             [ (pergunta,label) for pergunta,label in zip(perguntas_s_n_vet[n*block_size:(n+1)*block_size],
#                                                          perguntas_s_n_labels_vet[n*block_size:(n+1)*block_size]) 
#             ] for n in range(int(len(perguntas_s_n_vet)/block_size)) 
#         ]
# print(blocos)
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


# # for i in range(len(resp)):
# #     plt.stairs(A[i+1], baseline=A[i], fill=True)


# t = a["Em geral, quanto tempo você permanece conectado à intenet diariamente?"]
# y = t.value_counts().sort_index()
# y.plot(kind='pie', autopct='%.2f',ylabel='',title='Distribuição em pocentagem do tempo de uso' 
#                                    , labels=y.index, fontsize=10)
# plt.savefig('Tempo de uso diario da intenet')

# t = a["Qual dispositivo você mais utiliza?"]
# y = t.value_counts().sort_index()
# y.plot(kind='pie', autopct='%.2f', labels=y.index, fontsize=10)
# plt.show()
# plt.savefig('dispositimo mais ussado')
# plt.close("all")

# print(a['Renda familiar'].count())
# # #grafico de idade 
# a["Sexo"].value_counts().sort_index().plot(kind='pie', autopct='%.2f', labels=["Masculino","Feminino"], fontsize=10)
# plt.show()
# plt.close("all")
# b = a["Cursando semestre:"]
# print(b.mean(),b.median())
# print(b.value_counts())
# print(b.std(),b.var())


# # # ajustando dados de renda familiar para voltar para categorias em string
# b = a['Renda familiar']
# for n,c in enumerate(b):
#     a['Renda familiar'].iloc[n] = "Até 1 salário mínimo" if c == 1 else "De 1 a 3 salários mínimos" if c==2 else "De 3 a 5 salários mínimos" if c==3 else "De 5 a 7 salários mínimos" if c == 4 else "7+ salários mínimos" if c == 5 else "Não Respondeu"
# a['Renda familiar'] = b

# def f(r,t,k):
#     return [ f if  k == e else np.NaN for e,f in zip(r.values,t.values) ]
