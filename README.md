# RNAmotifs

## What is the project about?
In this project RNA motifs from RNA 3D Motif Atlas (http://rna.bgsu.edu/rna3dhub/motifs), both internal loops and hairpin loops, were searched for in a second database - RNA Bricks (http://iimcb.genesilico.pl/rnabricks2). This was done to see whether the motifs from the first database are present in the second one.

## Prerequsites
To be able to run the scripts provided please have Python 3.4 and requests package installed. The script should also work fine on Python 2.7 installed.

## How to use the files provided?
Initial data from the RNA 3D Motif Atlas is stored in two CSV files:
````
int.csv
pin.csv
````
First one containing internal loop motifs data, the second one contains information on hairpin loop motifs. Those files can be downloaded from the Atlas.

To perform basic parsing of provided files please run following script:
````
initial_csv_to_website_list.py
````
The script contains function which takes as argument either of those CSV files, and names of output files. Those output files will be described below. It also takes information whether it was internal or hairpin loop, that was the source of motif - this is later used to generate URL of 2D structure of a motif. 

First output file, in this project it is either of the two below:
````
websites_int.txt
websites_pin.txt
````
contains data about structures which, according to 3D Motif Atlas, might contain given motif, in format:
````
URL of structure in RNA Bricks          coordinates of motif in the structure          ID of the motif in the 3D Motif Atlas 
````
The list is generated automatically, but status code for each website is checked, so no nonexisting website should be written to the output file. 
Second file, here:
````
int_id_url.txt
pin_id_url.txt
````
Contains information about the motifs such as its ID in 3D Motif Atlas and and URL of its 2D structure in the Atlas. This file contains information such as below:
````
motif ID in 3D Motif Atlas | URL of motif's 2D structure
````

## That's great! But what should I do with those files now?
Here comes the tricky part! Each URL in first output file will redirect us to RNA Bricks page with one RNA structure. There we should be able to find our initial motif. How? We search by motif "position" which is also printed into the file with website URLs. Coordinates provided by the first script can be input into "Motif residue" field on this website along with letter representing suitable chain of nucleotides. 
Why? To use the second script we need to create a file, here named:
````
images_int.txt
images_pin.txt
````
Any images_X.txt file should have the same number of lines as corresponding websites_X.txt file. 

## Creating images_x.txt file
If a structure from webistes_x.txt file contains particular motif, please copy URL of its 2D structure (graphical file) to corresponding line in images_x.txt file. If the motif is nowhere to be found in the structure, please enter '0' in the corresponding line of images_x file. This way we obtain information whether the motif was found and if yes, how does its 2D structure look.
This is very long process, so if you feel like it, you might contribute and try to script it, so it's faster next time someone tries to use it! :) 

## Finally!
We can use the second script to generate output CSV file. This way we will be able to parse the information we have in any way we want sometime later. Please make sure that you haven't modified output files and that there are the two new input files (images_x) prepared.
The second script:
````
combine_outputs_to_result_file.py
````
will take websites, images and id .txt files as its inputs and give a CSV file as a result. The result file will contain information such as:
````
motif ID in RNA 3D Motif atlas, URL of motifs 2D structure in Atlas, 
    PDB id of structure which may possibly contain the motif, URL of motif's 2D structure in RNA Bricks
````
The data is comma-delimited, so it will be easy to interpret as needed. 

## Some numbers one might find interesting
When processing all of the motifs one shouldn't be surprised that there is some difference between what is stored in two different databases. 

Internal loops:
- 372 entries (motifs) in 3D Motif Atlas
- 2410 possible structures containing given motifs (from CSV file)
- 520 possible structures containing givem motifs on RNA Bricks(after checking status code)
- 299 structures containin initial motifs
- 128 unique motifs found in second database. 

Hairpin loops:
- 316 entries (motifs) in 3D Motif Atlas
- 1475 possible structures containing given motifs (from CSV file)
- 397 possible structures containing givem motifs on RNA Bricks(after checking status code)
- 232 structures containing initial motifs
- 119 unique motifs found in second database. 


## Author
Joanna Grochal (joanna.k.grochal@gmail.com)
