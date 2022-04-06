"""
read_sonnet.py: functions to read sonnet file, remove punctuation from a string
Input:  A text file holding the sonnets
Output:
"""
import string
import statistics

filename = "Sonnets.txt"



def readlines(fname):
    """Return contents of file as a list of strings"""
    f = open(fname, 'r')  #Open file for reading
    lines = f.readlines()       #Read contents as a list of strings
    f.close()   #Return file resources to the operating system
    return lines

def remove_punc(s):
    '''Returns string s with the punctuation removed'''
    for char in string.punctuation:
        s = s.replace(char, '')  #Replace punc char with null string
    return s

def makesonnets(lines):
    sonet=""
    start=False
    data={}
    c=0;
    for line in lines:
        if(line.strip().isdigit()):
            sonet="Sonnet "+line.strip()
            start=True;
            c=0;
        elif start and line.strip()!="" :
            c+=len(remove_punc(line.strip()).split(" "))
            data[sonet]=c
    return data

def meanValue(data):
    s=0
    for key in data.keys():
        s+=data[key]
    return s/len(data)
        

def main():
    wordstr = makesonnets(readlines(filename))
    print(f"Mean : {round(statistics.mean(wordstr.values()),1)}")
    print(f"Median : {statistics.median(wordstr.values())}")
    print(f"Standard Deviation : {round(statistics.stdev(wordstr.values()),1)}")
    
main()

            
        

