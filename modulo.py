diccionario = {
  "pares": [],
  "impares": []
}


for x in range(1,100001):
  if x%2==0:
    diccionario["pares"].append(x)
  else:
    diccionario["impares"].append(x)

print("impares")
print(diccionario["impares"])
print("pares")
print(diccionario["pares"])
