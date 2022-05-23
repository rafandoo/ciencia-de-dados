import matplotlib.pyplot as plt
import pandas as pd
import statistics as st
import numpy as np

df = pd.read_csv('ATV_2_Exercicios_Visualizacao_de_Dados\\atv2\\temperaturas.csv')
minima = df['minima']
maxima = df['maxima']

def indicadores(list):
    q1 = np.percentile(list, 25)
    q3 = np.percentile(list, 75)
    mediana = st.median(list)
    minimo = q1 - 1.5 * (q3 - q1)
    maximo = q3 + 1.5 * (q3 - q1)
    
    return (
        '1° Quartil: {:.2f}\n'+
        '3° Quartil: {:.2f}\n'+
        'Mediana:    {:.2f}\n'+
        'Minimo:     {:.2f}\n'+
        'Maximo:     {:.2f}\n').format(q1, q3, mediana, minimo, maximo)

def boxPlotMinima(minima):
    plt.title('Temperaturas minimas')
    plt.boxplot(minima)

    print('Inidicadores - Temperatura minima\n' + indicadores(minima))
    plt.show()
    plt.close()
    
def boxPlotMaxima(maxima):
    plt.title('Temperaturas maximas')
    plt.boxplot(maxima)

    print('Inidicadores - Temperatura maxima\n' + indicadores(maxima))
    plt.show()
    plt.close()

boxPlotMinima(minima)
boxPlotMaxima(maxima)
