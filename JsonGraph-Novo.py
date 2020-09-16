import json
import snap


# Criação do Grafo
G1 = snap.TNGraph.New()

# Variáveis contadoras que servem para criar os vértices e formar as arestas
n = 1 
i = 2

# Identificando os vértices 
NIdName = snap.TIntStrH()

# Abertura do arquivo JSON contendo o metamodelo e atribuindo a variável "data" do tipo dataset 
with open('java.json') as f:
	data = json.load(f)

# Identificando o vértice raiz do metamodelo
G1.AddNode(n)
NIdName[n] = "XMI"
IdXMI = n

# Identificando o vértice "EPackage", e estabelecendo a aresta entre "XMI" <--> "EPackage"
G1.AddNode(i)
G1.AddEdge(n,i)
NIdName[i] = "EPackage"
IdEPackage = i
i = i + 1

# Identificando o vértice "xmlns:xmi", e estabelecendo a aresta entre "XMI" <--> "xmlns:xmi"
G1.AddNode(i)
G1.AddEdge(n,i)
NIdName[i] = "xmlns:xmi"
IdXmlXmi = i
i = i + 1

# Identificando o vértice com o conteúdo de "xmlns:xmi", e estabelecendo uma aresta entre eles
G1.AddNode(i)
G1.AddEdge(IdXmlXmi,i)
NIdName[i] = data['XMI']['xmlns:xmi']
i = i + 1

# Identificando o vértice "xmlns:xsi", e estabelecendo a aresta entre "XMI" <--> "xmlns:xsi"
G1.AddNode(i)
G1.AddEdge(n,i)
NIdName[i] = "xmlns:xsi"
IdXmlXsi = i
i = i + 1

# Identificando o vértice com o conteúdo de "xmlns:xsi", e estabelecendo uma aresta entre eles
G1.AddNode(i)
G1.AddEdge(IdXmlXsi,i)
NIdName[i] = data['XMI']['xmlns:xsi']
i = i + 1

# Identificando o vértice "xmlns:ecore", e estabelecendo a aresta entre "XMI" <--> "xmlns:ecore"
G1.AddNode(i)
G1.AddEdge(n,i)
NIdName[i] = "xmlns:ecore"
IdXmlEcore = i
i = i + 1

# Identificando o vértice com o conteúdo de "xmlns:ecore", e estabelecendo uma aresta entre eles
G1.AddNode(i)
G1.AddEdge(IdXmlEcore,i)
NIdName[i] = data['XMI']['xmlns:ecore']
i = i + 1

# Identificando o vértice "xmi:version", e estabelecendo a aresta entre "XMI" <--> "xmi:version"
G1.AddNode(i)
G1.AddEdge(n,i)
NIdName[i] = "xmi:version"
IdXmiVersion = i
i = i + 1

# Identificando o vértice com o conteúdo de "xmi:version", e estabelecendo uma aresta entre eles
G1.AddNode(i)
G1.AddEdge(IdXmiVersion,i)
NIdName[i] = data['XMI']['xmi:version']
i = i + 1

# Identificando o vértice "prefix", e estabelecendo a aresta entre "XMI" <--> "prefix"
G1.AddNode(i)
G1.AddEdge(n,i)
NIdName[i] = "prefix"
IdPrefix = i
i = i + 1

# Identificando o vértice com o conteúdo de "prefix", e estabelecendo uma aresta entre eles
G1.AddNode(i)
G1.AddEdge(IdPrefix,i)
NIdName[i] = data['XMI']['prefix']


# Para cada instância de "eClassifiers" contida em "EPackage", vai estabelecer no grafo as arestas entre eles
for EPackage in data['XMI']['EPackage']:
	i = i + 1

	# Identificando o vértice "eClassifiers", e estabelecendo a aresta entre "EPackage" <--> "eClassifiers"
	G1.AddNode(i)
	G1.AddEdge(IdEPackage,i)
	NIdName[i] = "eClassifiers"
	IdeClassifiers = i
	i = i + 1

	# Identificando o vértice "name" que pertence ao "eClassifiers", e estabelecendo a aresta entre 
	# "eClassifiers" <--> "name"
	G1.AddNode(i)
	G1.AddEdge(IdeClassifiers,i)
	NIdName[i] = "name"
	Id_name = i
	i = i + 1

	# Identificando o vértice com o conteúdo de "name", e estabelecendo uma aresta entre eles
	G1.AddNode(i)
	G1.AddEdge(Id_name,i)
	NIdName[i] = EPackage['name']
	i = i + 1

	# Identificando o vértice "prefix" que pertence ao "eClassifiers", e estabelecendo a aresta entre 
	# "eClassifiers" <--> "prefix"
	G1.AddNode(i)
	G1.AddEdge(IdeClassifiers,i)
	NIdName[i] = "prefix"
	Id_prefix = i
	i = i + 1

	# Identificando o vértice com o conteúdo de "prefix", e estabelecendo uma aresta entre eles
	G1.AddNode(i)
	G1.AddEdge(Id_prefix,i)
	NIdName[i] = EPackage['prefix']

	# Variável contadora para identificar cada "eClassifier"
	QtdeEClassifier = 0

	# Para cada item da lista de "eClassifiers" contida no "EPackage"
	for eClassifiers in EPackage['eClassifiers']:
		# Incrementa as variáveis contadoras
		QtdeEClassifier = QtdeEClassifier + 1
		i = i + 1

		# Cria o vértice do "eClassifier" para cada item da lista de "eClassifiers"
		G1.AddNode(i)
		G1.AddEdge(IdeClassifiers,i)
		NIdName[i] = "eClassifier-" + str(QtdeEClassifier)
		Id_eClassifier = i 
		i = i + 1

		# Identificando o vértice "xsi:type" que pertence ao "eClassifier", e estabelecendo a aresta entre 
		# "eClassifier" <--> "xsi:type"
		G1.AddNode(i)
		G1.AddEdge(Id_eClassifier,i)
		NIdName[i] = "xsi:type"
		Id_xsi_type = i
		i = i + 1

		# Identificando o vértice com o conteúdo de "xsi:type", e estabelecendo uma aresta entre eles
		G1.AddNode(i)
		G1.AddEdge(Id_xsi_type,i)
		NIdName[i] = eClassifiers['xsi:type']
		i = i + 1

		# Identificando o vértice "name" que pertence ao "eClassifier", e estabelecendo a aresta entre 
		# "eClassifier" <--> "name"
		G1.AddNode(i)
		G1.AddEdge(Id_eClassifier,i)
		NIdName[i] = "name"
		Id_name = i
		i = i + 1

		# Identificando o vértice com o conteúdo de "name", e estabelecendo uma aresta entre eles
		G1.AddNode(i)
		G1.AddEdge(Id_name,i)
		NIdName[i] = eClassifiers['name']
		i = i + 1

		# Verifica se o "eClassifiers" em questão possui o elemento 'abstract', se TRUE ele cria o elemento no grafo 
		if 'abstract' in eClassifiers:

			# Identificando o vértice "abstract" que pertence ao "eClassifier", e estabelecendo a aresta entre 
			# "eClassifier" <--> "abstract"
			G1.AddNode(i)
			G1.AddEdge(Id_eClassifier,i)
			NIdName[i] = "abstract"
			Id_abstract = i
			i = i + 1

			# Identificando o vértice com o conteúdo de "abstract", e estabelecendo uma aresta entre eles
			G1.AddNode(i)
			G1.AddEdge(Id_abstract,i)
			NIdName[i] = eClassifiers['abstract']
			i = i + 1

		# Verifica se o "eClassifiers" em questão possui o elemento 'eSuperTypes', se TRUE ele cria o elemento no grafo 
		if 'eSuperTypes' in eClassifiers:

			# Identificando o vértice "eSuperTypes" que pertence ao "eClassifier", e estabelecendo a aresta entre 
			# "eClassifier" <--> "eSuperTypes"
			G1.AddNode(i)
			G1.AddEdge(Id_eClassifier,i)
			NIdName[i] = "eSuperTypes"
			Id_eSuperTypes = i
			i = i + 1

			# Identificando o vértice com o conteúdo de "eSuperTypes", e estabelecendo uma aresta entre eles
			G1.AddNode(i)
			G1.AddEdge(Id_eSuperTypes,i)
			NIdName[i] = eClassifiers['eSuperTypes']
			i = i + 1		

			
		# Verifica se o "eClassifiers" em questão possui o elemento 'eStructuralFeatures', se TRUE ele cria o elemento no grafo 
		if 'eStructuralFeatures' in eClassifiers:	
			
			# Variável contadora para identificar cada "eStructuralFeature"
			Qtde_eStructuralFeature = 0

			if isinstance(eClassifiers['eStructuralFeatures'], list):
				
				# Para cada item da lista de "eStructuralFeatures" contido em "eClassifiers"
				for eStructuralFeatures in eClassifiers['eStructuralFeatures']:
					# Incrementa as variáveis contadoras
					Qtde_eStructuralFeature = Qtde_eStructuralFeature + 1
					i = i + 1

					# Cria o vértice do "eStructuralFeature" para cada item da lista de "eClassifiers"
					G1.AddNode(i)
					G1.AddEdge(Id_eClassifier,i)
					NIdName[i] = "eStructuralFeature-" + str(Qtde_eStructuralFeature)
					Id_eStructuralFeature = i 
					i = i + 1

					# Identificando o vértice "xsi:type" que pertence ao "eStructuralFeature", e estabelece a aresta entre 
					# "eStructuralFeature" <--> "xsi:type"
					G1.AddNode(i)
					G1.AddEdge(Id_eStructuralFeature,i)
					NIdName[i] = "xsi:type"
					Id_xsi_type = i
					i = i + 1

					# Identificando o vértice com o conteúdo de "xsi:type", e estabelece uma aresta entre eles
					G1.AddNode(i)
					G1.AddEdge(Id_xsi_type,i)
					NIdName[i] = eStructuralFeatures['xsi:type']
					i = i + 1
					
					# Identificando o vértice "name" que pertence ao "eStructuralFeature", e estabelece a aresta entre 
					# "eStructuralFeature" <--> "name"
					G1.AddNode(i)
					G1.AddEdge(Id_eStructuralFeature,i)
					NIdName[i] = "name"
					Id_name = i
					i = i + 1

					# Identificando o vértice com o conteúdo de "name", e estabelece uma aresta entre eles
					G1.AddNode(i)
					G1.AddEdge(Id_name,i)
					NIdName[i] = eStructuralFeatures['name']
					i = i + 1

					# Verifica se o "eStructuralFeatures" em questão possui o elemento 'ordered', se TRUE ele cria o elemento no grafo
					if 'ordered' in eStructuralFeatures:
					
						# Identificando o vértice "ordered" que pertence ao "eStructuralFeature", e estabelece a aresta entre 
						# "eStructuralFeature" <--> "ordered"
						G1.AddNode(i)
						G1.AddEdge(Id_eStructuralFeature,i)
						NIdName[i] = "ordered"
						Id_ordered = i
						i = i + 1

						# Identificando o vértice com o conteúdo de "ordered", e estabelece uma aresta entre eles
						G1.AddNode(i)
						G1.AddEdge(Id_ordered,i)
						NIdName[i] = eStructuralFeatures['ordered']
						i = i + 1

					# Verifica se o "eStructuralFeatures" em questão possui o elemento 'upperBound', se TRUE ele cria o elemento no grafo
					if 'upperBound' in eStructuralFeatures:
					
						# Identificando o vértice "upperBound" que pertence ao "eStructuralFeature", e estabelece a aresta entre 
						# "eStructuralFeature" <--> "upperBound"
						G1.AddNode(i)
						G1.AddEdge(Id_eStructuralFeature,i)
						NIdName[i] = "upperBound"
						Id_upperBound = i
						i = i + 1

						# Identificando o vértice com o conteúdo de "upperBound", e estabelece uma aresta entre eles
						G1.AddNode(i)
						G1.AddEdge(Id_upperBound,i)
						NIdName[i] = eStructuralFeatures['upperBound']
						i = i + 1

					# Verifica se o "eStructuralFeatures" em questão possui o elemento 'unique', se TRUE ele cria o elemento no grafo
					if 'unique' in eStructuralFeatures:
					
						# Identificando o vértice "unique" que pertence ao "eStructuralFeature", e estabelece a aresta entre 
						# "eStructuralFeature" <--> "unique"
						G1.AddNode(i)
						G1.AddEdge(Id_eStructuralFeature,i)
						NIdName[i] = "unique"
						Id_unique = i
						i = i + 1

						# Identificando o vértice com o conteúdo de "unique", e estabelece uma aresta entre eles
						G1.AddNode(i)
						G1.AddEdge(Id_unique,i)
						NIdName[i] = eStructuralFeatures['unique']
						i = i + 1

					# Verifica se o "eStructuralFeatures" em questão possui o elemento 'lowerBound', se TRUE ele cria o elemento no grafo
					if 'lowerBound' in eStructuralFeatures:
					
						# Identificando o vértice "lowerBound" que pertence ao "eStructuralFeature", e estabelece a aresta entre 
						# "eStructuralFeature" <--> "lowerBound"
						G1.AddNode(i)
						G1.AddEdge(Id_eStructuralFeature,i)
						NIdName[i] = "lowerBound"
						Id_lowerBound = i
						i = i + 1

						# Identificando o vértice com o conteúdo de "lowerBound", e estabelece uma aresta entre eles
						G1.AddNode(i)
						G1.AddEdge(Id_lowerBound,i)
						NIdName[i] = eStructuralFeatures['lowerBound']
						i = i + 1

					# Verifica se o "eStructuralFeatures" em questão possui o elemento 'eType', se TRUE ele cria o elemento no grafo
					if 'eType' in eStructuralFeatures:
					
						# Identificando o vértice "eType" que pertence ao "eStructuralFeature", e estabelece a aresta entre 
						# "eStructuralFeature" <--> "eType"
						G1.AddNode(i)
						G1.AddEdge(Id_eStructuralFeature,i)
						NIdName[i] = "eType"
						Id_eType = i
						i = i + 1

						# Identificando o vértice com o conteúdo de "eType", e estabelece uma aresta entre eles
						G1.AddNode(i)
						G1.AddEdge(Id_eType,i)
						NIdName[i] = eStructuralFeatures['eType']
						i = i + 1

					# Verifica se o "eStructuralFeatures" em questão possui o elemento 'containment', se TRUE ele cria o elemento no grafo
					if 'containment' in eStructuralFeatures:
					
						# Identificando o vértice "containment" que pertence ao "eStructuralFeature", e estabelece a aresta entre 
						# "eStructuralFeature" <--> "containment"
						G1.AddNode(i)
						G1.AddEdge(Id_eStructuralFeature,i)
						NIdName[i] = "containment"
						Id_containment = i
						i = i + 1

						# Identificando o vértice com o conteúdo de "containment", e estabelece uma aresta entre eles
						G1.AddNode(i)
						G1.AddEdge(Id_containment,i)
						NIdName[i] = eStructuralFeatures['containment']
						i = i + 1

					# Verifica se o "eStructuralFeatures" em questão possui o elemento 'eOpposite', se TRUE ele cria o elemento no grafo
					if 'eOpposite' in eStructuralFeatures:
					
						# Identificando o vértice "eOpposite" que pertence ao "eStructuralFeature", e estabelece a aresta entre 
						# "eStructuralFeature" <--> "eOpposite"
						G1.AddNode(i)
						G1.AddEdge(Id_eStructuralFeature,i)
						NIdName[i] = "eOpposite"
						Id_eOpposite = i
						i = i + 1

						# Identificando o vértice com o conteúdo de "eOpposite", e estabelece uma aresta entre eles
						G1.AddNode(i)
						G1.AddEdge(Id_eOpposite,i)
						NIdName[i] = eStructuralFeatures['eOpposite']
						i = i + 1
			else:
				# Incrementa as variáveis contadoras
				Qtde_eStructuralFeature = Qtde_eStructuralFeature + 1
				i = i + 1

				# Cria o vértice do "eStructuralFeature" para cada item da lista de "eClassifiers"
				G1.AddNode(i)
				G1.AddEdge(Id_eClassifier,i)
				NIdName[i] = "eStructuralFeature-" + str(Qtde_eStructuralFeature)
				Id_eStructuralFeature = i 
				i = i + 1

				# Identificando o vértice "xsi:type" que pertence ao "eStructuralFeature", e estabelece a aresta entre 
				# "eStructuralFeature" <--> "xsi:type"
				G1.AddNode(i)
				G1.AddEdge(Id_eStructuralFeature,i)
				NIdName[i] = "xsi:type"
				Id_xsi_type = i
				i = i + 1

				# Identificando o vértice com o conteúdo de "xsi:type", e estabelece uma aresta entre eles
				G1.AddNode(i)
				G1.AddEdge(Id_xsi_type,i)
				NIdName[i] = eClassifiers['eStructuralFeatures']['xsi:type']
				i = i + 1

				# Identificando o vértice "name" que pertence ao "eStructuralFeature", e estabelece a aresta entre 
				# "eStructuralFeature" <--> "name"
				G1.AddNode(i)
				G1.AddEdge(Id_eStructuralFeature,i)
				NIdName[i] = "name"
				Id_name = i
				i = i + 1

				# Identificando o vértice com o conteúdo de "name", e estabelece uma aresta entre eles
				G1.AddNode(i)
				G1.AddEdge(Id_name,i)
				NIdName[i] = eClassifiers['eStructuralFeatures']['name']
				i = i + 1

				# Verifica se o "eStructuralFeatures" em questão possui o elemento 'ordered', se TRUE ele cria o elemento no grafo
				if 'ordered' in eClassifiers['eStructuralFeatures']:
					
					# Identificando o vértice "ordered" que pertence ao "eStructuralFeature", e estabelece a aresta entre 
					# "eStructuralFeature" <--> "ordered"
					G1.AddNode(i)
					G1.AddEdge(Id_eStructuralFeature,i)
					NIdName[i] = "ordered"
					Id_ordered = i
					i = i + 1

					# Identificando o vértice com o conteúdo de "ordered", e estabelece uma aresta entre eles
					G1.AddNode(i)
					G1.AddEdge(Id_ordered,i)
					NIdName[i] = eClassifiers['eStructuralFeatures']['ordered']
					i = i + 1

				# Verifica se o "eStructuralFeatures" em questão possui o elemento 'upperBound', se TRUE ele cria o elemento no grafo
				if 'upperBound' in eClassifiers['eStructuralFeatures']:
					
					# Identificando o vértice "upperBound" que pertence ao "eStructuralFeature", e estabelece a aresta entre 
					# "eStructuralFeature" <--> "upperBound"
					G1.AddNode(i)
					G1.AddEdge(Id_eStructuralFeature,i)
					NIdName[i] = "upperBound"
					Id_upperBound = i
					i = i + 1

					# Identificando o vértice com o conteúdo de "upperBound", e estabelece uma aresta entre eles
					G1.AddNode(i)
					G1.AddEdge(Id_upperBound,i)
					NIdName[i] = eClassifiers['eStructuralFeatures']['upperBound']
					i = i + 1

				# Verifica se o "eStructuralFeatures" em questão possui o elemento 'unique', se TRUE ele cria o elemento no grafo
				if 'unique' in eClassifiers['eStructuralFeatures']:
					
					# Identificando o vértice "unique" que pertence ao "eStructuralFeature", e estabelece a aresta entre 
					# "eStructuralFeature" <--> "unique"
					G1.AddNode(i)
					G1.AddEdge(Id_eStructuralFeature,i)
					NIdName[i] = "unique"
					Id_unique = i
					i = i + 1

					# Identificando o vértice com o conteúdo de "unique", e estabelece uma aresta entre eles
					G1.AddNode(i)
					G1.AddEdge(Id_unique,i)
					NIdName[i] = eClassifiers['eStructuralFeatures']['unique']
					i = i + 1

				# Verifica se o "eStructuralFeatures" em questão possui o elemento 'lowerBound', se TRUE ele cria o elemento no grafo
				if 'lowerBound' in eClassifiers['eStructuralFeatures']:
					
					# Identificando o vértice "lowerBound" que pertence ao "eStructuralFeature", e estabelece a aresta entre 
					# "eStructuralFeature" <--> "lowerBound"
					G1.AddNode(i)
					G1.AddEdge(Id_eStructuralFeature,i)
					NIdName[i] = "lowerBound"
					Id_lowerBound = i
					i = i + 1

					# Identificando o vértice com o conteúdo de "lowerBound", e estabelece uma aresta entre eles
					G1.AddNode(i)
					G1.AddEdge(Id_lowerBound,i)
					NIdName[i] = eClassifiers['eStructuralFeatures']['lowerBound']
					i = i + 1

				# Verifica se o "eStructuralFeatures" em questão possui o elemento 'eType', se TRUE ele cria o elemento no grafo
				if 'eType' in eClassifiers['eStructuralFeatures']:
					
					# Identificando o vértice "eType" que pertence ao "eStructuralFeature", e estabelece a aresta entre 
					# "eStructuralFeature" <--> "eType"
					G1.AddNode(i)
					G1.AddEdge(Id_eStructuralFeature,i)
					NIdName[i] = "eType"
					Id_eType = i
					i = i + 1

					# Identificando o vértice com o conteúdo de "eType", e estabelece uma aresta entre eles
					G1.AddNode(i)
					G1.AddEdge(Id_eType,i)
					NIdName[i] = eClassifiers['eStructuralFeatures']['eType']
					i = i + 1

				# Verifica se o "eStructuralFeatures" em questão possui o elemento 'containment', se TRUE ele cria o elemento no grafo
				if 'containment' in eClassifiers['eStructuralFeatures']:
					
					# Identificando o vértice "containment" que pertence ao "eStructuralFeature", e estabelece a aresta entre 
					# "eStructuralFeature" <--> "containment"
					G1.AddNode(i)
					G1.AddEdge(Id_eStructuralFeature,i)
					NIdName[i] = "containment"
					Id_containment = i
					i = i + 1

					# Identificando o vértice com o conteúdo de "containment", e estabelece uma aresta entre eles
					G1.AddNode(i)
					G1.AddEdge(Id_containment,i)
					NIdName[i] = eClassifiers['eStructuralFeatures']['containment']
					i = i + 1

				# Verifica se o "eStructuralFeatures" em questão possui o elemento 'eOpposite', se TRUE ele cria o elemento no grafo
				if 'eOpposite' in eClassifiers['eStructuralFeatures']:
					
					# Identificando o vértice "eOpposite" que pertence ao "eStructuralFeature", e estabelece a aresta entre 
					# "eStructuralFeature" <--> "eOpposite"
					G1.AddNode(i)
					G1.AddEdge(Id_eStructuralFeature,i)
					NIdName[i] = "eOpposite"
					Id_eOpposite = i
					i = i + 1

					# Identificando o vértice com o conteúdo de "eOpposite", e estabelece uma aresta entre eles
					G1.AddNode(i)
					G1.AddEdge(Id_eOpposite,i)
					NIdName[i] = eClassifiers['eStructuralFeatures']['eOpposite']
					i = i + 1
   	 
# Plotagem do grafo
snap.DrawGViz(G1, snap.gvlDot, "JAVAJsonGraph.png", "JAVAJsonGraph", NIdName)