import pytest
from loan_calculator import Loan_Calculator

#import functions as needed per person
#Each person test two of their functions
#check for happy paths and edge paths
from budget_calculator import Budget_Calculator
from loan_calculator import Loan_Calculator
import pytest

#Anthony


#Maya
def test_loan_calc():

    #last 2 args do not effect loan_calc
    assert Loan_Calculator(0,0,0,0,0).loan_calc() == print("The time required to repay the loan is 0.0 months")
    #tests if loan = 0
    assert Loan_Calculator(0,.15,500,0,0).loan_calc() == print("The time required to repay the loan is 0.0 months")
    assert Loan_Calculator(0,.07,2,0,0).loan_calc() == print("The time required to repay the loan is 0 months")
    assert Loan_Calculator(0,.03,1000,0,0).loan_calc() == print("The time required to repay the loan is 0 months")
    #tests if interest = 0
    assert Loan_Calculator(70000,0,500,0,0).loan_calc() == print("The time required to repay the loan is 140 months")
    assert Loan_Calculator(5000,0,100,0,0).loan_calc() == print("The time required to repay the loan is 50 months")
    assert Loan_Calculator(5,0,1,0,0).loan_calc() == print("The time required to repay the loan is 5 months")
    #test if payment = 0
    assert Loan_Calculator(100,.2,0,0,0).loan_calc() == print("The time required to repay the loan is -inf months")
    assert Loan_Calculator(6000,0.15,0,0,0).loan_calc() == print("The time required to repay the loan is -inf months")
    assert Loan_Calculator(56,0.5,0,0,0).loan_calc() == print("The time required to repay the loan is -inf months")
    #test random situations
    assert Loan_Calculator(504845,.05,5496,0,0).loan_calc() == print("The time required to repay the loan is 93 months")
    assert Loan_Calculator(568,0.15,60,0,0).loan_calc() == print("The time required to repay the loan is 11 months")
    assert Loan_Calculator(4354,0.23,230,0,0).loan_calc() == print("The time required to repay the loan is 24 months")

#Thomas
def test_credit_score():
    """ Tests whether the boundaries of the credit scores have been established.
        This should be no less than 300 and no higher than 850
    """
    # awful credit score
    assert credit_score(1, 5000, 1, 5, 5) == 300
    # perfect credit score
    assert credit_score(0, 0, 50, 0, 4) == 850
    # average credit score
    assert credit_score(20, 200, 20, 2, 2) == 565

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