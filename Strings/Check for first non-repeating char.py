# 1. USING DICTIONARY
#----------------------------
def nonRepeatingChar(s): 
        #code here
        freq = {} #Creating dict for frequency 
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        for i in s: #Assuming that element 1st inserted into dict will have greater
            if freq[i] == 1:#chance of getting non repeated char
                return i    #while traversing the string iteratively
        
        return '$'

# 2. USING FREQUENCY ARRAY
------------------------------------------
def nonRepeatingChar(s):
    freq = [0] * 26 #Creating frequency array
    
    for i in s: #Storing count frequency in array
        freq[ord(i) - ord('a')] += 1
    
    for i in range(len(s)): #If 1st nonrepeating char found return char
        if freq[ord(s[i]) - ord('a')] == 1:
            return s[i]
    
    return '$' #else return "$"

# 3. USING SORTING INCIDES
--------------------------------------------

def firstnonrepeatingChar(st):
    
    array = [-1] * 26 #Creating visited array, each element of -1(unseen)
    
    for i in range(len(st)): # Iterating through the string
        if array[ord(st[i]) - ord('a')] == -1: # If char 1st seen, put index no.
            array[ord(st[i]) - ord('a')] = i 
        
        else:
            array[ord(st[i]) - ord('a')] = -2  # If repeated char, put -2
    
    #Goal is to find min +ve value from array
    
    # ASSUMING NON REPEATING CHAR MUST HAVE STARTED FROM THE SMALLEST INDEX POSSIBLE
    index = float('inf') 

    for i in range(26):
        if array[i] >= 0:
            index = min(index, array[i])
    
    # If non-repeating character is found, return it 
    # Else return '$'
    return '$' if index == float('inf') else st[index]

