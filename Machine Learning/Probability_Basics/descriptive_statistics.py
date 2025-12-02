"""This class implements the Basic Arithmetic Functions of Probability"""

import statistics


class descriptiveStatistics(object):

    def __init__(self, Data):
        self.Data = Data

    """The mean of the one Dimensional Dataset"""
    def mean(self):
        sum = 0
        # sum over all elements
        for datapoint in self.Data:
            sum += datapoint

        return sum/len(self.Data) # mean

    """The mode of the one Dimensional Dataset"""
    def mode(self):
        dict = {} # initialise dictionary
        count, itm = 0, ''
        for item in reversed(self.Data): # for every Key
            dict[item] = dict.get(item, 0) + 1
            if dict[item] >= count:
                count, itm = dict[item], item
        return itm

    """The median of the one Dimensional Dataset"""
    def median(self):
        sorted_Data = sorted(self.Data)
        len_Data = len(sorted_Data)
        if (len_Data%2 == 0):
            median = (sorted_Data[len_Data//2] + (sorted_Data[len_Data//2 - 1]))/2
        else :
            median = sorted_Data[len_Data//2]
        return median

    """ The midrange of the one Dimensional Dataset"""
    def midrange(self):
        midrange = (self.Data[0] + self.Data[-1]) / 2 #midrange (middle between first and last value)
        return midrange













