import numpy as np

class Loan_Calculator:
    """Calculates how long it will take to pay off a loan and the apr of the loan
    
        Attributes:
            loan(float): total amount of the loan
            loan_interest(float): decimal of the monthly interest on the loan
            payment(float): amount willing to pay per month
            loan_term(int): the number of years to pay off a loan
            fee(int): the total fee for taking out the loan

    """
    def __init__(self, loan, loan_interest, payment, loan_term, fee): #Maya
        self.loan = loan
        self.loan_interest = loan_interest
        self.payment = payment
        self.loan_term = loan_term
        self.fee = fee
        
    def loan_calc(self): # Maya
        """Calculates how long it will take ot pay off a loan
            
            Returns:
                Time in months till the loan is paid
        """
        time=(-np.log(1-self.loan_interest*self.loan/self.payment))/ np.log(1+self.loan_interest)
        return time
    
    def annual_apr(self):
        """Calculates the annual percentage rate of loans. The function requires loan amount, interest rate, 
           loan term, and total fees
            
            Returns:
                A message that informs user of the APR of the loan. 
        """
        interest_total = self.loan * (self.loan_interest) * self.loan_term 
        total_loan_days = 365 * self.loan_term 
        apr = ((((self.fee + interest_total)/self.loan)/total_loan_days) * 365) * 100
        print("The apr of your loan is " + round(apr, 2))