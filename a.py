import pandas as pd, numpy as np
import matplotlib.pyplot as plt

#H:\materias\probabilidade

# lendo planilha
a = pd.read_csv("Planilha sem título - Página1.csv")

# #grafico de idade dos intrevistados por sexo
# a.plot.hist(column=["Idade:"], by="Sexo", figsize=(10, 8))
# plt.show()
# plt.close("all")


# #grafico de quantidade de intervistados por sexo
# a['Sexo'].value_counts().plot.barh()
# plt.show()
# plt.close("all")


# # ajustando dados de renda familiar para voltar para categorias em string
b = a['Renda familiar']
for n,c in enumerate(b):
    a['Renda familiar'].iloc[n] = "Até 1 salário mínimo" if c == 1 else "De 1 a 3 salários mínimos" if c==2 else "De 3 a 5 salários mínimos" if c==3 else "De 5 a 7 salários mínimos" if c == 4 else "7+ salários mínimos" if c == 5 else "Não Respondeu"
a['Renda familiar'] = b
# print(a['Renda familiar'])


# # grafico de quantidade de intrevistado por categoria em renda familiar
# a['Renda familiar'].value_counts().plot.barh()
# plt.show()
# plt.close("all")


# grafico de intrevistados por turno estudado
# a["Qual o turno do seu curso?"].value_counts().plot.barh()
# plt.show()
# plt.close("all")


#função que retorna o valores de t qando r == k ou NaN
def f(r,t,k):
    return [ f if  k == e else np.NaN for e,f in zip(r.values,t.values) ]

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


# # plot da qtd de intrevistados por semestre
# a['Cursando semestre:'].value_counts().sort_index().plot.bar()
# plt.show()
# plt.close("all")


# #grafico de pizza de dsipositivo mais usado
# a['Qual dispositivo você mais utiliza?'].value_counts().sort_index().plot.pie()
# plt.show()
# plt.close("all")


# grafico de pizza de tempo de uso diario de internet
a["Em geral, quanto tempo você permanece conectado à intenet diariamente?"].value_counts().sort_index().plot.bar()
plt.ylabel('Tempo de uso da intenet diario')
plt.show()
plt.close("all")