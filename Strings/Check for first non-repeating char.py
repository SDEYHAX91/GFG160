def nonRepeatingChar(self,s):
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
