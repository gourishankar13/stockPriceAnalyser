#-------------------------------------------------------------------------------
# Name:    stockPriceAnalyser
# Purpose: Get the list for each Company year and month in which the share price was highest.
#
# Author:  gouri
#
# Created:     21-08-2014
# Copyright:   (c) gouri 2014
#-------------------------------------------------------------------------------
import csv
import re
class stockPriceAnalyser(object):
    def __init__(self, filePath):
        """
        Parameter:
            filePath <str> : The csv file path from where we need to fetch the data
        """
        self.dataSource = filePath
        self.result = {}
        pat = "^\d+(\.\d+)?$"
        self.numMtch = re.compile(pat).match

    def __fetchData(self):
        """
        Reads in a CSV file and returns the contents as list,
        where every row is stored as a sublist, and each element
        in the sublist represents 1 cell in the table.
        """
        with open(self.dataSource, 'r') as csvFp:
            reader = csv.reader(csvFp)
            return list(reader)

    def __isValidPrice(self, price):
        """Check if the price is valid else return -1, so that the sorting succed"""
        return True if self.numMtch(price) else False

    def __checkCSVFormat(self, csvData):
        """
        Check the csv format:
        Format sould be :
               Column 1: Year, Column 2: Month,
               Rest of the column will treat as company data
               (at least one company should present)
        """
        if len(csvData) == 0:
            raise Exception("Blank csv file")
        headerList = csvData[0]
        if len(headerList) < 3:
            # 2 column (year & month) + 1 column (min one company)
            raise Exception("Not enough column")
        elif headerList[0].lower() != "year":
            raise Exception("1st column should be year")
        elif headerList[1].lower() != "month":
            raise Exception("2nd column should be month")

    def getCompWiseHighestStckPriceData(self):
        """
        Get the year, month and share price for each company in which the share price was highest
        return <list of list>: [[<company name>, <year>, <month>, <price>], ...]
        """
        try:
            csvData = self.__fetchData()
            self.__checkCSVFormat(csvData)

            headerList = csvData[0]
            csvData = csvData[1:]
            retData = []
            for colIndx, header in enumerate(headerList):
                # As the first two columns are Year and month, so skipping those
                if colIndx in [0, 1]: continue
                res = self.getDataForMaxPrice(colIndx, csvData)
                # If no max data found for a company,
                # then don't return that company details
                if not res : continue
                res.insert(0,header)
                retData.append(res)
            return retData
        except Exception as e:
            return str(e)


    def getDataForMaxPrice(self, colIndx, csvData):
        """
        Get the max price data of a company.
        Parameters:
           colIndx <int>  : Col index of the company which you want to get the data
           csvData <list> : The data from the csv file, with header
        return :
           If there isn't any data then return blank list
           If every thing went fine then it will return a list like:
              [<year>, <month>, <price>] for the max stock price
        """

        try:
            resData = max(csvData, key = lambda echRec: float(echRec[colIndx]) if self.__isValidPrice(echRec[colIndx]) else -1)
            return [resData[0], resData[1], resData[colIndx]]
        except Exception as e:
            #print "Exception - "+ str(e)
            return []




if __name__ == "__main__":
    CSV_FILE = "test_shares_data.csv"
    obj = stockPriceAnalyser(CSV_FILE)
    print "+"*100
    print obj.getCompWiseHighestStckPriceData()
    print "+"*100