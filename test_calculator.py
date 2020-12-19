import pytest
from loan_calculator import Loan_Calculator
from budget_calculator import Budget_Calculator
import random

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

def test_credit_score():
    """ Tests whether the boundaries of the credit scores have been established.
        This should be no less than 300 and no higher than 850
    """
    standard = Loan_Calculator(50000, 0.05, 500, 5, 200)
    # awful credit score
    assert standard.credit_score(1, 5000, 1, 5, 0) == 300
    # perfect credit score
    assert standard.credit_score(0, 0, 50, 0, 4) == 850
    # average credit score
    assert standard.credit_score(20, 200, 20, 2, 2) == 565
    # random credit score
    assert 300 <= standard.credit_score(random.randrange(0,25),
                                 random.randrange(0,5000),
                                 random.randrange(0,100),
                                 random.randrange(0,7),
                                 random.randrange(0,7)) <= 850

def test_retirement():
    test = Loan_Calculator(50000, 0.05, 500, 5, 200)
    assert isinstance(test, Loan_Calculator)
    assert test.retirement(20, 65, 400000, 40000, 2000) == print('You are on track to meeting your pension goal')
    assert test.retirement(20, 65, 600000, 1000, 300) == print('Your current monthly saving is not on track for reaching your pension goal',
                                                               'Increase the amount by $809.26',
                                                               sep='\n')
    assert test.retirement(65, 20, 600000, 1000, 300) == print('Invalid Input: current age cannot be bigger than retirement age')
    assert test.retirement(20, 65, 600, 1000, 300) == print('You can retire now!')

def test_budget_calc():
    #Testing high savings and low spending on needs and wants
    assert Budget_Calculator(10000, 1000, 100, 200, 300, 50, 500, 6000, 1000).budget_rule() == print("Your budgeting matches the 50-30-20 Rule")
    #Testing high savings and low spending on needs high wants
    assert Budget_Calculator(10000, 6000, 100, 200, 300, 50, 500, 3000, 0).budget_rule() == print("Your budgeting does not match the 50-30-20 Rule")
    #Testing high savings and high spending on needs and wants
    assert Budget_Calculator(10000, 4000, 300, 200, 500, 0, 3500, 2000, 0).budget_rule() == print("Your budgeting does not match the 50-30-20 Rule")
    #Testing low savings and high spending on needs and wants
    assert Budget_Calculator(10000, 4000, 300, 200, 500, 0, 3500, 1000, 0).budget_rule() == print("Your budgeting does not match the 50-30-20 Rule")