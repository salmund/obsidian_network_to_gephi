# How to import your network data into Gephi for Graph Analysis

**This step by step guide allows you to import your Obsidian network data directly into a software such as Gephi, or any other graph analysis software.**

1. Using the command "this.app.metadataCache.resolvedLinks" in the Obsidian developer console, you can get a JSON object containing all your notes and links.

All you have to do now is to produce a CSV from this JSON object and import it into Gephi.

2. Copy the obtained object (right click on it) in your clipboard and paste it in a file that you will name "obsidian_data.json"


3. Use the script network_json_to_csv.js, download it and run it in the same directory as your JSON file.


4. You normally get a .csv file named obsidian_data.csv that you can import directly into Gephi

## Requirements

- [Node JS](https://nodejs.org/en/)
- [Objects-to-csv](https://www.npmjs.com/package/objects-to-csv)

# Acknowledgements

- [Marc Julian](https://www.marc-julian.de/) for his python script
