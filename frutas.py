#%%

import pandas as pd

df = pd.read_excel("dados_frutas.xlsx")




# %%

from sklearn import tree

arvore = tree.DecisionTreeClassifier(random_state=42)
# %%

y = df['Fruta']

caracteristicas = ['Arredondada','Suculenta', 'Vermelha','Doce']

X = df[caracteristicas]

# %%
arvore.fit(X,y)
# %%
arvore.predict([[0,1,0,0]])
# %%

