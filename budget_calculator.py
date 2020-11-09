from argparse import ArgumentParser

    
def parse_args(arglist): #Maya
    """Parse and validate command line arguments.
    
    Args:
        arglist(list of str): list of arguments
    Returns: 
        namespace: parsed arguments
    Raises: 
        ValueError: checks for valid data types
    """
    parser = ArgumentParser()
    parser.add_argument("income", type=float,
                        help="monthly income")
    parser.add_argument("home", type=float,
                        help="monthly rent/mortgage")
    parser.add_argument("insurance", type=float,
                        help="monthly insurance cost")
    parser.add_argument("transport", type=float,
                        help="monthly transportion cost")
    parser.add_argument("food", type=float,
                        help=" monthly food costs")
    parser.add_argument("loan", type=float,
                        help="monthly loan payments")
    parser.add_argument("entertain", type=float,
                        help="monthly entertainment costs")

class Budget_Calculator:
    """Calculates credit score and annual percentage rate, provides graph
       to break down budget allocation and plans for repaying loans/mortgages
       and annual percentage rate (APR), and compares user's budget with the 
       50-30-20 rule. 
       
       Attributes: 
    
    
    """
    
    def credit_score(self): # Thomas
        """ DOCSTRING
        """
    
    def spending_graph(self): # Thomas
        """ DOCSTRING
        """

    def retirement(self):
        """Calculates how much of monthly budget should be directed to retirement
           savings in order to reach pension goal. The function requires user's
           current age, retirement age, planned amount of pension, current total retirement saving,
           and current monthly retirement saving.The user will be notified if the current monthly
           saving is on track to meeting the goal. 
        
            Attributes:
                current_age(int): the current age of user. 
                retirement_age(int): the age the user plans to retire. 
                pension(int): the planned amount of pension.  
                current_saving(int): the current amount of pension saved. 
                current_monthly_saving(int): the current amount of monthy saving directed to pension.      
            
            Returns:
                A message that informs the user if his or her monthly retirement saving is on track to 
                meeting the pension goal. If not, user will be notified on how much they should increase
                to the monthly retirement saving. 
        
        """
    
    def apr(self):
        """Calculates the annual percentage rate of loans. The function requires loan amount, interest rate, 
           loan term, and total fees
            
            Attributes:
                loan_amount(int): the total amount of loan
                interest(int): the percentage of interest from loan 
                loan_term(int): the number of years to pay off a loan
                fees(int): the total fees for taking out the loan

            Returns:
                A message that informs user of the APR of the loan. 
        """
    
    def loan_calc(self, loan, loan_intrest, payment): # Maya
        """Calculates how long it will take ot pay off a loan
        Args:
            loan(float): total cost of the loan
            loan_intrest(float): the interest rate of the loan as a decimal
            payment(float): how much the user is willing to pay per month
            
        Returns:
            time(int): time in months till the loan is paid
        """