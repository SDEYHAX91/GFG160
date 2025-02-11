#FUNCTION TO CHECK WHETHER 2 STRINGS ARE ANAGRAMS

# 1. USING DICTIONARY / HASHMAP
#---------------------------------------------------
def areAnagrams(s1, s2):
        
        if len(s1) != len(s2):
            return False
        d1 = {} #Initializing dict for both strings
        d2 = {}
        
        for i in s1: #Dict for char frequency for s1
            if i not in d1:
                d1[i] = 1
            elif i in d1:
                d1[i] += 1
                
        for i in s2: #Dict for char frequency for s2
            if i not in d2:
                d2[i] = 1
            elif i in d2:
                d2[i] += 1
        
        return d1 == d2
        

# 2. USING FREQUENCY ARRAY
#------------------------------------------------------
def check(s1, s2):
    freq_arr = [0] * 26 #Creating array of size 26
    
    for i in s1: #Incrementing frequency for s1
        freq_arr[ord(i) - ord('a')] += 1
    
    for i in s2: #Decrementing frequency for s2
        freq_arr[ord(i) - ord('a')] -= 1
        
    for i in freq_arr: #Check whether freq.. array has elements other than zero
        if i != 0: 
            return False #If so, then not anagram
    return True # Else, true

