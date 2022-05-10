from turtle import color
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ATV_2_Exercicios_Visualizacao_de_Dados\\atv1\matriculas.csv')

def anoXmatriculas():
    plt.title('Ano x Matriculas')
    plt.xlabel('ano')
    plt.ylabel('matriculas')
    plt.bar(df['ano'], df['matriculas'], color='blue')
    
    plt.show()
    plt.close()

def anoXEvasao():
    plt.title('Ano x Evasao Escolar')
    plt.xlabel('ano')
    plt.ylabel('evasao escolar')
    plt.bar(df['ano'], df['evasaoEscolar'], color='blue')
    
    plt.show()
    plt.close()
       
anoXmatriculas()
anoXEvasao()
