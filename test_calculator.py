import pytest
#import functions as needed per person
#Each person test two of their functions
#check for happy paths and edge paths
from budget_calculator import Budget_Calculator
from loan_calculator import Loan_Calculator
import pytest

#Anthony


#Maya
def function():
    assert easter_date(2021) == "April 4"
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