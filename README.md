# Optimal-Stopping
Demonstration of the optimal stopping problem, or the secretary problem in python.
The secretary problem (https://en.wikipedia.org/wiki/Secretary_problem) also known by other names such as 
In the secretary version of this problem, we have the following scenario. We have N applicants for the position of a secretary. You as a boss need to interview and select the best candidate amongst the applications. The catch here is that you need to give your decision (yes/no) before interviewing the next candidate. Once rejected, the applicant cannot be recalled. Since it seems like we're completely shooting in the dark, a good strategy is to first interview a bunch of candidates and create a baseline. Once we have a fair idea of the quality of candidates then select the best one from our experience.

Turns out, for this explore-exploit strategy, our best chance is if we first interview a fraction 1/e of the total applicants. This gives us the best possible odds of choosing the best candidate.

With this code snippet, I tried to see how 'e' "naturally" occurs in explore-exploit problems!
