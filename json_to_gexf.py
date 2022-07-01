import networkx as nx
import json

import argparse

parser = argparse.ArgumentParser(description='Convert your JSON Obsidian Network to GEXF.')


parser.add_argument("--i", "--input", type=str, help="specify the JSON file for input.", default="No input file specified.")
parser.add_argument("--o", "--output", type=str, help="specify the GEXF file for output.", default="graph.gexf")

args = parser.parse_args()

def export_to_gexf(input_file,output_file):
    g = nx.Graph()

    with open(input_file) as f:
        data = json.load(f)

    for node, neighbors in data.items():
        name = node.split("/")[-1].replace(".md", "")
        g.add_node(name)
        for neighbor in neighbors:
            n_name = neighbor.split("/")[-1].replace(".md", "")
            g.add_edge(name, n_name)

    nx.write_gexf(g, output_file)

if __name__ == '__main__':
    export_to_gexf(args.i, args.o)
