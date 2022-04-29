import pandas as pd
import numpy as np

combustiveis = pd.read_csv('COMBUSTÍVEIS.csv')


gasolina = combustiveis[combustiveis.combustivel == 'gasolina']
gasolinaA = gasolina[gasolina.cidade == 'A']
gasolinaB = gasolina[gasolina.cidade == 'B']
gasolinaC = gasolina[gasolina.cidade == 'C']

diesel = combustiveis[combustiveis.combustivel == 'diesel']
dieselA = diesel[diesel.cidade == 'A']
dieselB = diesel[diesel.cidade == 'B']
dieselC = diesel[diesel.cidade == 'C']

etanol = combustiveis[combustiveis.combustivel == 'etanol']
etanolA = etanol[etanol.cidade == 'A']
etanolB = etanol[etanol.cidade == 'B']
etanolC = etanol[etanol.cidade == 'C']


gA = [gasolinaA.at[0, 'preco1'], gasolinaA.at[0, 'preco2'], gasolinaA.at[0, 'preco3'], gasolinaA.at[0, 'preco4'], gasolinaA.at[0, 'preco5']]
gB = [gasolinaB.at[3, 'preco1'], gasolinaB.at[3, 'preco2'], gasolinaB.at[3, 'preco3'], gasolinaB.at[3, 'preco4'], gasolinaB.at[3, 'preco5']]
gC = [gasolinaC.at[6, 'preco1'], gasolinaC.at[6, 'preco2'], gasolinaC.at[6, 'preco3'], gasolinaC.at[6, 'preco4'], gasolinaC.at[6, 'preco5']]

print('Variancia gasolina cidade A: {:.3f}'.format(np.var(gA)))
print('Desvio padrão gasolina cidade A: {:.3f}'.format(np.std(gA)))
print('Variancia gasolina cidade B: {:.3f}'.format(np.var(gB)))
print('Desvio padrão gasolina cidade B: {:.3f}'.format(np.std(gB)))
print('Variancia gasolina cidade C: {:.3f}'.format(np.var(gC)))
print('Desvio padrão gasolina cidade C: {:.3f}'.format(np.std(gC)))

print('\n\n\n')

dA = [dieselA.at[2, 'preco1'], dieselA.at[2, 'preco2'], dieselA.at[2, 'preco3'], dieselA.at[2, 'preco4'], dieselA.at[2, 'preco5']]
dB = [dieselB.at[5, 'preco1'], dieselB.at[5, 'preco2'], dieselB.at[5, 'preco3'], dieselB.at[5, 'preco4'], dieselB.at[5, 'preco5']]
dC = [dieselC.at[7, 'preco1'], dieselC.at[7, 'preco2'], dieselC.at[7, 'preco3'], dieselC.at[7, 'preco4'], dieselC.at[7, 'preco5']]

print('Variancia diesel cidade A: {:.3f}'.format(np.var(dA)))
print('Desvio padrão diesel cidade A: {:.3f}'.format(np.std(dA)))
print('Variancia diesel cidade B: {:.3f}'.format(np.var(dB)))
print('Desvio padrão diesel cidade B: {:.3f}'.format(np.std(dB)))
print('Variancia diesel cidade C: {:.3f}'.format(np.var(dC)))
print('Desvio padrão diesel cidade C: {:.3f}'.format(np.std(dC)))

print('\n\n\n')

eA = [etanolA.at[1, 'preco1'], etanolA.at[1, 'preco2'], etanolA.at[1, 'preco3'], etanolA.at[1, 'preco4'], etanolA.at[1, 'preco5']]
eB = [etanolB.at[4, 'preco1'], etanolB.at[4, 'preco2'], etanolB.at[4, 'preco3'], etanolB.at[4, 'preco4'], etanolB.at[4, 'preco5']]
eC = [etanolC.at[8, 'preco1'], etanolC.at[8, 'preco2'], etanolC.at[8, 'preco3'], etanolC.at[8, 'preco4'], etanolC.at[8, 'preco5']]

print('Variancia diesel cidade A: {:.3f}'.format(np.var(eA)))
print('Desvio padrão diesel cidade A: {:.3f}'.format(np.std(eA)))
print('Variancia diesel cidade B: {:.3f}'.format(np.var(eB)))
print('Desvio padrão diesel cidade B: {:.3f}'.format(np.std(eB)))
print('Variancia diesel cidade C: {:.3f}'.format(np.var(eC)))
print('Desvio padrão diesel cidade C: {:.3f}'.format(np.std(eC)))




print('\n\n\n')
print(combustiveis)