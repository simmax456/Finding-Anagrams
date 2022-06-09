# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(string1, string2):
    print('\nThe first word is: ', string1)
    print('The second word is: ', string2)

    # convert the strings to lower lcase
    string1 = string1.lower()
    string2 = string2.lower()

    if(len(string1) == len(string2)):
        # sort the strings
        sorted_string1 = sorted(string1)
        sorted_string2 = sorted(string2)
    
        # if sorted char arrays are same, return boolean
        return print(sorted_string1 == sorted_string2)
    
    else:
        print("\n" + string1 + " and " + string2 + " are not the same in length, and therefore are not anagrams.")

find_anagram('hello', 'check')
find_anagram('below', 'elbow')
find_anagram('low', 'wool')