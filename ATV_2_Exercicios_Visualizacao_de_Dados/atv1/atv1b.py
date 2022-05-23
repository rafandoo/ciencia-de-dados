import pandas as pd
import seaborn as sns

df = pd.read_csv('ATV_2_Exercicios_Visualizacao_de_Dados\\atv1\matriculas.csv')

plt = sns.scatterplot(data = df, x = df['ano'], y = df['evasaoEscolar']).get_figure()
plt.savefig('dispersaoEvasaoPorAno.png')

"""Por meio da analise do grafico podemos constatar que há uma grande dispersão dos dados analisados
"""