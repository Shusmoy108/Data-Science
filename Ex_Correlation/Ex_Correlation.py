'''
Calculate and print correlation coefficient for 2 series of data
'''
import csv   #For reading csv files
import math  #For square root function

def readcsv(fname):
    '''Reads a csv file and returns its contents'''
    with open(fname, 'r') as f:
        reader = csv.reader(f)
        lines = list(reader)
    return lines

def calc_coeff(data):
    '''Returns correlation coefficient'''
    sumH=0
    sumW=0
    sumWH=0
    sumWW=0
    sumHH=0
    for i in range(1,len(data)):
        sumH+=float(data[i][0])
        sumW+=float(data[i][1])
        sumHH+=float(data[i][0])*float(data[i][0])
        sumWW+=float(data[i][1])*float(data[i][1])
        sumWH+=float(data[i][0])*float(data[i][1])
    #print(sumWH)
    #print(sumW)
    #print(sumH)
    #print(sumWW)
    #print(sumHH)
    
    x=(len(data)-1)*sumWH- sumW*sumH
    y=((len(data)-1)*sumHH- sumH*sumH)*((len(data)-1)*sumWW- sumW*sumW)
    #print(y)
    corel=x/math.sqrt(y)
    return round(corel,2)
    #Need: number of elements, sum of pairwise products...
    #...sum of x data, sum of y data...
    #...sum of squares of x data, sum of squares of y data
    #Get number of items...
    #...Assume each row after header is 1 pair of elements
    #Probably best to do the following sums in a loop;...
    #...don't forget to skip the header row
      #sum of pairwise products (x[i] * y[i])
      #sum of x values
      #sum of y values
      #sum of squared x values (x[i]**2)
      #sum of squared y values (y[i]**2)
    #Calculate the numerator
    #Calculate the x part of the denominator
    #Calculate the y part of the denominator
    #Calculate the Pearson's correlation coefficient
    #Optional: print debugging info
    #Return the coefficient, rounded to 2 decimal places

def main():
    '''Controls the program'''
    filename = "height_weight.csv"
    print(calc_coeff(readcsv(filename)))
    #Get the data (call readcsv)
    #Get the coefficient
    #Print the coefficient

main()
 
    
