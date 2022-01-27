'''
Ex01: Perform various analysis tasks on a list of words
'''
from collections import Counter

fname = "Wordle_MysteryWords.csv"

def readfile(fname):
    '''Reads a file and return the contents as a string'''
    file= open(fname,'r')
    filedata= file.read()
    file.close()
    return filedata
    
    #Open the file
    #Read the text as one long string
    #Close the file
    #Return the text

def count_letters(words):
    '''Returns a dictionary with letters and their counts'''
    data={}
    for word in words:
        for char in word:
            if char not in data:
                data[char]=0
            data[char]+=1
    return data
    #Create a dictionary
    #For each word in words
    #  For each character in the word
    #    If the character is not in the dictionary
    #      Add it with a count of 1
    #    Otherwise
    #      Add 1 to the character's count
    #Return the dictionary

def count_words(words):
    '''Returns a dictionary with letters and the number of words each
       letter occurs in'''
    data={}
    for word in words:
        wordset= set(word)
        for char in wordset:
            if char not in data:
                data[char]=0
            data[char]+=1
    return data
    #Create a dictionary
    #For each word in words
    #  Create a set from the word
    #  For each character in the set
    #    If the character is not in the dictionary
    #      Add it with a count of 1
    #    Otherwise
    #      Add 1 to the character's count
    #Return the dictionary

def count_mult(words):
    '''Returns a dictionary with the number of times a letter
       occurs multiple times in a word'''
    data={}
    for word in words:
        counter = Counter(word)
        for char in counter:
            if(counter[char]>1):
                if char not in data:
                    data[char]=0
                data[char]+=1
    return data
    #Create a dictionary
    #For each word in words
    #  Create a Counter using the word
    #  For each character in the Counter
    #    If the character's count > 1
    #      Add it to the dictionary or add 1 to its count
    #Return the dictionary

def count_pos(words):
    '''Returns a dictionary with the number of times each letter occurs
       in each position in a word'''
    data={}
    for word in words:
        for i in range(len(word)):
            if word[i] not in data:
                data[word[i]]=[0,0,0,0,0]
            data[word[i]][i]+=1
    return data
    #Create a dictionary
    #For each word in words
    #  For i ranging from 0 to the length of the word
    #    Get the ith character from the word
    #    If the character is no in the dictionary
    #      Add it with a list of 5 0's
    #    Add 1 to the character's corresponding position in the list
    #Return the dictionary

def count_letters2(words):
    '''Use a Counter; functionally the same as count_letters()'''
    counter=Counter()
    for word in words:
        counter.update(word)
    return counter
    #Create a Counter
    #For each word in words
    #  Update the Counter using the word
    #Return the counter

def show_counts(d, title):
    '''Print the keys and values from dictionary d'''
    print(title)
    keylist = list(d)
    keylist.sort()
    for key in keylist:
        print(key, d[key])
        
def main():
    wordstr = readfile(fname)
    #print(wordstr[:30])  #Print 1st 30 chars
    wordlist = wordstr.split()  #Convert str into list of words
    #print(wordlist[:20])  #Print 1st 20 words
    #print(wordlist[-20:])
    #show_counts(count_letters(wordlist), "Number of times each letter occurs")
    #show_counts(count_words(wordlist), "Number of words each letter occurs in")
    #show_counts(count_mult(wordlist), "Counts of letters in multiple words")
    #show_counts(count_pos(wordlist),
     #           "Number of times each letter occurs in each position")
    count= count_letters2(wordlist);
    for c in count.most_common():
        print(c[0],c[1])
    #show_counts(count_letters2(wordlist), "Number of times each letter occurs")
    
main()
