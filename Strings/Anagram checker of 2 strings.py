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
