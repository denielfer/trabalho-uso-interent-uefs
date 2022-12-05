from matplotlib_venn import venn3_unweighted
from matplotlib import pyplot as plt
import pandas as pd
from time import perf_counter

#tempo sem multthreading com print:53.48859600000287  s
#tempo sem multthreading sem print:53.18989919999876  s
#tempo com multthreading com print:2.1584835999965435 s
#tempo com multthreading sem print:2.1706609000029857 s
#usar a de baixo para usar respostas_dataframe compartilhado entre todas as thread para ganho de performace
# def perg(coll,name,labels,respostas_dataframe):
def perg(coll,name,labels):
    print(name,coll)
    b = respostas_dataframe[coll].apply(lambda x: x == 'Sim')
    # print(b)
    v = [True,False]
    resp = {q:{ q:{ q:0 for q in v} for q in v } for q in v }
    # print(b.columns)
    for n in range(b.last_valid_index()+1):
        t,y,z = b.iloc[n]
        resp.setdefault(t,{})
        resp[t].setdefault(y,{})
        resp[t][y].setdefault(z,0)
        resp[t][y][z]+=1
    # print()
    # print(pd.DataFrame(resp))
    # print(b.sum())
    venn3_unweighted(subsets=(resp[True][False][False],resp[False][True][False],resp[True][True][False],
        resp[False][False][True],resp[True][False][True],resp[False][True][True],
        resp[True][True][True]),set_labels = labels)
    plt.savefig('venn//'+name)
    plt.close("all")
def main():
    respostas_dataframe = pd.read_csv("Planilha sem título - Página1.csv")
    perguntas_s_n_vet = ["Você utiliza a internet para trabalho?","Você utiliza a internet para conversar com amigos?",
                "Você utiliza a internet para conversar com desconhecidos?","Você utiliza e-mail?",
                "Você utiliza a internet para realizar Pesquisas Acadêmicas?","Você utiliza a internet para acessar noticias?",
                "Você faz compras online?","Você assiste vídeos online?","Você utiliza a internet para participar de jogos online?",
                "Você acredita que a internet atrapalha em sua formação?","Você considera as redes sociais um ambiente tóxico?",
                "Você utiliza a internet para fazer download de conteúdo?"]

    from concurrent.futures import ProcessPoolExecutor

    with ProcessPoolExecutor() as executor:
        for n,q in enumerate(perguntas_s_n_vet):
            for i,w in enumerate(perguntas_s_n_vet[n+1:]):
                for j,e in enumerate(perguntas_s_n_vet[i+2:]):
                    executor.submit(perg,[q,w,e], name= f'{n+14}_{i+15}_{j+16}',labels=(f'Pergunta {n+14}',f'Pergunta {i+15}',f'Pergunta {j+16}'))
                    # esssa versao abaixo demora mais tempo uma vez que o dataframe esta sendo copiado e mandado pra cada thread, enquanto na de cima o datrame usado é compartilhado por todas as thread
                    # executor.submit(perg,[q,w,e], name= f'{n+14}_{i+15}_{j+16}',labels=(f'Pergunta {n+14}',f'Pergunta {i+15}',f'Pergunta {j+16}'),respostas_dataframe=respostas_dataframe)

if __name__ == '__main__':
    t1 = perf_counter()
    main()
    print(perf_counter() - t1)
