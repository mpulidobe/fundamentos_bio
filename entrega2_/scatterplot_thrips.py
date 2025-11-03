import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./datos/datosThrips.tsv', sep='\t')

sns.scatterplot(data=df,
                x='Length (bp)',
                y='Intergenic Space',
                hue='Gene Type')
plt.title('Diagrama de dispersión del espacio intergénico')
plt.show()

print(df.columns)