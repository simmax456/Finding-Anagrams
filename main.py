# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram():
    print("NOTE: The program is not case sensitive\n")
    string1 = input('Enter the first word: ')
    string2 = input('Enter the second word: ')

    # convert the strings to lower lcase
    string1 = string1.lower()
    string2 = string2.lower()

    if(len(string1) == len(string2)):
        # sort the strings
        sorted_string1 = sorted(string1)
        sorted_string2 = sorted(string2)
    
        # if sorted char arrays are same
        if(sorted_string1 == sorted_string2):
            print("\n")
            print(True, ": " + string1 + " and " + string2 + " are anagrams")
        else:
            print("\n")
            print(False, ": " + string1 + " and " + string2 + " are not anagrams")
    
    else:
        print("\n" + string1 + " and " + string2 + " are not the same in length, and therefore are not anagrams.")

find_anagram()