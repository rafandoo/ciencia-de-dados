import pandas as pd
import seaborn as sns

df = pd.read_csv('ATV_2_Exercicios_Visualizacao_de_Dados\\atv4\\pessoas.csv')
fem = df[df.sexo == 'F']

def relacao():
    plt = sns.lineplot(data = fem, x = fem['peso'], y = fem['altura']).get_figure()
    #plt.savefig('ATV_2_Exercicios_Visualizacao_de_Dados\\atv4\\relacaoPesoXAltura.png')

def dispercao():
    plt2 = sns.scatterplot(data = fem, x = fem['peso'], y = fem['altura']).get_figure()
    #plt2.savefig('ATV_2_Exercicios_Visualizacao_de_Dados\\atv4\\dispercaoPesoXAltura.png')

relacao()
dispercao()
