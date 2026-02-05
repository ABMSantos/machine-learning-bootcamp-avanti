import pandas as pd

def numeros_impares(lista):
    resultado = []

    for numero in lista:
        if numero % 2 != 0:
            resultado.append(numero)

    return resultado


print(numeros_impares([1, 2, 3, 4, 5, 6]))

def numeros_primos(lista):
    primos = []

    for numero in lista:
        if numero > 1:
            eh_primo = True

            for i in range(2, numero):
                if numero % i == 0:
                    eh_primo = False

            if eh_primo:
                primos.append(numero)

    return primos


print(numeros_primos([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def elementos_unicos(lista1, lista2):
    resultado = []

    for item in lista1:
        if item not in lista2:
            resultado.append(item)

    for item in lista2:
        if item not in lista1:
            resultado.append(item)

    return resultado


print(elementos_unicos([1, 2, 3], [3, 4, 5]))

def segundo_maior(lista):
    lista.sort()
    return lista[-2]

print(segundo_maior([10, 20, 30, 40]))

def ordenar_por_nome(pessoas):
    pessoas.sort()
    return pessoas


pessoas = [("Ana", 27), ("Carlos", 30), ("Beatriz", 25)]
print(ordenar_por_nome(pessoas))

dados = {
    "nome": ["Ana", "Carlos", "Beatriz", "Daniel"],
    "idade": [27, 35, None, 40]
}

df = pd.DataFrame(dados)

print("\nDataFrame:")
print(df)

media = df["idade"].mean()
desvio = df["idade"].std()

outliers = df[(df["idade"] > media + desvio) | (df["idade"] < media - desvio)]

print("\nOutliers:")
print(outliers)

df2 = pd.DataFrame({"cidade": ["RP", "SP", "RJ", "BH"]})

df_final = pd.concat([df, df2], axis=1)

print("\nConcatenado:")
print(df_final)

# df_csv = pd.read_csv("arquivo.csv")
# print(df_csv.head())

print("\nColuna idade:")
print(df["idade"])

print("\nIdade maior que 30:")
print(df[df["idade"] > 30])

df["idade"] = df["idade"].fillna(media)

print("\nApós preencher valores vazios:")
print(df)
