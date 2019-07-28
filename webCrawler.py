from urllib.request import Request, urlopen


req = Request('https://www.melhorcambio.com/dolar-hoje', headers={'User-Agent': 'Mozilla/5.0'})
content = urlopen(req).read()
content = str(content)
find = '<input type="hidden" value="'
posicao = int(content.index(find) + len(find))
dolar = content[ posicao : posicao  + 4]

req = Request('https://www.melhorcambio.com/euro-hoje', headers={'User-Agent': 'Mozilla/5.0'})
content = urlopen(req).read()
content = str(content)
posicao = int(content.index(find) + len(find))
euro = content[ posicao : posicao  + 4]


req = Request('https://www.climatempo.com.br/previsao-do-tempo/cidade/271/curitiba-pr', headers={'User-Agent': 'Mozilla/5.0'})
content = urlopen(req).read()
content = str(content)
find = 'tempMax0">'
posicao = int(content.index(find) + len(find))
maxima = content[ posicao : posicao  + 2]
find = 'tempMin0">'
posicao = int(content.index(find) + len(find))
minima = content[ posicao : posicao  + 2]


print("Dolar: " + dolar)
print("Euro: " + euro)
print("Temp. Maxima: " + maxima)
print("Temp. Minima: " + minima)
