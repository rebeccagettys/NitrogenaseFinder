Goals for this Review
In this technical review, we will be showing you the code that we have so far. We’d like to get feedback for how the code is coming so far and any potential problems you foresee.

Background and context
What information about your project does the audience need to participate fully in the technical review? You should share enough to make sure your audience understands the questions you are asking, but without going into unnecessary detail.

As you know from the last technical review, our code uses gene finder to find and visualize nitrogenase in a genome. So far, we have the gene finder code that looks for open reading frames and implements a memoized levenshtein algorithm that finds the nitrogen fixation gene without it being an exact match. It returns a percentage similarity that we can then use to see if the gene fixes nitrogen. We also have developed a basic visualization code that builds off “ideal” result examples we’ve created (lists of tuples with the first value representing a decimal version of the percentage match and the second value representing the length in base pairs of coding base pair snippets.) The visualization shows the coding snippets lined up next to each other in bars that represent genomes. Each snippet has a color correlating with its percentage match (black is a false match, which is between a set threshold and brighter colors of green denote better matches.) 

Key questions
What do you want to learn from the review? What are the most important decisions your team is currently contemplating? Where might an outside perspective be most helpful? As you select key questions to ask during the review, bear in mind both the time limitations and background of your audience.

    From this technical review, we want to know: 

How we find matches within the matches 
How do we make our code efficient?
How do we fix bugs like the trouble with nearby snippet representations blocking the ability to see the exact match in the scroll over process? 
How do we integrate the results of the new genefinder code with the visualization program (using pickle)?


Agenda for technical review session
Be specific about how you plan to use your allotted time. What strategies will you use to communicate with your audience?

    Project Recap, Background and Context(7 minutes)

Technical Questions Discussion: Optimization and Algorithms, Data Structure (9 minutes)        
Overall Advice/Feedback Period (share your wisdom, overarching comments, questions for us, etc) (9 minutes)
