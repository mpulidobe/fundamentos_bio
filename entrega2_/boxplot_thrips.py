import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./datos/datosThrips.tsv', sep='\t')

sns.boxplot(data=df,
            color='green',
            x='Gene Type',
            y='Length (bp)',
            fill=False)
plt.title('Diferencia de longitud para cada tipo de gen')
plt.show()