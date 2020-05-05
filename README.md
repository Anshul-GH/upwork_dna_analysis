Problem Statement
-----------------

- DNA sequences are represented in form of strings with a combination of only the following letters - a, g, c and t
- Source input is a single string of dna sequence (could be of any length - typically in the range of thousands or more).
- We need to identify a substring within the input, with a given minimum (min_k) and maximum (max_k) lengths, that is repeating within the sequence at the highest frequency. 
- If there is a tie between the frequency of occourance of two substrings, the one which is larger is preferred. 
- If they are of the same length, any one can be chosen at random.
- Essentially we are looking for a possible 'viral' sequence that is replicating.

- For Example:
source_input = 'gactctcagc'
min_k = 2
max_k = 6

- This would return 'ctc'(frequency:2), 'ct' (frequency:2) and 'tc' (frequency:2) as the most repeating ones. 
- Hence 'ctc' which has the maximum length, must be chosen as the answer.


Lets get started !!