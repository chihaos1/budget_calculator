import pytest
from loan_calculator import Loan_Calculator

#import functions as needed per person
#Each person test two of their functions
#check for happy paths and edge paths



#Anthony


#Maya
#def function():
    #assert easter_date(2021) == "April 4"
#Thomas


#Chi-Hao
def test_retirement():
    test = Loan_Calculator(50000, 0.05, 500, 5, 200)
    assert isinstance(test, Loan_Calculator)
    assert test.retirement(20, 65, 400000, 40000, 2000) == print('You are on track to meeting your pension goal')
    assert test.retirement(20, 65, 600000, 1000, 300) == print('Your current monthly saving is not on track for reaching your pension goal',
                                                               'Increase the amount by $809.26',
                                                               sep='\n')
    assert test.retirement(65, 20, 600000, 1000, 300) == print('Invalid Input: current age cannot be bigger than retirement age')
    assert test.retirement(20, 65, 600, 1000, 300) == print('You can retire now!')