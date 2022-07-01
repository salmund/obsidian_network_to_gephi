import networkx as nx
import json

import argparse

parser = argparse.ArgumentParser(description='Convert your JSON Obsidian Network to GEXF.')


parser.add_argument("file", type=str, help="specify the JSON file.", default="No file specified.")

args = parser.parse_args()

def export_to_gexf(file):
    g = nx.Graph()

    with open(file) as f:
        data = json.load(f)

    for node, neighbors in data.items():
        name = node.split("/")[-1].replace(".md", "")
        g.add_node(name)
        for neighbor in neighbors:
            n_name = neighbor.split("/")[-1].replace(".md", "")
            g.add_edge(name, n_name)

    nx.write_gexf(g, "graph.gexf")

if __name__ == '__main__':
    export_to_gexf(args.file)

