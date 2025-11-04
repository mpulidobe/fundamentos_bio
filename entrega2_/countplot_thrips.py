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
plt.savefig('countplot_thrips.png', dpi=300, bbox_inches='tight')
plt.show()