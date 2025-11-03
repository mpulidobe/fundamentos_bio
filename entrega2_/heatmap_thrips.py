import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./datos/datosThrips.tsv', sep='\t')
tabla = pd.crosstab(df["Gene Name"], df["Codon Start"])

sns.heatmap(tabla,
            cmap='Greens',
            cbar=True)
plt.title("Relación entre genes y codones de inicio en T. tabaci")
plt.xlabel("Codón de inicio")
plt.ylabel("Gen")
plt.show()