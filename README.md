This is a tool used, for example, when analyzing DNA for possible replication site origins. Your function, mostCommonSubstring(dna, mink, maxk), takes a string as an argument (the DNA sequence) and also takes the shortest, mink, and longest, maxk, acceptable result length. Your task then is to look at all substrings of length mink, mink+1, ..., maxk-1, maxk and return the one that occurs with most frequency throughout the entire sequence. If there is a tie, it returns the longer string. If the tie is between substrings of the same length, the choice is arbitrary, and you can return any of the tied equal-length substrings.
For example, mostCommonSubstring('gactctcagc', 2, 6) returns 'ctc' since it occurs twice and is longer than 'ct' and 'tc' which each also occur twice, and all other substrings of length 2, 3, 4, 5, or 6 only occur once. Note that the occurrences can overlap. (Practice on this example before you try the whole huge file.)
We'll implement this by writing another function, mostCommonK(dna, k), which looks for just the most common substring of length k, and returns it and it's frequency. So then mostCommonSubstring just calls mostCommonK repeatedly with each of mink, mink+1, etc. as arguments. The algorithm within mostCommonK is to take the first k letters of dna and see how many times that is seen within dna, then taking the 2nd through (k+1)th letters and doing the same, then the 3rd through (k+2)nd letters, etc. This is not the most efficient approach, but it will suffice for our purposes. You are not allowed to use the string method count().
In addition you will have another function, runMostCommonSubstring, that asks the user for a filename, opens that file and reads in the DNA string from that file and calls mostCommonSubstring with it.
(For more on this and related bioinformatics algorithms, see Bioinformatics Algorithms: An Active Learning Approach, 2nd Ed. Vol. 1 by Phillip Compeau (Links to an external site.).)

Here is the datafile with the first 6000 basepairs of Vibria cholerae (the critter that causes cholera; DNA sequence from NCBI (Links to an external site.)). Use that file for real-life testing. Calling mostCommonSubstring(dna,4,9) on that dataset should run in no more than a minute or two. That's way too slow to use on a whole DNA sequence of millions of basepairs, but reasonable given how much Python you know now. Here's what run might look like:
Data file: initial6000.txt
mink: 4
maxk: 9
mostCommonSubstring(dna,4,9) = 'cttt' 


Guidance
Here are the steps I recommend to finishing this project. It is unlikely you can do this all in one day and you might want help from me or the tutor, so plan accordingly:
    1. Create a flowchart or pseudo-code code algorithm for each of the functions described in the flowing steps. 
    2. Write a program that sets a variable, dna, to a short-ish string and also sets the variable, k, to a small integer. This  program runs a loop printing out each k-length substring in dna.
    3. Once that is working, modify the program to do more inside the loop. Now store the substring in a variable, target. Then make a nested loop that that counts how many times target is seen in dna. Print out that count.
    4. Once that is working, modify the program to keep track of which target string produces the highest count. (Hint: use another pair of variables, highestCount and targetWithHighestCount, to keep track of the best target seen so far.) Print out targetWithHighestCount at the end of your program.
    5. Now turn your working program from the step above into a function. Instead of setting dna and k up front, make them parameters to the function. Instead of printing targetWithHighestCount, return it. Name your function mostCommonK.
    6. Next write a program that sets dna to a short-ish string and then calls mostCommonK repeatedly with different values for the k argument, say for 2, 3, 4, 5, and 6. Now do something similar to what you did in step #3 and print out the value for the k argument that caused mostCommonK to return the largest value.
    7. Now change the program in the step above into a function, mostCommonSubstring.
    8. Next write a program that does what runMostCommonSubstring needs to do. It asks the user for the name of the file and the values for mink and maxk, opens the file and reads its contents into the variable dna, then calls mostCommonSubstring(dna, mink, maxk) and prints the answer. Test this program on a file with a small dna string in it before attempting the big one. Once it works on a small file, then try the big one.
    9. Change the previous step into a function, runMostCommonSubstring. Test it. And hand it in!
    • Make sure that you have good comments and docstring including program header and function description. 


