#REDES COMPLEXAS
#YURI COUGO SANDY REIS

from igraph import *
import random
import math
import matplotlib.pylab as plt
import itertools


def analises(grafo,n):
	"analisa o grafo"
	print "\n\nGrafo: "
	print grafo
	print "\nCoeficiente de Clustering: "
	print grafo.transitivity_undirected()
	print "\nGrau max: "
	print grafo.maxdegree()
	print "\nGrau medio: "
	graus = grafo.degree()
	soma = 0
	menor = 10000
	for i in graus:
		soma = soma + i
		if i < menor: menor = i
	print float(soma)/float(n)
	print "\nGrau min: "
	print menor
	arquivo = raw_input("Entre com o nome do arquivo para saida da distribuicao de grau (sem extensao): ")
	print "\nDistribuicao de grau: Impressa em imagem '"+arquivo+".png'"
	plot(grafo.degree_distribution(bin_width=0.1),arquivo+".png")


def ErdosRenyi(n,p):
	"""gera um grafo modelo Erdos e Renyi (aleatorio)"""
	grafo = Graph()
	grafo.add_vertices(n)
	if (p >= 1): grafo = grafo.Full(n,False,False)
	elif ((p>0.0)and(p<1.0)):
		for aresta in itertools.permutations(range(n),2):
			if random.random() < p:
				grafo.add_edge(aresta[0],aresta[1])

	return grafo


def WattsStrogatz(k, n, p):
	"""gera um grafo modelo Watts-Strogratz (mundo pequeno)"""
	grafo = Graph()
	grafo.add_vertices(n)
	vertices = tuple(range(n))
	for i in range(1, k+1):
		alvos = vertices[i:] + vertices[0:i]
		for i in range(0, len(vertices)):
			grafo.add_edge(vertices[i],alvos[i])

	arestas = grafo.get_edgelist()
	for i in arestas:
		if random.random() < p:
			novoVertice = random.choice(vertices)
			grafo.delete_edges([i])
			grafo.add_edge(i[0],novoVertice)
	
	return grafo


def BarabasiAlbert(n,m):
	"""gera um grafo modelo Barabasi-Albert (rede sem escala)"""
	grafo = Graph()
	grafo.add_vertices(m)
	vertice = m-1
	vertices = list(range(0,m))
	probabilidade = []
	while (n > vertice):
		for v in vertices:
			grafo.add_edge(vertice, v)
		probabilidade = probabilidade + [vertice for i in xrange(m)] + vertices
		vertices = []
		vertices = [probabilidade[i] for i in sorted(random.sample(xrange(len(probabilidade)), m))]
		vertice = vertice + 1
		grafo.add_vertex()
	
	return grafo
	
	

opcao = ''
while (opcao != '4'):
	print "\n\nGerar Grafo: \n1 - Erdos e Renyi \n2 - Watts-Strogatz \n3 - Barabasi-Albert\n4 - Sair"
	opcao = raw_input("Opcao: ")
	if(opcao == '1'):
		n = int(raw_input("Valor de n: "))
		p = float(raw_input("Valor de p: "))
		analises(ErdosRenyi(n,p),n)
	elif(opcao == '2'):
		k = int(raw_input("Valor de k: "))
		n = int(raw_input("Valor de n: "))
		p = float(raw_input("Valor de p: "))
		analises(WattsStrogatz(k,n,p),n)
	elif(opcao == '3'):
		n = int(raw_input("Valor de n: "))
		m = int(raw_input("Valor de m: "))
		analises(BarabasiAlbert(n,m),n)
	elif(opcao == '4'):
		print "Programa Finalizado"
	else:
		print "Opcao Invalida"
	
	
	


	
