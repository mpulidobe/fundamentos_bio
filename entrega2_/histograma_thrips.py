import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./datos/datosThrips.tsv', sep='\t')

sns.histplot(data=df,
             bins=6,
             x='Length (bp)',
             kde=True,
             color='blue')
plt.title('Distribución de longitud génica en T. tabaci')
plt.xlabel('Longitud (pb)')
plt.ylabel('Frecuencia')
plt.savefig('histograma_thrips.png', dpi=300)
plt.show()

