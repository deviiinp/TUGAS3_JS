import networkx as nx 
import matplotlib.pyplot as plt 

G=nx.DiGraph() 

G.add_edge('UU Nomor 22 Tahun 2001','UUD 1945') 
G.add_edge('UU Nomor 22 Tahun 2001','Ketetapan MPR Nomor XV/MPR/1998')
G.add_edge('UU Nomor 39 Tahun 2007','UUD 1945')
G.add_edge('UU Nomor 39 Tahun 2007','UUD 1945')
G.add_edge('UU Nomor 1 Tahun 2017','UU Nomor 24 Tahun 2000')
G.add_edge('UU Nomor 18 Tahun 2017','UUD 1945') 
G.add_edge('UU Nomor 18 Tahun 2017','UU Nomor 13 Tahun 2003')
G.add_edge('UU Nomor 18 Tahun 2017','UU Nomor 6 Tahun 2012')
G.add_edge('UU Nomor 2 Tahun 2018',' UUD 1945')
G.add_edge('UU Nomor 2 Tahun 2018 ','UU Nomor 17 Tahun 2014') 

def main():
	G = nx.read_edgelist('Cit-HepTh.txt', create_using=nx.DiGraph())

	deg = dict(G.in_degree())  #Returns a dictionay, with key as nodes and indegrees as values.
	pr = nx.pagerank(G)
	pr_values = []
	for i in deg.keys():
		pr_values.append(pr[i])

	plt.plot(deg.values(), pr_values, 'ro', markersize = 3)
	plt.xlabel('Indegree value of the nodes')
	plt.ylabel('PageRank value of the nodes')
	plt.show()
main()

