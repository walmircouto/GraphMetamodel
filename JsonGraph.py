import json
import snap

JsonFile = open('java.json')
JsonData = json.load(JsonFile)
JsonFile.close()

#print(JsonData)

# Criação do Grafo
G1 = snap.TNGraph.New()
n = 1
i = 2

# Identificando os vértices 
NIdName = snap.TIntStrH()


for (k, v) in JsonData.items():
   G1.AddNode(n)
   G1.AddNode(i)
   G1.AddEdge(n,i)
   NIdName[n] = k 
   NIdName[i] = str(v)
   n = n + 1
   i = i + 1

# Plotagem do grafo
snap.DrawGViz(G1, snap.gvlDot, "JAVAJsonGraph.png", "JAVAJsonGraph", NIdName)

'''
for key in JsonData:
	G1.AddNode(n)
	NIdName[n] = str(key)
	for value in JsonData[key]:
		G1.AddNode(i)
		G1.AddEdge(n,i) 
   		NIdName[i] = str(value)
   		i = i + 1
   	n = n + 1
'''


'''
json_object = json.loads(json_file)
for element in json_object: 
    for value in json_object['Name_OF_YOUR_KEY/ELEMENT']:
        print(json_object['Name_OF_YOUR_KEY/ELEMENT']['INDEX_OF_VALUE']['VALUE'])
'''




   #print("Key: " + k)
   #print("Value: " + str(v))


'''
import snap
import networkx as nx
from node2vec import Node2Vec


# Criação do Grafo
G1 = snap.TNGraph.New()

# Adição dos vértices
G1.AddNode(1)
G1.AddNode(2)
G1.AddNode(3)
G1.AddNode(4)
G1.AddNode(5)
G1.AddNode(6)
G1.AddNode(7)
G1.AddNode(8)
G1.AddNode(9)
G1.AddNode(10)
G1.AddNode(11)
G1.AddNode(12)
G1.AddNode(13)
G1.AddNode(14)
G1.AddNode(15)
G1.AddNode(16)
G1.AddNode(17)
G1.AddNode(18)
G1.AddNode(19)
G1.AddNode(20)
G1.AddNode(21)
G1.AddNode(22)
G1.AddNode(23)
G1.AddNode(24)
G1.AddNode(25)
G1.AddNode(26)
G1.AddNode(27)
G1.AddNode(28)
G1.AddNode(29)
G1.AddNode(30)
G1.AddNode(31)
G1.AddNode(32)
G1.AddNode(33)
G1.AddNode(34)
G1.AddNode(35)
G1.AddNode(36)
G1.AddNode(37)
G1.AddNode(38)
G1.AddNode(39)
G1.AddNode(40)
G1.AddNode(41)
G1.AddNode(42)
G1.AddNode(43)
G1.AddNode(44)
G1.AddNode(45)
G1.AddNode(46)
G1.AddNode(47)
G1.AddNode(48)
G1.AddNode(49)
G1.AddNode(50)
G1.AddNode(51)
G1.AddNode(52)
G1.AddNode(53)
G1.AddNode(54)
G1.AddNode(55)
G1.AddNode(56)
G1.AddNode(57)
G1.AddNode(58)
G1.AddNode(59)
G1.AddNode(60)

# Adição das arestas entre os vértices
G1.AddEdge(1,2)
G1.AddEdge(2,3)
G1.AddEdge(3,4)
G1.AddEdge(3,6)
G1.AddEdge(3,21)
G1.AddEdge(3,40)
G1.AddEdge(4,5)
G1.AddEdge(6,7)
G1.AddEdge(2,8)
G1.AddEdge(8,9)
G1.AddEdge(8,11)
G1.AddEdge(9,10)
G1.AddEdge(11,12)
G1.AddEdge(8,13)
G1.AddEdge(8,15)
G1.AddEdge(8,17)
G1.AddEdge(8,19)
G1.AddEdge(13,14)
G1.AddEdge(15,16)
G1.AddEdge(17,18)
G1.AddEdge(19,20)
G1.AddEdge(21,22)
G1.AddEdge(22,23)
G1.AddEdge(21,24)
G1.AddEdge(24,25)
G1.AddEdge(21,26)
G1.AddEdge(26,27)
G1.AddEdge(21,28)
G1.AddEdge(28,29)
G1.AddEdge(21,30)
G1.AddEdge(30,31)
G1.AddEdge(21,32)
G1.AddEdge(32,33)
G1.AddEdge(21,34)
G1.AddEdge(34,35)
G1.AddEdge(21,36)
G1.AddEdge(36,37)
G1.AddEdge(21,38)
G1.AddEdge(38,39)
G1.AddEdge(40,41)
G1.AddEdge(41,42)
G1.AddEdge(40,43)
G1.AddEdge(43,44)
G1.AddEdge(40,45)
G1.AddEdge(45,46)
G1.AddEdge(40,47)
G1.AddEdge(47,48)
G1.AddEdge(40,49)
G1.AddEdge(49,50)
G1.AddEdge(40,51)
G1.AddEdge(51,52)
G1.AddEdge(40,53)
G1.AddEdge(53,54)
G1.AddEdge(40,55)
G1.AddEdge(55,56)
G1.AddEdge(40,57)
G1.AddEdge(57,58)
G1.AddEdge(40,59)
G1.AddEdge(59,60)

# Identificando os vértices 
NIdName = snap.TIntStrH()
NIdName[1] = "JAVAMetamodel" # G1.AddEdge(1,2)
NIdName[2] = "EPackage" # G1.AddEdge(2,3) / G1.AddEdge(2,8)
NIdName[3] = "eClassifiers" # eClassifiers-01
NIdName[4] = "name" # G1.AddEdge(3,4)
NIdName[5] = "JAVA" # G1.AddEdge(4,5)
NIdName[6] = "prefix" # G1.AddEdge(3,6)
NIdName[7] = "ecore" # G1.AddEdge(6,7)
NIdName[8] = "eClassifiers" # eClassifiers-02 --> G1.AddEdge(8,9) / G1.AddEdge(8,11)
NIdName[9] = "name" # G1.AddEdge(8,9)
NIdName[10] = "PrimitiveTypes" # G1.AddEdge(9,10)
NIdName[11] = "prefix" # G1.AddEdge(8,11)
NIdName[12] = "ecore" # G1.AddEdge(11,12)
NIdName[13] = "type" # G1.AddEdge(8,13)
NIdName[14] = "EDataType" # G1.AddEdge(13,14)
NIdName[15] = "name" # G1.AddEdge(8,15)
NIdName[16] = "String" # G1.AddEdge(15,16)
NIdName[17] = "type" # G1.AddEdge(8,17)
NIdName[18] = "EDataType" # G1.AddEdge(17,18)
NIdName[19] = "name" # G1.AddEdge(8,19)
NIdName[20] = "Boolean" # G1.AddEdge(19,20)
NIdName[21] = "eStructuralFeatures" # G1.AddEdge(3,21)
NIdName[22] = "type" # G1.AddEdge(21,22)
NIdName[23] = "EAttribute" # G1.AddEdge(22,23)
NIdName[24] = "name" # G1.AddEdge(21,24)
NIdName[25] = "name" # G1.AddEdge(24,25)
NIdName[26] = "ordered" # G1.AddEdge(21,26)
NIdName[27] = "false" # G1.AddEdge(26,27)
NIdName[28] = "unique" # G1.AddEdge(21,28)
NIdName[29] = "false" # G1.AddEdge(28,29)
NIdName[30] = "lowerBound" # G1.AddEdge(21,30)
NIdName[31] = "1" # G1.AddEdge(30,31)
NIdName[32] = "eType" # G1.AddEdge(21,32)
NIdName[33] = "String" # G1.AddEdge(32,33)
NIdName[34] = "type" # G1.AddEdge(21,34)
NIdName[35] = "EClass" # G1.AddEdge(34,35)
NIdName[36] = "name" # G1.AddEdge(21,36)
NIdName[37] = "JavaElement" # G1.AddEdge(36,37)
NIdName[38] = "abstract" # G1.AddEdge(21,38)
NIdName[39] = "true" # G1.AddEdge(38,39)
NIdName[40] = "eStructuralFeatures" # G1.AddEdge(3,40)
NIdName[41] = "type" # G1.AddEdge(40,41)
NIdName[42] = "EAttribute" # G1.AddEdge(41,42)
NIdName[43] = "name" # G1.AddEdge(40,43)
NIdName[44] = "isFinal" # G1.AddEdge(43,44)
NIdName[45] = "ordered" # G1.AddEdge(40,45)
NIdName[46] = "false" # G1.AddEdge(45,46)
NIdName[47] = "unique" # G1.AddEdge(40,47)
NIdName[48] = "false" # G1.AddEdge(47,48)
NIdName[49] = "lowerBound" # G1.AddEdge(40,49)
NIdName[50] = "1" # G1.AddEdge(49,50)
NIdName[51] = "eType" # G1.AddEdge(40,51)
NIdName[52] = "Boolean" # G1.AddEdge(51,52)
NIdName[53] = "type" # G1.AddEdge(40,53)
NIdName[54] = "EClass" # G1.AddEdge(53,54)
NIdName[55] = "name" # G1.AddEdge(40,55)
NIdName[56] = "ClassFeature" # G1.AddEdge(55,56)
NIdName[57] = "abstract" # G1.AddEdge(40,57)
NIdName[58] = "true" # G1.AddEdge(57,58)
NIdName[59] = "eSuperTypes" # G1.AddEdge(40,59)
NIdName[60] = "JavaElement" # G1.AddEdge(59,60)

# Plotagem do grafo
snap.DrawGViz(G1, snap.gvlDot, "JAVAMetamodel.png", "JAVAMetamodel", NIdName)


# Imprimindo informacoes sobre o grafo
snap.PrintInfo(G1, "JAVAMetamodel Stats", "JAVAMetamodel-info.txt", False)


# Pesquisa de largura (distância) e profundidade
D = snap.GetBfsFullDiam(G1, 100)
print ("diameter", D)

ED = snap.GetBfsEffDiam(G1, 100)
print ("effective diameter", ED)

# Propriedades espectral do grafo JavaMetaModel
# tá dando erro --> verificar!
# ------------------------------------------------
#EigV = snap.TFltV()
#snap.GetEigVec(G1, EigV)

#nr = 0

#for f in EigV:
#	nr += 1
#	print ("%d: %.6f" % (nr, f))

Core3 = snap.GetKCore(G1, 3)

#print (Core3)



# ********************************************************************************************

'''
# Tentativa do uso do node2vec no JavaMetaModelGraph

# FILES
#EMBEDDING_FILENAME = './embeddings.emb'
#EMBEDDING_MODEL_FILENAME = './embeddings.model'

#node2vec = Node2Vec(G1, dimensions=64, walk_length=30, num_walks=200, workers=4)

# Embed
#model = node2vec.fit(window=10, min_count=1, batch_words=4)

# Look for most similar nodes
#model.wv.most_similar('2')  # Output node names are always strings

# Save embeddings for later use
#model.wv.save_word2vec_format(EMBEDDING_FILENAME)

# Save model for later use
#model.save(EMBEDDING_MODEL_FILENAME)

#'''
#model = _n2v.fit()
#model.wv.save_word2vec_format("out")

#print("\n\nRESULTADO")
#with open('out', 'r') as f:
#    print(f.read())















