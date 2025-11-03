import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./datos/datosThrips.tsv', sep='\t')

sns.countplot(data=df,
              x='Strand',
              palette=sns.color_palette('colorblind'))
plt.title('Frecuencia de genes en cada hebra')
plt.xlabel('Hebra')
plt.ylabel('Frecuencia')
plt.show()