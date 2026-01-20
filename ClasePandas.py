import pandas as pd

serie = pd.Series([10,20,30,40])
#print(serie)

s= pd.Series([10,20,30,40,50], index=["a","b","c","d","e"])
#print(s)

#print(s[["b","c"]])

#print(s.iloc[1:4])

#print(s["b":"d"])

#print(s(s>35))

#OPERACIONES ARÍTMETICAS
serie_doble=serie*2
print(serie_doble)

serie_cuadrado=serie**2
print(serie_cuadrado)


#OPERACIONES CON SERIES
serie