import pandas as pd
import seaborn as sns

df = pd.read_csv('ATV_2_Exercicios_Visualizacao_de_Dados\\atv3\\pessoas.csv')

def relacao():
    plt = sns.lineplot(data = df, x = df['peso'], y = df['altura']).get_figure()
    #plt.savefig('ATV_2_Exercicios_Visualizacao_de_Dados\\atv3\\relacaoPesoXAltura.png')

def dispercao():
    plt2 = sns.scatterplot(data = df, x = df['peso'], y = df['altura']).get_figure()
    #plt2.savefig('ATV_2_Exercicios_Visualizacao_de_Dados\\atv3\\dispercaoPesoXAltura.png')

relacao()
dispercao()
