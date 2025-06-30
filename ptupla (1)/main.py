# Parte 1: Tuplas
# 1.1 Crie uma tupla para armazenar os códigos de cor RGB (Vermelho, Verde, Azul), usando os valores 255 para vermelho, 102 para verde e 0 para azul.

cor = (255, 102, 0)

# 1.2 Crie uma tupla para as coordenadas geográficas, usando -8.0578 para latitude e -34.8829 para longitude.

coordenada_geografica = (-8.0578, -34.8829)

# 1.3 Crie uma tupla para armazenar as informações básicas e imutáveis de um usuário, contendo o ID 101, o username 'ana_silva' e a data de criação '2023-01-15'.

usuario = (101, 'ana_silva', '2023-01-15')

# 1.4 Dada a tupla de cores RGB (255, 102, 0), acesse e imprima o valor do componente 'Verde' (o segundo elemento, de índice 1).

r, g, b = cor
print(g)

# 1.5 Dada a tupla de coordenadas (-8.0578, -34.8829), desempacote-a em duas variáveis separadas chamadas latitude e longitude.

latitude = coordenada_geografica[0]
longitude = coordenada_geografica[1]

print(f"latitude: {latitude}\nlongitude {longitude}")

# 1.6 A partir da tupla de usuário (205, 'Carlos Pereira', 'carlos.p@email.com'), que representa (id, nome, email), desempacote-a em variáveis e use a variável do nome para imprimir uma saudação.

usuario = (205, 'Carlos Pereira', 'carlos.p@email.com')

id, nome, email = usuario
print(f"Olá, {nome} saudações!")

# 1.7 Dada a tupla de papéis de administrador ('moderador', 'editor', 'sysadmin'), itere sobre ela e imprima cada papel.

administrador = ('moderador', 'editor', 'sysadmin')

for papel in administrador:
    print(papel)

# 1.8 Dada a tupla dados dos usuários acima, itere sobre elas e imprima cada dado.

for dado in usuario:
    print(dado)

# 1.9 Dada a tupla de cores RGB acima, itere sobre ela e imprima cada parte da cor, R, G e B.

for rgb in cor:
    print(rgb)

# 1.10 Escreva uma função que verifique se um papel de usuário existe em uma tupla de papéis de administrador ('moderador', 'editor', 'sysadmin'). Teste a função com os papéis 'editor' e 'usuario_comum'.

def admin(papel):
    resultado = False
    administrador = ('moderador', 'editor', 'sysadmin')
    for admin in administrador:
        if papel == admin:
            resultado = True

    return resultado

print (f"Editor é administrador? {admin('editor')}")
print (f"Usuário é administrador? {admin('usuario')}")

# 1.11 Dada a tupla de atribuições das pessoas de um equipe ('editor', 'leitor', 'editor', 'comentarista', 'editor'), escreva uma função que conta o número de vezes em que um papel aparece, teste a função com os papíes 'editor', 'comentarista' e 'tradutor'.

def contador(papel):
    equipe = ('editor', 'leitor', 'editor', 'comentarista', 'editor')
    
    x = 0
    for i in equipe:
        if i == papel:
            x+=1
    return x

print(f"Editor: {contador('editor')}")


# Parte 2: Dicionários
# 2.1 Crie um dicionário para um usuário. Use a chave 'username' para o valor 'bia_costa', a chave 'email' para 'bia.costa@email.com', e a chave 'data_adesao' para '2024-05-21'.

usuario = {
    'username': 'bia_costa',
    'email':'bia.costa@email.com',
    'data_adesao': '2024-05-21'
}
print(usuario)

# 2.2 Crie um dicionário para um produto. Use as chaves 'id_produto', 'nome', 'preco' e 'estoque' com os respectivos valores 'XYZ-001', 'Fone de Ouvido Sem Fio', 299.90 e 150.

produto = {
    'id_produto': 'XYZ-001',
    'nome': 'Fone de Ouvido Sem Fio',
    'preco': '299.90',
    'estoque': '150'
}
print(produto)

# 2.3 Crie um dicionário vazio chamado preferencias_usuario.

preferencias_usuario = {}

# 2.4 Dado o dicionário de produto {'id_produto': 'XYZ-001', 'nome': 'Fone de Ouvido Sem Fio', 'preco': 299.90, 'estoque': 150}, acesse e imprima o preço original. Em seguida, atualize o preço para o valor promocional de 249.99.

print(f'Preço original: R${produto["preco"]}')
produto['preco'] = 249.99
print(f'Preço promocional: R${produto["preco"]}')

# 2.5 Dado o perfil de usuário {'username': 'bia_costa', 'email': 'bia.costa@email.com', 'data_adesao': '2024-05-21'}, adicione uma nova informação: a chave 'telefone' com o valor '98765-4321'.

# 2.6 Dado o perfil de usuário {'username': 'bia_costa'}, use o método .get() para tentar acessar o valor da chave 'ultimo_login'. Como a chave não existe, forneça o valor padrão 'Nunca logou'. Após a tentativa, bia fez o login, então atualize o dicionário para incluir a chave 'ultimo_login' com o valor '2024-05-22'.

# 2.7 Dado o perfil de usuário {'username': 'bia_costa', 'email': 'bia.costa@email.com', 'telefone_fixo': '3265-4321'}, use a instrução del ou a função pop() para remover a chave 'telefone_fixo'.

# 2.8 Dado o catálogo de produtos {'XYZ-001': 'Fone de Ouvido Sem Fio', 'ABC-002': 'Teclado Mecânico'}, use a instrução o método .pop() para remover o produto com a chave 'XYZ-001'. Armazene o valor retornado (o nome do produto) e imprima uma mensagem de confirmação.

# 2.9 Dado o perfil de usuário {'username': 'bia_costa'}, tente remover a chave 'email' usando o método .pop(). Forneça o valor padrão 'Email não encontrado.' para evitar um erro.

# 2.10 Dado o catálogo de produtos {'Fone de Ouvido': 249.99, 'Teclado Mecânico': 450.00, 'Mouse Gamer': 120.50}, itere sobre seus itens e imprima o nome e o preço de cada um no formato 'Nome: R$Preço'.

# 2.11 Dado a lista de compras da feira {'Tapioca': 18.99, 'Queijo Manteiga': 45.00, 'Ovos': 23.50}, itere sobre seus itens e imprima o nome e o preço de cada um no formato 'Nome: R$Preço' e depois imprima o total.

# 2.12 Dado o perfil de usuário {'username': 'bia_costa'}, adicione uma nova chave 'endereco'. O valor associado a essa chave deve ser outro dicionário contendo: 'rua': 'Rua das Flores, 123', 'cidade': 'São Paulo' e 'cep': '01000-000'.

# 2.13 Dado o perfil de usuário {'username': 'bia_costa'}, adicione uma nova chave 'profissao'. O valor associado a essa chave deve ser outro dicionário contendo: 'cargo': 'Desenvolvedora', 'empresa': 'Tech Solutions'.

# 2.14 A partir do perfil de usuário com endereço e profissão aninhados da questão anterior, acesse e imprima apenas o valor associado à chave 'cidade'.

# 2.15 Dado o perfil de usuário com endereço aninhado, atualize o valor da chave 'rua' para 'Avenida Principal, 456'.

# 2.16 Crie um dicionário para mapear coordenadas para nomes de locais. Use a tupla (-8.0578, -34.8829) como chave para o valor 'Recife' e a tupla (-23.5505, -46.6333) como chave para o valor 'São Paulo'.

# 2.17 A partir do dicionário da questão anterior, adicione um novo local. A chave deve ser a tupla (-22.9068, -43.1729) e o valor deve ser 'Rio de Janeiro'.

# 2.18 Escreva uma função que, dado um dicionário de locais, encontre o nome do local a partir de uma tupla de coordenadas. A função deve retornar uma mensagem padrão caso a coordenada não seja encontrada. Teste a função com as coordenadas (-23.5505, -46.6333) e (0, 0).





