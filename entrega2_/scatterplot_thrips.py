import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./datos/datosThrips.tsv', sep='\t')

sns.scatterplot(data=df,
                x='Length (bp)',
                y='Intergenic Space',
                hue='Gene Type')
plt.title('Longitud y espacio intergénico por tipo de gen')
plt.xlabel('Longitud (pb)')
plt.ylabel('Espacio intergenico')
plt.legend(title='Tipo de gen')
plt.savefig('diagrama_thrips.png', dpi=300)
plt.show()

print(df.columns)