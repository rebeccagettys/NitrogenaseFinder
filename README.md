**Nitrogene - A Nitrogenase(Gene) Search Tool and Visualization Maker

Authors: Rebecca Gettys, Erica Lee, and Liv Kelley
Microbial Metagenome from Dr. Jean Huang

A code snippet used for the recursive levenshtein memoized distance from(https://programmingpraxis.com/2014/09/12/levenshtein-distance/)
 walked us through the implementation; we based ours on this.
We also  used the code contained in the base repository for the Software Design Miniproject 1 (Gene Finder) which can be
 found on [Github](https://github.com/sd16spring/GeneFinder).

Description:

Nitrogene is a program that finds percentage similarities between a gene and open reading frames (ORFs) in a genome or
metagenome which is comprised of a set of contigous regions ("contigs"). It identifies the similarities using a memoized
levenstein distance algorithm. Nitrogenase_finder.py returns a list of dictionaries for each plaustibly-sized ORF that
contains the length of the ORF, the start and end locations of the ORF, a flag indicating forward or reverse complement
location, and the percentage match between the ORF and the gene, in addition to the length of the gene being used and
the levenshtein distance, which are not used in the visualization but are present for debugging reasons in the
dictionaries. When the algorithm identifies a match higher than the user-set percent similarity threshold, it visualizes
the ORF in varying shades of green; non-matches (determined by having a percent similarity below the threshold) and
non-ORF DNA are visualized in black. The locations of these ORFs may be found by mousing over the ORF of interest, which
will cause the start and end index (in nucleotides, counting from zero) of the ORF to appear, in addition to the name of
the contig on which the ORF is located.

Getting Started and Usage:

After downloading this program from GitHub and install Pygame (and Python 2.7 if you don't already have it!).  run this function by choosing a bacterial colony and use the program Finch to find its base pair sequence. Put this sequence into a script format and input it into the function's variable (dna). The program should output an image displaying the strength of the percentage match by the length of the bolded sections of a bar representing the DNA. This program should work with multiple genome inputs, so long as each sequence is in its own string and then put into a list.

Requirements:
This program runs on python 2.7. It uses the sys and pickle modules, which are built into Python 2. Additionally,
it uses PyGame for the visualization component (http://pygame.org/hifi.html), and which you will need to have installed
in order to utilize our program.


MIT license used for this program.


