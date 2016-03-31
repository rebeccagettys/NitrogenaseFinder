**Rebecca Gettys, Liv Kelley, Erica Lee**

**Nitrogen Fixation Gene Analysis Project Proposal**
**Link to Slides: (https://docs.google.com/presentation/d/1WKHuqHWuO_hqYM5-ReRb3LxcIaa2dwi6mjbmYXJzYtY/edit#slide=id.p)**
**Goals for This Review**

We would like to get some feedback and advice on areas of concern for us: optimization, algorithms, data structures, and dealing with large quantities of data. Mostly, we would like to pick your brains on how to have a successful, functional project because none of us have a ton of software development experience.

**Context**

Jean Huang has a number of bacterial metagenomes (sets of genomes for an entire community of bacteria) that she is analyzing for nitrogen fixation genes - their presence, location (which microbes have them), and number, in each metagenome. This project aims to allow us to analyze the data for use in a possible future paper. 

**Background Information**

We are aiming to build a "extended gene finder" which will help to locate nitrogen fixation genes within a metagenome (set of bacterial genomes). In addition to locating the gene if it is an exact match, our program will be able to identify genes which are similar but not identical (they have mutations), and return a percent similarity to the search query sequence.This is mainly a data analysis and algorithm project - our main challenge is the huge volume of data that we have to work with. 

So far, the current code uses gene_finder.py from the first miniproject. A metagenome is passed through the gene finder which returns a list of the open reading frames within the metagenome. If the metagenome contains an open reading frame that contains nitrogenase, the code should return the metagenome as well as the index for the metagenome in the list of metagenomes.  We are planning on using memoized Levenshtein distance for the percentage similarity this but would be interested about hearing about better/faster/more accurate alternatives/adjuncts.

The minimum viable product for this project is an extended gene-finder that finds genes in a genome that are similar to a given gene and returns a percentage similarity; for data visualization, a dot plot could be employed. Our stretch goal is to create code that prints the genes (as base pairs) of the nitrogen fixing bacteria and shows the number of nitrogen fixing gene matches; we would like to be able to analyze as much data as possible (optimize the algorithms used).

**Key Questions**

Focused

1. The current code for finding the nitrogenase in the metagenomes takes a long time to execute. How can we make it efficient enough to have a shorter execution time?

2. How do we approach making the code more optimized?

3. Similarity algorithm? Besides Levenshtein distance, what else would you recommend using to quantify similarity in sequences (percent similarity)? Damerau-Levenshtein?

4. We are currently using the gene finder data structure - can you foresee a reason to change any of the data structures from that project for this application? If so, can you elaborate and make any recommendations? It’s easiest to change data structures now vs. later when we’re further into optimization.

Overall

5. Do you have any "pearls of wisdom" to share? Any libraries or tools to make life easier? (We’re aware of PyPy but would also be happy to hear about PyPy pitfalls). Ideally we would like to balance between learning some optimization and algorithms but also not making things hard for ourselves when good solutions exist - more than anything, being able to process the data accurately with good information yields would be ideal.

**Agenda for Technical Review**

Project Overview, Background, and Goals (7 minutes)

Focused Technical Questions Discussion: Optimization and Algorithms, Data Structure (9 minutes)		

Overall Advice/Feedback Period (share your wisdom, overarching comments, questions for us, etc) (9 minutes)

