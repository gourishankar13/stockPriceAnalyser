#-------------------------------------------------------------------------------
# Name    : test.py
# Purpose : To test the stockPriceAnalyser class of stockPriceAnalyser module
#
# Author  : gouri
# Created : 21-08-2014
#-------------------------------------------------------------------------------

import unittest
from stockPriceAnalyser import *

class TestMod(unittest.TestCase):

    def setUp(self):
        pass

    def test_normalInput(self):
        """Test for valid data"""
        csvFile = "test_shares_data.csv"
        expectedRetVal = [['Company-A', '2000', 'Mar', '1000'],
                          ['Company-B', '2007', 'Mar', '986'],
                          ['Company-C', '1993', 'Jun', '995'],
                          ['Company-D', '2002', 'Apr', '999'],
                          ['Company-E', '2008', 'Oct', '997']]
        obj = stockPriceAnalyser(csvFile)
        retData = obj.getCompWiseHighestStckPriceData()
        self.assertEqual(retData, expectedRetVal)

    def test_with_no_data(self):
        """Test for no data"""
        csvFile = "test_no_date.csv"
        expectedRetVal = []
        obj = stockPriceAnalyser(csvFile)
        retData = obj.getCompWiseHighestStckPriceData()
        self.assertEqual(retData, expectedRetVal)


    def test_with_blank_csv(self):
        """Test for black csv"""
        csvFile = "test_blank_csv.csv"
        expectedRetVal = "blank csv file"
        obj = stockPriceAnalyser(csvFile)
        retData = obj.getCompWiseHighestStckPriceData()
        self.assertEqual(str(retData).lower(), expectedRetVal)

    def test_with_invalid_csv(self):
        """Test for invalid csv format"""
        csvFile = "test_invalid_csv.csv"
        expectedRetVal = "1st column should be year"
        obj = stockPriceAnalyser(csvFile)
        retData = obj.getCompWiseHighestStckPriceData()
        self.assertEqual(str(retData).lower(), expectedRetVal)

    def test_some_date_contains_no_cost(self):
        """Test for invalid price"""
        csvFile = "test_wrong_price_type.csv"
        expectedRetVal = [['Company-A', '1990', 'Jan', '751'],
                          ['Company-B', '1990', 'Apr', '914'],
                          ['Company-C', '1990', 'Jan', '829'],
                          ['Company-D', '1990', 'Jul', '941'],
                          ['Company-E', '1990', 'Jul', '870']]
        obj = stockPriceAnalyser(csvFile)
        retData = obj.getCompWiseHighestStckPriceData()
        self.assertEqual(retData, expectedRetVal)

    def test_more_data(self):
        """Test for invalid price"""
        csvFile = "test_more_data.csv"
        expectedRetVal = [['Company-A', '2000', 'Mar', '1000'],
                          ['Company-B', '2007', 'Mar', '986'],
                          ['Company-C', '1993', 'Jun', '995'],
                          ['Company-D', '2002', 'Apr', '999'],
                          ['Company-E', '2008', 'Oct', '997'],
                          ['Company-F', '2000', 'Mar', '1000'],
                          ['Company-G', '2007', 'Mar', '986'],
                          ['Company-H', '1993', 'Jun', '995'],
                          ['Company-I', '2002', 'Apr', '999'],
                          ['Company-J', '2008', 'Oct', '997'],
                          ['Company-K', '2000', 'Mar', '1000'],
                          ['Company-L', '2007', 'Mar', '986'],
                          ['Company-M', '1993', 'Jun', '995'],
                          ['Company-N', '2002', 'Apr', '999'],
                          ['Company-O', '2008', 'Oct', '997'],
                          ['Company-P', '2000', 'Mar', '1000'],
                          ['Company-Q', '2007', 'Mar', '986'],
                          ['Company-R', '1993', 'Jun', '995'],
                          ['Company-S', '2002', 'Apr', '999'],
                          ['Company-T', '2008', 'Oct', '997'],
                          ['Company-U', '2000', 'Mar', '1000'],
                          ['Company-V', '2007', 'Mar', '986'],
                          ['Company-W', '1993', 'Jun', '995'],
                          ['Company-X', '2002', 'Apr', '999'],
                          ['Company-Y', '2008', 'Oct', '997'],
                          ['Company-Z', '2000', 'Mar', '1000'],
                          ['Company-AA', '2007', 'Mar', '986'],
                          ['Company-AB', '1993', 'Jun', '995'],
                          ['Company-AC', '2002', 'Apr', '999'],
                          ['Company-AD', '2008', 'Oct', '997'],
                          ['Company-AE', '2000', 'Mar', '1000'],
                          ['Company-AF', '2007', 'Mar', '986'],
                          ['Company-AG', '1993', 'Jun', '995'],
                          ['Company-AH', '2002', 'Apr', '999'],
                          ['Company-AI', '2008', 'Oct', '997'],
                          ['Company-AJ', '2000', 'Mar', '1000'],
                          ['Company-AK', '2007', 'Mar', '986'],
                          ['Company-AL', '1993', 'Jun', '995'],
                          ['Company-AM', '2002', 'Apr', '999'],
                          ['Company-AN', '2008', 'Oct', '997']]
        obj = stockPriceAnalyser(csvFile)
        retData = obj.getCompWiseHighestStckPriceData()
        self.assertEqual(retData, expectedRetVal)

if __name__ == '__main__':
    unittest.main()