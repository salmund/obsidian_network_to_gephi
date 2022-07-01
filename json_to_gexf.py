import networkx as nx
import json

g = nx.Graph()

with open('my graph.json') as f:
    data = json.load(f)

for node, neighbors in data.items():
    name = node.split("/")[-1].replace(".md", "")
    g.add_node(name)
    for neighbor in neighbors:
        n_name = neighbor.split("/")[-1].replace(".md", "")
        g.add_edge(name, n_name)

nx.write_gexf(g, "graph.gexf")
