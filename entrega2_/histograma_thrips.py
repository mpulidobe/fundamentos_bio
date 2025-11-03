import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./datos/datosThrips.tsv', sep='\t')
sns.histplot(data=df,
             x='Length (bp)',
             kde=True,
             color='b')
plt.title('Distribución de longitud génica en T. tabaci')
plt.show()

