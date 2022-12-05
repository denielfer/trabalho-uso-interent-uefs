from matplotlib_venn import venn3_unweighted
from matplotlib import pyplot as plt
import pandas as pd
from time import perf_counter

#tempo sem multthreading com print:53.48859600000287  s
#tempo sem multthreading sem print:53.18989919999876  s
#tempo com multthreading com print:2.1584835999965435 s
#tempo com multthreading sem print:2.1706609000029857 s
def perg(name,labels,respostas_dataframe):
    v = [True,False]
    resp = {q:{ q:{ q:0 for q in v} for q in v } for q in v }
    print(name,' - ',labels)
    for n in range(respostas_dataframe.last_valid_index()+1):
        t,y,z = respostas_dataframe.iloc[n]
        resp.setdefault(t,{})
        resp[t].setdefault(y,{})
        resp[t][y].setdefault(z,0)
        resp[t][y][z]+=1
    # print()
    # print(pd.DataFrame(resp))
    # print(b.sum())
    #fazendo dragama de ven
    venn3_unweighted(subsets=(resp[True][False][False],resp[False][True][False],resp[True][True][False],
        resp[False][False][True],resp[True][False][True],resp[False][True][True],
        resp[True][True][True]),set_labels = labels)
    #salvando plot
    plt.savefig('venn//'+name)
    plt.close("all")
def main(file = "Planilha sem título - Página1.csv"):
    #lendo dados
    respostas_dataframe = pd.read_csv(file)
    #selecionando pergutnas
    perguntas_s_n_vet = ["Você utiliza a internet para trabalho?","Você utiliza a internet para conversar com amigos?",
                "Você utiliza a internet para conversar com desconhecidos?","Você utiliza e-mail?",
                "Você utiliza a internet para realizar Pesquisas Acadêmicas?","Você utiliza a internet para acessar noticias?",
                "Você faz compras online?","Você assiste vídeos online?","Você utiliza a internet para participar de jogos online?",
                "Você acredita que a internet atrapalha em sua formação?","Você considera as redes sociais um ambiente tóxico?",
                "Você utiliza a internet para fazer download de conteúdo?"]
    #filtrando data frame para ter valores True ou False ao invez de 'Sim' e 'Não'
    for a in perguntas_s_n_vet:
        respostas_dataframe[a] = respostas_dataframe[a].apply(lambda x: x == 'Sim')

    from concurrent.futures import ProcessPoolExecutor


    #criando poll de thread
    with ProcessPoolExecutor() as executor:
        for n,q in enumerate(perguntas_s_n_vet[:-2]):
            for i,w in enumerate(perguntas_s_n_vet[n+1:-1]):
                for j,e in enumerate(perguntas_s_n_vet[n+i+1:]):
                    executor.submit(perg, name= f'{n+14}_{n+i+15}_{n+i+j+15}',labels=(f'Pergunta {n+14}',f'Pergunta {n+i+15}',f'Pergunta {n+i+j+15}'),respostas_dataframe=respostas_dataframe[[q,w,e]])

if __name__ == '__main__':
    t1 = perf_counter()
    main()
    print(perf_counter() - t1)
