from urllib.parse import urlencode
from urllib.request import Request, urlopen

def unescapeXml(s):
    s = s.replace("&lt;","<")
    s = s.replace("&gt;",">")
    s = s.replace("&amp;","&")
    s = s.replace("&nbsp;"," ")
    return s
def unescapeString(s):
    s = s.replace("\\r",'')
    s = s.replace("\\t",'')
    s = s.replace("\\n",'')
    return s

def unescapeTable(s):
    s = s.replace("</tr>",'')
    s = s.replace("<tr>",'')
    s = s.replace("<table>",'')
    return s
def buscarComponente(s):
    posicaoInicio = int(s.index('>'))
    s = s[posicaoInicio + 1: ]
    return s


url = "http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm"

cep = input("Digite o cep:\n")
cep = cep.replace("-",'')
post_fields = {'relaxation':cep,'tipoCep':'ALL','semelhante':'N'}

request = Request(url, urlencode(post_fields).encode())
result = urlopen(request).read()
result = str(result)
#print(type(result))

result = unescapeString(result)
#result = bytes(result,"iso-8859-1").decode("unicode_escape")
result = unescapeXml(result)

try:
    find = 'CEP:</th>'
    posicao = int(result.index(find) + len(find))
    result = result[posicao : posicao + 200]

    findFim = '</table>'
    posicaoFim = int(result.index(findFim))
    result = result[ : posicaoFim]

    result = unescapeTable(result)
    result = result.split('</td>')

    Logradouro = buscarComponente(result[0])
    Bairro = buscarComponente(result[1])
    Cidade = buscarComponente(result[2])
    Cep = buscarComponente(result[3])

    print ("Logradouro: {0}".format(Logradouro))
    print ("Bairro: {0}".format(Bairro))
    print ("Cidade: {0}".format(Cidade))
    print ("Cep: {0}".format(Cep))
except:
    print("CEP não encontrado")




#findInicio = '<td width="150">'
#findFim = '</td><td>'
#posicaoInicio = int(result.index(findInicio) + len(findInicio))
#posicaoFim = int(result.index(findFim))
#Logradouro = result[posicaoInicio : posicaoFim]
#result = result[posicaoFim + len(findFim): ]

#findFim = '</td><td>'
#posicaoInicio = int(result.index(findInicio) + len(findInicio))
#posicaoFim = int(result.index(findFim))
#Bairro = result[ : posicaoFim]
#result = result[posicaoFim + len(findFim): ]



