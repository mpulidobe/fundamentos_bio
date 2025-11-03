import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./datos/datosThrips.tsv', sep='\t')

sns.scatterplot(data=df,
                x=df.index,
                y='Intergenic Space')
plt.title('Diagrama de dispersión del espacio intergénico')
plt.show()