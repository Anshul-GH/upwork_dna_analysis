import tkinter as tk
from tkinter import filedialog
from config import get_config

# first point of entry
def runMostCommonSubstring():
    '''This method is the entry point which prompts the user for choosing a valid text 
    file with the required DNA sequence data to be analyzed. The file chosen must be of the 
    extension '.txt' and should only contain a single string dna sequence.

    Input Parameters: [None]; 
    
    Returns: [None];

    Console Output: [Prints the identified substring sequence that has the maximum recurrences];

    '''

    # define the root
    root = tk.Tk()
    # hide the intrusive root window using withdraw
    root.withdraw()

    # display the minimalistic file open dialog for the user to chose the input text file
    inp_file = filedialog.askopenfilename()
    inp_file = open(file=inp_file)
    
    # read the data from the file
    dna=inp_file.read()

    # define the mink and maxk values in an external config file
    # Note: These can also be hard-coded, if needed. The advantage with the config file approach
    # is that it can be modified without touching the primary code.
    mink = get_config("MIN_K", default = 4)
    maxk = get_config("MAX_K", default = 9)

    # pass the data for further processing
    required_string = mostCommonSubstring(dna, mink, maxk)

    # return data
    print(required_string)


def mostCommonSubstring(dna, mink, maxk):
    '''This is the primary method that implements the algorithm to identify the most common 
    and longest substring.

    Input Parameters:
    
    dna: [type: string]: [description: 
        input source dna string data read from the chosen text file]
    
    mink: [type: integer]: [description: 
        minimum length of the substring to consider. It is read from the config file which gives
        the control to alter the value outside the main code file]
    
    maxk: [type: integer]: [description: 
        maximum length of the substring to consider. It is read from the config file which gives
        the control to alter the value outside the main code file];

    Returns:
    
    max_str: [type: integer]: [description:
        identified string that is the most common and also the longest in length in case there is
        a tie on the recurrance frequency];

    Console Output: [None];

    '''

    # placeholder for max len string 
    max_str = ''

    # placeholder for count of occourance of the max len str
    max_count = 0
       
    # starting with the longest substring (len: maxk) 
    # and moving to the smallest (len: mink) in loop
    for length in range(maxk, mink-1, -1):
        substr, counter = mostCommonK(dna, length)
    
        # store the string with max length and max count
        # Please Note: this is to store the overall max count string info
        if counter > max_count:
            max_str = substr
            max_count = counter

    # print(max_str, max_count)
    return max_str


def mostCommonK(dna, length):
    '''This method implements the core logic to search the most common substring of a given length
    supplied as input and returns the string and the frequency count.

    Input Parameters:
    
    dna: [type: string]: [description: 
        input source dna string data read from the source text file]
    
    length: [type: integer]: [description: 
        it is the length of the substring to be considered while identifying the frequency of occourance
        for all the substrings of the same 'length']

    Returns:
    
    max_str: [type: integer]: [description:
        identified substring that is the most common - that is one with the highest frequency of 
        occourance];

    max_count: [type: integer]: [description:
        the frequency of occourance for the 'max_str' identified above];

    Console Output: [None];

    '''
    # max string for a given length 
    max_str = ''
    # count of occourance for the above string
    max_count = 0

    # maximum possible iterations for a substring with specific length   
    iterations = len(dna) - length
    # fetch the substrings, one at a time, for a given length
    for index in range(iterations):                
        # counter for occourance for each substring
        counter = 0
        substr = dna[index:length+index]
        # for each chosen substr, look for a match
        for subindex in range(iterations):
            if dna[subindex:length+subindex] == substr:
                counter += 1

        # store the sring with max length and max count
        # Please Note: this is to store the max count string info for a given 'length'
        if counter > max_count:
            max_str = substr
            max_count = counter

    return max_str, max_count
    

if __name__ == "__main__":
    runMostCommonSubstring()
