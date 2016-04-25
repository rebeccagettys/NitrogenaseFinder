**Nitrogenes Second Technical Review Feedback and Synthesis**

Rebecca Gettys, Liv Kelley, Erica Lee

**Feedback and decisions**

The feedback that we received during the technical review was recommendations for implementing the "search within the similar region" feature, solving some bugs in the visualization, and improving efficiency overall by utilizing object orientation to save attributes. 

For the "search within the similar region" feature, it was recommended that we use a search algorithm instead of Levenshtein distance, and use Levenshtein distance only for finding the regions of similarity. We will use this proposal because it will simplify things significantly, make the code more modular, and be easier for everyone (including us!) to understand. Now, we would like to figure out which search algorithm is best for this application, and whether using a pre-made module for this feature might make the most sense given where we are in the project. 

	We received significant feedback on tracking down and fixing some bugs within the visualization code and also some feedback about how to make the visualization more clear by adding a legend explaining the color scheme’s relation to the percent similarity. We will try to add the legend as it is easy to do and will really improve intelligibility; we may also add labels for each contig that we visualize to clarify their identity. We have already used the debugging suggestions and feedback to fix the bugs in the visualization. Moving forward, we feel like we really understand what needs to get done on the visualization and how to do it; the feedback we received was extremely helpful.

	We also discussed making all sections of DNA as objects in a class so that we can use attributes such as length and sequence to save important attributes so that we don’t need to recompute them, increasing efficiency. This is a really interesting idea and one that we will work on if we have time, but is not our first priority because we would like to get the visualization working really well before taking on object orientation. 

	In this way, we plan to take concrete steps to address comments we received after our most recent presentation. We believe modifying genefinder and the visualization this way will allow our final product to be the best it possible can be and the most user friendly and more informative, which will ultimately make our tool more useful.

**Review process reflection**

The review went well in general because the team divided time effectively and because we received answers to our key questions about how to make the program more efficient, debug the visualization, and implement the "search within a similar region" feature. We had a code diagram for how different scripts in the code interacted in this project. We also displayed snippets of our code to provide more context to the issues we were having moving forward. We were able to get good suggestions for how we should move forward which we will utilize in the next phases of our development. Though the procedure of getting suggestions during the review was very effective for the first technical review, it might have been a better this time to have utilized post-its because we split up and individually listened to suggestions. Overall, the technical review went well, and we were able to collect helpful ideas for moving forward.

