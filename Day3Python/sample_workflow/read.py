'''Here we store some sample ways to read in data and spit out the pieces that we want from the  dataset

Let's assume all of the data we are using has a header, and columns, so we can read it uin using pandas read_csv method

Let's create a function (or series of functions) to read in our kind of data set, then returns and  and y value that we care about)'''

import pandas as pd

def read_my_csv(csvfile):
    '''Our csv files are space separated. This function reads  in our csv file, and returns the x and y axis we care about '''
    data=pd.read_csv(csvfile, sep=' ')
    return data.xaxis, data.yaxis

print("Name is: "+__name__)

if __name__ == "__main__":
    print(__name__)
    print ("in name == main if statement"

