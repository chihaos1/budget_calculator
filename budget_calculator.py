from argparse import ArgumentParser
import matplotlib.pyplot as plt
    
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
        """ Estimates the user's credit score based on several attributes. The scale will assess how the 300-850
            point range looks on paper, by deeming it "very poor", "poor", "fair", "good", and "excellent. The
            points are 300-580, 580-640, 640-720, 720-780, and 780-850, respectively.
            
            Attributes:
                missed_payments(int): number of missed payments over 7 years
                outstanding_balance(int): sum of unpaid debt
                credit_length(int):length that credit has been established
                new_credit(int): number of credit lines opened within 3 years
            Returns:
                credit_score(int): credit score on the 300-850 point scale
        """
    
    def spending_graph(self): # Thomas
        """ Visualizes the user's monthly spending habits into a pie chart, giving percentages of how much each
            field consumes one's spending.
            
            Attributes:
                housing_cost(int):
                food_cost(int):
                transportation_cost(int):
                insurance_cost(int):
                savings_cost(int):
                retirement_cost(int):
                recreational_cost(int):
                
            Returns:
                pie chart that shows the spending percentage of each attribute.
                
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
        
def budget_rule(needs, wants, savings): #Anthony
    '''
    Function to tell you if your budgeting matches the 50-30-20 Rule

    Params:
        needs (integer): The amount of money that you spend of necessities per month
        wants (integer); The amount of money that you spend of wants per month
        savings (integer): The amount of money that you save per month

    Returns:
        Boolean: Returns based on if your spending fits into the 50-30-20 Rule
    '''
    total = needs+wants+savings
    if (needs/total) <= .5 and (wants/total) <= .3 and (savings/total) >= .2:
        return True
    else:
        return False

def american_comparison(needs, wants, savings): #Anthony
    '''
    Function to display a comparison about your spending versus the average american

    Params:
        needs (integer): The amount of money that you spend of necessities per month
        wants (integer); The amount of money that you spend of wants per month
        savings (integer): The amount of money that you save per month

    Returns:
        None: Displays a line graph of the users inputted budgeting information and compares it to the average american
    '''
    average_needs = .748
    average_wants = .173
    average_savings = .079

    total = needs+wants+savings
    user_needs = needs/total
    user_wants = wants/total
    user_savings = savings/total

    spending_type = ["Needs", "Wants", "Savings"]
    spending_rate1 = [user_needs, user_wants, user_savings]
    spending_rate2 = [average_needs, average_wants, average_savings]

    plt.plot(spending_type, spending_rate1)
    plt.plot(spending_type, spending_rate2)

    plt.title('You vs Average American Spending')
    plt.xlabel('Type of Spending')
    plt.ylabel('Percentage of Income')
    plt.show()
