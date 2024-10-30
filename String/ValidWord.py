# Time Complexity O(n)
# Space Complexity O(1)

def isValid(self, word: str) -> bool:
        hashmap = {
            "a" : "a",
            "e" : "e",
            "i" : "i",
            "o" : "o",
            "u" : "u"
        }
        
        if len(word) < 3 or ("@" in word or ("$" in word or "#" in word)):
            return False
        
        vowel, consonant, upper, lower, digit = False, False, False, False, False

        for i in word:
            if i.isupper():
                upper = True
            if i.islower():
                lower = True
            if i.isdigit() and int(i) in range(0, 9):
                digit = True
            if i.isalpha() and i.lower() in hashmap:
                vowel = True
            elif i.isalpha():
                consonant = True
        
        if digit and consonant and vowel and lower and upper is True:
            return True
        elif consonant and vowel is True:
            return True
        return False