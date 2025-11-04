import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./datos/datosThrips.tsv', sep='\t')

sns.boxplot(data=df,
            x='Gene Type',
            y='Length (bp)',
            hue='Gene Type',
            palette='Set1',
            fill=False)
plt.title('Distribución de longitudes según el tipo de gen')
plt.xlabel('Tipo de gen')
plt.ylabel('Longitud (pb)')
plt.tight_layout()
plt.savefig('boxplot_thrips.png', dpi=300, bbox_inches='tight')
plt.show()