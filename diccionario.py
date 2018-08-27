diccionario = {
    1: [{ "num1" : 1 }],
    2: [{ "Letra1" : "A" }],
    3: [{
        "data1" : 1,
        "data2" : 2,
        "data3": 3,
        "data4" : ["a","b","c","d",("tup1", "tup2")]
    }]
}

print(diccionario[3][0]["data4"][4][0])
