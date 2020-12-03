class Loan_Calculator:
    """Calculates how long it will take to pay off a loan
    
        Params:
    
    """
    def __init__(self, loan, loan_interest, payment):
        '''Initilizes loan calculator variables
        Args:
            loan(float): total cost of the loan
            loan_interest(float): decimal of the monthly interest on the loan
            payment(float): amount willing to pay per month
        '''
        self.loan = loan
        self.loan_interest = loan_interest
        self.payment = payment
        
    def loan_calc(self): # Maya
        """Calculates how long it will take ot pay off a loan
            
        Returns:
            time(int): time in months till the loan is paid
        """
        time=(-np.log(1-self.loan_interest*self.loan/self.payment))/ np.log(1+self.loan_interest)
        return time
    
     def annual_apr(self, loan_amount, interest_rate, loan_term, fee):
            """Calculates the annual percentage rate of loans. The function requires loan amount, interest rate, 
           loan term, and total fees
            
            Attributes:
                loan_amount(int): the total amount of loan
                interest_rate(int): the percentage of interest from loan 
                loan_term(int): the number of years to pay off a loan
                fees(int): the total fees for taking out the loan

            Returns:
                A message that informs user of the APR of the loan. 
        """
        interest_total = loan_amount * (interest_rate/100) * loan_term #total interest paid over the lifetime of the loan
        total_loan_days = 365 * loan_term #number of days in loan term
        apr = ((((fee + interest_total)/loan_amount)/total_loan_days) * 365) * 100
        print(round(apr, 2))