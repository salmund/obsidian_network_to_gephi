/*

1. Importer le fichier JSON et le stocker
dans un objet

2. Chaque note est sous la forme

"Note1":{
	"Lien1": 1,
	"Lien2": 1,
	...
	}

Donc il faut itérer sur chaque Objet / Note afin d'avoir les liens, 

par exemple pour chaque lien dans l'objet "Note1"
on écrit dans le fichier CSV correspondant

Source,Target,Type
Note1,Lien1,Undirected
Note1,Lien2,Undirected

3. On enregistre le CSV dans l'espace courant

*/
const ObjectsToCsv = require('objects-to-csv');

const obsidian_data = require("./obsidian_data.json");

const liste_notes = Object.keys(obsidian_data);

var reformatted = Array();

// On trie les données JSON fournies par OBSIDIAN pour pouvoir faire un CSV

for(let i = 0; i < liste_notes.length ; i++){
	for(let k = 0; k < Object.keys(obsidian_data[liste_notes[i]]).length ; k++){
		var current_json_link_object = obsidian_data[liste_notes[i]]
		var obj_to_append = {Source: liste_notes[i], Target: Object.keys(current_json_link_object)[k], Type: "undirected", Weight: 1}
		reformatted.push(obj_to_append)
	}
}

(async () => {
  const csv = new ObjectsToCsv(reformatted);
 
  // Save to file:
  await csv.toDisk('./obsidian_data.csv');
 
  // Return the CSV file as string:
  console.log(await csv.toString());
})();