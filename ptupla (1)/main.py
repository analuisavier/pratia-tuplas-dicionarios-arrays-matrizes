import numpy as np
import datetime

def separador(questao):
    print('\n' + '='*30)
    print(f'Questão {questao}')
    
def format():
    print(f"{'='*30}")

# Parte 1: Tuplas
# 1.1 Crie uma tupla para armazenar os códigos de cor RGB (Vermelho, Verde, Azul), usando os valores 255 para vermelho, 102 para verde e 0 para azul.

separador('1.1')
cor = (255, 102, 0)
print(f"Cores RGB: {cor}")
format()

# 1.2 Crie uma tupla para as coordenadas geográficas, usando -8.0578 para latitude e -34.8829 para longitude.

separador('1.2')
coordenada_geografica = (-8.0578, -34.8829)
print(f"Coordenadas geográficas: {coordenada_geografica}")
format()

# 1.3 Crie uma tupla para armazenar as informações básicas e imutáveis de um usuário, contendo o ID 101, o username 'ana_silva' e a data de criação '2023-01-15'.

separador('1.3')
usuario = (101, 'ana_silva', '2023-01-15')
print(f"Usuário: {usuario}")
format()

# 1.4 Dada a tupla de cores RGB (255, 102, 0), acesse e imprima o valor do componente 'Verde' (o segundo elemento, de índice 1).

separador('1.4')
r, g, b = cor
print(g)
format()

# 1.5 Dada a tupla de coordenadas (-8.0578, -34.8829), desempacote-a em duas variáveis separadas chamadas latitude e longitude.

separador('1.5')
latitude = coordenada_geografica[0]
longitude = coordenada_geografica[1]

print(f"latitude: {latitude}\nlongitude {longitude}")
format()

# 1.6 A partir da tupla de usuário (205, 'Carlos Pereira', 'carlos.p@email.com'), que representa (id, nome, email), desempacote-a em variáveis e use a variável do nome para imprimir uma saudação.

separador('1.6')
usuario = (205, 'Carlos Pereira', 'carlos.p@email.com')

id, nome, email = usuario
print(f"Olá, {nome} saudações!")
format()

# 1.7 Dada a tupla de papéis de administrador ('moderador', 'editor', 'sysadmin'), itere sobre ela e imprima cada papel.

separador('1.7')
administrador = ('moderador', 'editor', 'sysadmin')

for papel in administrador:
    print(papel)
format()

# 1.8 Dada a tupla dados dos usuários acima, itere sobre elas e imprima cada dado.

separador('1.8')
for dado in usuario:
    print(dado)
format()    

# 1.9 Dada a tupla de cores RGB acima, itere sobre ela e imprima cada parte da cor, R, G e B.

separador('1.9')
for rgb in cor:
    print(f"RGB: {rgb}")
format()

# 1.10 Escreva uma função que verifique se um papel de usuário existe em uma tupla de papéis de administrador ('moderador', 'editor', 'sysadmin'). Teste a função com os papéis 'editor' e 'usuario_comum'.

separador('1.10')
def admin(papel):
    resultado = False
    administrador = ('moderador', 'editor', 'sysadmin')
    for admin in administrador:
        if papel == admin:
            resultado = True

    return resultado

print (f"Editor é administrador? {admin('editor')}")
print (f"Usuário é administrador? {admin('usuario')}")
format()

# 1.11 Dada a tupla de atribuições das pessoas de um equipe ('editor', 'leitor', 'editor', 'comentarista', 'editor'), escreva uma função que conta o número de vezes em que um papel aparece, teste a função com os papíes 'editor', 'comentarista' e 'tradutor'.

separador('1.11')
def contador(papel):
    equipe = ('editor', 'leitor', 'editor', 'comentarista', 'editor')
    
    x = 0
    for i in equipe:
        if i == papel:
            x+=1
    return x

print(f"Editor: {contador('editor')}")
format()

# Parte 2: Dicionários
# 2.1 Crie um dicionário para um usuário. Use a chave 'username' para o valor 'bia_costa', a chave 'email' para 'bia.costa@email.com', e a chave 'data_adesao' para '2024-05-21'.

separador('2.1')
usuario = {
    'username': 'bia_costa',
    'email':'bia.costa@email.com',
    'data_adesao': '2024-05-21'
}
print(usuario)
format()

# 2.2 Crie um dicionário para um produto. Use as chaves 'id_produto', 'nome', 'preco' e 'estoque' com os respectivos valores 'XYZ-001', 'Fone de Ouvido Sem Fio', 299.90 e 150.

separador('2.2')
produto = {
    'id_produto': 'XYZ-001',
    'nome': 'Fone de Ouvido Sem Fio',
    'preco': 299.90,
    'estoque': 150
}
print(produto)
format()

# 2.3 Crie um dicionário vazio chamado preferencias_usuario.

separador('2.3')
preferencias_usuario = {}
print(preferencias_usuario)
format()

# 2.4 Dado o dicionário de produto {'id_produto': 'XYZ-001', 'nome': 'Fone de Ouvido Sem Fio', 'preco': 299.90, 'estoque': 150}, acesse e imprima o preço original. Em seguida, atualize o preço para o valor promocional de 249.99.

separador('2.4')
print(f'Preço original: R${produto["preco"]}')
produto['preco'] = 249.99
print(f'Preço promocional: R${produto["preco"]}')
format()

# 2.5 Dado o perfil de usuário {'username': 'bia_costa', 'email': 'bia.costa@email.com', 'data_adesao': '2024-05-21'}, adicione uma nova informação: a chave 'telefone' com o valor '98765-4321'.

separador('2.5')
perfil_usuario =  {'username': 'bia_costa', 'email': 'bia.costa@email.com', 'data_adesao': '2024-05-21'}
print(f"Perfil de usuário: {perfil_usuario}")
perfil_usuario['telefone'] = '98765-4321'
print(f"Perfil de usuário atualizado: {perfil_usuario}")
format()

# 2.6 Dado o perfil de usuário {'username': 'bia_costa'}, use o método .get() para tentar acessar o valor da chave 'ultimo_login'. Como a chave não existe, forneça o valor padrão 'Nunca logou'. Após a tentativa, bia fez o login, então atualize o dicionário para incluir a chave 'ultimo_login' com o valor '2024-05-22'.

separador('2.6')
perfil_usuario = {'username': 'bia_costa'}
ultimo_login = perfil_usuario.get('ultimo_login', 'Nunca logou')
print(f"Último login: {ultimo_login}")
perfil_usuario['ultimo_login'] = '2024-05-22'
print(f"Perfil de usuário atualizado com último login: {perfil_usuario}")
format()

# 2.7 Dado o perfil de usuário {'username': 'bia_costa', 'email': 'bia.costa@email.com', 'telefone_fixo': '3265-4321'}, use a instrução del ou a função pop() para remover a chave 'telefone_fixo'.

separador('2.7')
usuario = {'username':'bia_costa','email':'bia.costa@email.com','telefone_fixo':'3265-4321'}
print(f"Antes da remoção: {usuario}")
del usuario['telefone_fixo']
print(f"Depois da remoção: {usuario}")
format()

# 2.8 Dado o catálogo de produtos {'XYZ-001': 'Fone de Ouvido Sem Fio', 'ABC-002': 'Teclado Mecânico'}, use a instrução o método .pop() para remover o produto com a chave 'XYZ-001'. Armazene o valor retornado (o nome do produto) e imprima uma mensagem de confirmação.

separador('2.8')
catalago_produtos = {'XYZ-001':'Fone de Ouvido Sem Fio', 'ABC-002': 'Teclado Mecânico'}
print(f"Catálogo antes da remoção: {catalago_produtos}")
produto_removido = catalago_produtos.pop('XYZ-001')
print(f"Produto removido: {produto_removido}")
print(f"Catálogo depois da remoção: {catalago_produtos}")
format()

# 2.9 Dado o perfil de usuário {'username': 'bia_costa'}, tente remover a chave 'email' usando o método .pop(). Forneça o valor padrão 'Email não encontrado.' para evitar um erro.

separador('2.9')
usuario = {'username': 'bia_costa'}
print(f"Usuario: {usuario}")
remover_email = usuario.pop('email','Email não encontrado.')
print(remover_email)
format()

# 2.10 Dado o catálogo de produtos {'Fone de Ouvido': 249.99, 'Teclado Mecânico': 450.00, 'Mouse Gamer': 120.50}, itere sobre seus itens e imprima o nome e o preço de cada um no formato 'Nome: R$Preço'.

separador('2.10')
catalago_produtos = {'Fone de Ouvido': 249.99, 'Teclado Mecânico': 450.00, 'Mouse Gamer': 120.50}
print("Catálogo de produtos: ")
for produto in catalago_produtos:
    print(f"{produto}: R${catalago_produtos[produto]}")
format()    

# 2.11 Dado a lista de compras da feira {'Tapioca': 18.99, 'Queijo Manteiga': 45.00, 'Ovos': 23.50}, itere sobre seus itens e imprima o nome e o preço de cada um no formato 'Nome: R$Preço' e depois imprima o total.

separador('2.11')
lista_compras = {'Tapioca': 18.99, 'Queijo Manteiga': 45.00, 'Ovos': 23.50}
total = 0

for nome, preco in lista_compras.items():
    print(f'Nome: {nome}, Preço: R${preco}')
    total += preco

print(f'Total: R${total}')
format()

# 2.12 Dado o perfil de usuário {'username': 'bia_costa'}, adicione uma nova chave 'endereco'. O valor associado a essa chave deve ser outro dicionário contendo: 'rua': 'Rua das Flores, 123', 'cidade': 'São Paulo' e 'cep': '01000-000'.

separador('2.12')
endereco = {
    'rua': 'Rua das Flores, 123',
    'cidade': 'São Paulo',
    'cep': '01000-000'
}

usuario['endereco'] = endereco
print(usuario)
format()

# 2.13 Dado o perfil de usuário {'username': 'bia_costa'}, adicione uma nova chave 'profissao'. O valor associado a essa chave deve ser outro dicionário contendo: 'cargo': 'Desenvolvedora', 'empresa': 'Tech Solutions'.

separador('2.13')
usuario = {'username': 'bia_costa'}
print(f"Usuario: {usuario}")
usuario['profissao'] = {'cargo': 'Desenvolvedora', 'empresa': 'Tech Solutions'}
print(f"Usuario: {usuario}")
format()


# 2.14 A partir do perfil de usuário com endereço e profissão aninhados da questão anterior, acesse e imprima apenas o valor associado à chave 'cidade'.

separador('2.14')
print(f"Usuario: {usuario}")
usuario['endereco'] = endereco
print(f"Usuario: {usuario}")
print(f"Cidade: {usuario['endereco']['cidade']}")
format()

# 2.15 Dado o perfil de usuário com endereço aninhado, atualize o valor da chave 'rua' para 'Avenida Principal, 456'.

separador('2.15')
usuario['endereco']['rua'] = 'Avenida Principal, 456'
print(f"Endereço atualizado: {usuario['endereco']}")
format()

# 2.16 Crie um dicionário para mapear coordenadas para nomes de locais. Use a tupla (-8.0578, -34.8829) como chave para o valor 'Recife' e a tupla (-23.5505, -46.6333) como chave para o valor 'São Paulo'.

separador('2.16')
locais = {
    (-8.0578, -34.8829): 'Recife',
    (-23.5505, -46.6333): 'São Paulo'
}
print(locais)
format()

# 2.17 A partir do dicionário da questão anterior, adicione um novo local. A chave deve ser a tupla (-22.9068, -43.1729) e o valor deve ser 'Rio de Janeiro'.

separador('2.17')
locais[(-22.9068, -43.1729)] = 'Rio de Janeiro'
print(locais)
format()

# 2.18 Escreva uma função que, dado um dicionário de locais, encontre o nome do local a partir de uma tupla de coordenadas. A função deve retornar uma mensagem padrão caso a coordenada não seja encontrada. Teste a função com as coordenadas (-23.5505, -46.6333) e (0, 0).

separador('2.18')
def encontrar_local(locais, coordenadas):
    return locais.get(coordenadas, 'Local não encontrado')

print(encontrar_local(locais, (-23.5505, -46.6333)))
print(encontrar_local(locais, (0, 0)))
format()

# Parte 3: Vetores (Listas e NumPy)
# 3.1 Crie uma lista de hashtags (#) para redes sociais chamada tags_post com os valores ['#tecnologia', '#python', '#programacao']. Em seguida, adicione a tag '#dados' ao final da lista.

separador('3.1')
tags_post = ['#tecnologia', '#python', '#programacao']
tags_post.append('#dados')
print(tags_post)
format()

# 3.2 Dada a lista de tags ['#tecnologia', '#python', '#programacao', '#dados'], remova o elemento '#programacao'.

separador('3.2')
print(tags_post)
tags_post.remove('#programacao')
print(tags_post)
format()

# 3.3 Dada a lista de tags ['#tecnologia', '#python', '#dados'], verifique se a string '#importante' existe na lista.

separador('3.3')
print(tags_post)
if '#importante' in tags_post:
    print("#importante está na lista")
else:
    print("#importante não está na lista")
format()

# 3.4 Importe a biblioteca numpy com o alias np. Crie um array NumPy a partir da lista de itens vendidos da semana, em que os itens são tuplas representando (produto, quantidade): [('camiseta', 10), ('calça', 5), ('sapato', 2)].

separador('3.4')
itens_vendidos = [('camiseta', 10), ('calça', 5), ('sapato', 2)]
array_itens = np.array(itens_vendidos)
print(array_itens)
format()

# 3.5 Crie um array NumPy para armazenar as seguintes pontuações de um aluno: [0.85, 0.92, 0.78, 0.95, 0.88].

separador('3.5')
pontuacoes = [0.85, 0.92, 0.78, 0.95, 0.88]
array_pontuacoes = np.array(pontuacoes)
print(array_pontuacoes)
format()

# 3.6 Crie um array NumPy para armazenar as temperaturas em Celsius: [45.5, 46.0, 45.8, 47.1, 46.5].

separador('3.6')
temperaturas_celsius = [45.5, 46.0, 45.8, 47.1, 46.5]
array_temperaturas = np.array(temperaturas_celsius)
print(array_temperaturas)
format()

# 3.7 Dado o array NumPy com tuplas de itens e preços precos = np.array([(Sapato, 100.0), (Calça, 250.0), (Camiseta, 80.0), (Tênis, 150.0)]), crie um novo array aplicando um desconto de 10% a todos os elementos (multiplicando por 0.9).

separador('3.7')
precos = np.array([('Sapato', 100.0), ('Calça', 250.0), ('Camiseta', 80.0), ('Tênis', 150.0)])
precos_com_desconto = [(item, float(preco) * 0.9) for item, preco in precos]
print(precos_com_desconto)
format()

# 3.8 Modifique o desconto aplicado acima para ser de 15% e imprima todos os valores originais e com desconto no formato, o <item> custava <preco_original>, agora custa <preco_com_desconto>.

separador('3.8')
for item, preco in precos:
    preco = float(preco)
    preco_com_desconto = preco * 0.85
    print(f"O {item} custava R${preco:.2f}, agora custa R${preco_com_desconto:.2f}")
format()

# 3.9 Dados o array de quantidades quantidades = np.array([1, 2, 3]) e o array de preços unitários precos_unitarios = np.array([15.0, 30.0, 22.5]), calcule o valor total por item multiplicando os dois arrays.

separador('3.9')
quantidades = np.array([1, 2, 3])
precos_unitarios = np.array([15.0, 30.0, 22.5])
valores_totais = quantidades * precos_unitarios
print(valores_totais)
format()

# 3.10 Dado o array de temperaturas em Celsius temperaturas_celsius = np.array([45.5, 46.0, 45.8, 47.1, 46.5]), converta todas as temperaturas para Fahrenheit usando a fórmula F = C * 1.8 + 32.

separador('3.10')
temperaturas_celsius = np.array([45.5, 46.0, 45.8, 47.1, 46.5])
temperaturas_fahrenheit = temperaturas_celsius * 1.8 + 32
print(temperaturas_fahrenheit)
format()

# Parte 4: Matrizes (NumPy)
# 4.1 Crie e imprima uma matriz NumPy 3x4 (3 meses, 4 produtos) para representar as vendas com os dados: 
# [0, 1, 3]
# [9, 7, 4]
# [2, 6, 6]
# [3, 3, 3].

separador('4.1')
vendas = np.array([[0, 1, 3],
                   [9, 7, 4],
                   [2, 6, 6],
                   [3, 3, 3]])
format()

# 4.2 Usando a matriz de vendas da questão anterior, imprima seu formato (atributo .shape) e sua transposta (atributo .T).

separador('4.2')
print("Formato da matriz de vendas:", vendas.shape)
print("Transposta da matriz de vendas:")
print(vendas.T)
format()

# 4.3 Crie uma matriz NumPy 3x3 preenchida com zeros, com tipo de dado inteiro (dtype=int).

separador('4.3')
matriz_zeros = np.zeros((3, 3), dtype=int)
print("Matriz 3x3 de zeros:")
print(matriz_zeros)
format()

# 4.4 Dada a matriz de vendas da questão 4.1, extraia e imprima a linha completa de dados para o segundo produto (linha de índice 1).

separador('4.4')
linha_produto_2 = vendas[1]
print("Vendas do segundo produto:", linha_produto_2)
format()

# 4.5 Usando a mesma matriz de vendas, extraia e imprima a coluna completa de dados para o terceiro mês (coluna de índice 2).

separador('4.5')
coluna_mes_3 = vendas[:, 2]
print("Vendas do terceiro mês:", coluna_mes_3)
format()

# 4.6 Ainda com a matriz de vendas, acesse e imprima o valor específico do produto 3 (linha 2) no mês 2 (coluna 1).

separador('4.6')
valor_produto_3_mes_2 = vendas[2, 1]
print("Vendas do produto 3 no mês 2:", valor_produto_3_mes_2)
format()

# 4.7 Dada a matriz de preços matriz_precos = np.array([[10.00, 12.50], [25.00, 28.00]]), crie uma nova matriz com todos os preços aumentados em 5%.

separador('4.7')
matriz_precos = np.array([[10.00, 12.50], [25.00, 28.00]])
matriz_precos_aumentados = matriz_precos * 1.05
print("Matriz de preços aumentados em 5%:")
print(matriz_precos_aumentados)
format()

# 4.8 Dadas as matrizes de vendas com a quantidade de vendas de 4 produtos nos primeiros 3 meses do ano, vendas_eua = np.array([[100, 150, 200], [80, 120, 160], [90, 110, 130], [70, 100, 140]]) e vendas_europa = np.array([[90, 140, 190], [70, 110, 150], [80, 100, 120], [60, 90, 130]]), some-as para criar uma matriz vendas_globais.

separador('4.8')
vendas_eua = np.array([[100, 150, 200], [80, 120, 160], [90, 110, 130], [70, 100, 140]])
vendas_europa = np.array([[90, 140, 190], [70, 110, 150], [80, 100, 120], [60, 90, 130]])
vendas_globais = vendas_eua + vendas_europa
print("Vendas globais:")
print(vendas_globais)
format()

# 4.9 Dada a matriz de vendas vendas_unidades = np.array([[100, 150], [80, 120], [90, 110]]) (3 produtos x 2 meses) e o vetor de preços precos = np.array([4.99, 5.25, 2.19]), calcule a receita total por mês usando o produto escalar (np.dot).

separador('4.9')
vendas_unidades = np.array([[100, 150], [80, 120], [90, 110]])
precos = np.array([4.99, 5.25, 2.19])
receita_total = np.dot(vendas_unidades.T, precos)
print("Receita total por mês:")
print(receita_total)
format()

# 4.10 Usando a matriz de vendas da questão 4.1, calcule o total de unidades vendidas em cada mês (soma ao longo do eixo 0).

separador('4.10')
total_vendas_mensais = np.sum(vendas, axis=0)
print("Total de vendas mensais:")
print(total_vendas_mensais)
format()

# 4.11 Usando a mesma matriz de vendas, calcule a média de vendas para cada produto (média ao longo do eixo 1).

separador('4.11')
media_vendas_produtos = np.mean(vendas, axis=1)
print("Média de vendas por produto:")
print(media_vendas_produtos)
format()

# 4.12 A partir da matriz de vendas, encontre e imprima o valor máximo.

separador('4.12')
valor_maximo = np.max(vendas)
print("Valor máximo de vendas:")
print(valor_maximo)
format()

# Parte 5: Desafios Finais
# Crie uma lista chamada usuarios contendo um dicionário para um usuário. Este dicionário deve ter: a chave 'id_usuario' com valor 101; a chave 'perfil' com um dicionário aninhado {'nome': 'Ana Silva', 'email': 'ana.s@email.com'}; a chave 'permissoes' com a tupla ('leitura', 'escrita'); e a chave 'mapa_calor_logins' com uma matriz NumPy de 7x24 preenchida com zeros. Implemente uma função registrar_login(usuario) que incremente o contador no mapa de calor do usuário correspondente ao dia e hora atuais.

separador('5.1')
usuarios = [
    {
        'id_usuario': 101,
        'perfil': {
            'nome': 'Ana Silva',
            'email': 'ana.s@email.com'
        },
        'permissoes': ('leitura', 'escrita'),
        'mapa_calor_logins': np.zeros((7, 24), dtype=int)
    }
]

def registrar_login(usuario):
    agora = datetime.datetime.now()
    dia = agora.weekday()
    hora = agora.hour
    usuario['mapa_calor_logins'][dia, hora] += 1
    print(f"Login feito em: {agora.strftime('%d/%m/%Y %H:%M:%S')}")

registrar_login(usuarios[0])
print("Mapa de calor de logins:")
print(usuarios[0]['mapa_calor_logins'])
format()

# Escreva uma função analisar_inventario(catalogo) que processe um dicionário de produtos. A função deve retornar uma tupla contendo: 1. O valor total do inventário (soma de preco * estoque), 2. O nome do produto mais caro, e 3. Uma lista de produtos sem estoque. Teste a função com o catálogo: {'Laptop Gamer': {'preco': 7500.00, 'estoque': 10}, 'Mouse Vertical': {'preco': 350.00, 'estoque': 50}, 'Monitor 4K': {'preco': 4200.00, 'estoque': 15}, 'Webcam HD': {'preco': 250.00, 'estoque': 0}}.

separador('5.2')
def analisar_inventario(catalogo):
    valor_total = 0
    produto_mais_caro = ''
    preco_mais_caro = 0
    produtos_sem_estoque = []

    for produto, info in catalogo.items():
        valor_total += info['preco'] * info['estoque']
        if info['preco'] > preco_mais_caro:
            preco_mais_caro = info['preco']
            produto_mais_caro = produto
        if info['estoque'] == 0:
            produtos_sem_estoque.append(produto)

    return valor_total, produto_mais_caro, produtos_sem_estoque

catalogo = {
    'Laptop Gamer': {'preco': 7500.00, 'estoque': 10},
    'Mouse Vertical': {'preco': 350.00, 'estoque': 50},
    'Monitor 4K': {'preco': 4200.00, 'estoque': 15},
    'Webcam HD': {'preco': 250.00, 'estoque': 0}
}   

valor_total, produto_mais_caro, sem_estoque = analisar_inventario(catalogo)
preco_mais_caro = catalogo[produto_mais_caro]['preco']
print(f"Valor total do inventário: R${valor_total:.2f}")
print(f"Produto mais caro: {produto_mais_caro} (R${preco_mais_caro:.2f})")
print(f"Produtos sem estoque: {', '.join(sem_estoque) if sem_estoque else 'Nenhum'}")
format()

# Projete uma classe SocialGraph para gerenciar amizades. O construtor deve inicializar um dicionário self.conexoes. Implemente os métodos adicionar_amizade(id1, id2) para criar uma amizade mútua e obter_amigos(id_usuario) para retornar a lista de amigos. Instancie a classe e adicione as seguintes amizades: (101, 205), (101, 308), (205, 400). Teste o método obter_amigos para os usuários 101, 205 e 999.

separador('5.3')
class SocialGraph:
    def __init__(self):
        self.conexoes = {}

    def adicionar_amizade(self, id1, id2):
        if id1 not in self.conexoes:
            self.conexoes[id1] = set()
        if id2 not in self.conexoes:
            self.conexoes[id2] = set()
        self.conexoes[id1].add(id2)
        self.conexoes[id2].add(id1)

    def obter_amigos(self, id_usuario):
        return list(self.conexoes.get(id_usuario, []))


social_graph = SocialGraph()
social_graph.adicionar_amizade(101, 205)
social_graph.adicionar_amizade(101, 308)
social_graph.adicionar_amizade(205, 400)

print("Amigos de 101:", sorted(social_graph.obter_amigos(101)))
print("Amigos de 205:", sorted(social_graph.obter_amigos(205)))
print("Amigos de 999:", sorted(social_graph.obter_amigos(999)))
format()