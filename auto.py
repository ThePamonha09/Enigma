from funçoes import convert

list = ["yipenwoftqrlzjabmcxvkhgsud"]

n=0
i = 0
while (n<25):
    x = list[i]
    x = x + x[0]
    x = x[:0] +  x[1:] 
    list.append(x)
    i += 1
    n += 1

codigo = input("digite o código: ")
print (convert(codigo))

