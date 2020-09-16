import networkx as nx
from node2vec import Node2Vec

# Arquivos usados na Analise
ArquivoComOsCasamentos = './Casamentos.emb'
ArquivoModeloCasamentos = './Casamentos.model'

# Criando o Grafo
# graph = nx.fast_gnp_random_graph(n=100, p=0.5)
graph = nx.fast_gnp_random_graph(n=80, p=0.5)

# Probabilidades predefinidas e geracao das caminhadas aleatorias --> aqui falta explorar o entendimento de cada parametro
node2vec = Node2Vec(graph, dimensions=64, walk_length=30, num_walks=200, workers=4)

# Se a dimensao do grafo for muito, pode ser preciso usar um diretorio temporario para auxiliar no processamento 
# Nesse caso sera usado processamento paralelo (quebrando o grafo em partes menores) 
#node2vec = Node2Vec(graph, dimensions=64, walk_length=30, num_walks=200, workers=4, temp_folder="/mnt/tmp_data")

# Realizando os casamento dos nodos (vertices)
# Aqui podemos passar diversas palavras chaves como parametro, porem preciso explorar o entendimento de cada uma delas
# e o seus efeitos na execucao
model = node2vec.fit(window=10, min_count=1, batch_words=4)  

# Procurando por similaridades entre nos nodos (vertices), passando como parametro o grau de similaridades
# falta entender qual o impacto desses niveis na pesquisa de similaridades
model.wv.most_similar('2')  # O nome dos nodos (vertices) de saida sao sempre string

# Salvando os casamentos realizados, com suas similaridades
model.wv.save_word2vec_format(ArquivoComOsCasamentos)

# Salvando o modelo de casamentos
model.save(ArquivoModeloCasamentos)
