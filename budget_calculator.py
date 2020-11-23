from argparse import ArgumentParser
import sys
import matplotlib.pyplot as plt
import numpy as np
    
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
    parser.add_argument("savings", type=float,
                        help="monthly savings payments")
    parser.add_argument("retirement", type=float,
                        help="monthly retirement savings costs")
#Add argument for retirement and savings (done)
    
    
class Budget_Calculator:
    """Calculates credit score and annual percentage rate, provides graph
       to break down budget allocation and plans for repaying loans/mortgages
       and annual percentage rate (APR), and compares user's budget with the 
       50-30-20 rule. 
       
       Attributes: 
    
    
    """
    def __init__(self, income, home, insurance, transport, food, loan, entertain, save, retire):
        #Maya
        #Individual and a total for need and want
        
        self.need = home + insurance + transport + food + loan
        self.want = entertain
        self.savings = retire + save
        
        self.income = income
        self.home = home
        self.insurance = insurance
        self.transport = transport
        self.food = food
        self.loan = loan
        self.entertain = entertain
        self.save = save
        self.retire = retire
        
    
    def spending_graph(self, housing, food, transport, insurance, savings, retirement, recreation): # Thomas
        """ Visualizes the user's monthly spending habits into a pie chart, giving percentages of how much each
            field consumes one's spending.
            
            Attributes:
                housing(int): monthly cost of housing
                food(int): monthly cost of food
                transportation(int): monthly cost of transportation
                insurance(int): monthly cost of insuranc
                savings(int): monthly cost devoted to savings
                retirement(int): monthly cost devoted to retirement
                recreation(int): monthly cost for recreation
                
            Returns:
                pie chart that shows the spending percentage of each attribute.
                
        """
        labels = "Housing", "Food", "Transportation", "Insurance", "Savings", "Retirement", "Recreation"
        sizes = housing, food, transport, insurance, savings, retirement, recreation
        explode = (0,0,0,0,0.1,0.1,0)
        
        plt.pie(sizes, explode = explode, labels = labels, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.show()
    
    def budget_rule(self): #Anthony
        """
        Function to tell you if your budgeting matches the 50-30-20 Rule

        Params:
            needs (integer): The amount of money that you spend of necessities per month
            wants (integer); The amount of money that you spend of wants per month
            savings (integer): The amount of money that you save per month

        Returns:
            Boolean: Returns based on if your spending fits into the 50-30-20 Rule
        """
        total = self.need+self.want+self.savings
        if (self.need/total) <= .5 and (self.want/total) <= .3 and (self.savings/total) >= .2:
            return True
        else:
            return False
    
    def american_comparison(self): #Anthony
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

        total = self.need+self.want+self.savings
        user_needs = self.need/total
        user_wants = self.want/total
        user_savings = self.savings/total

        spending_type = ["Needs", "Wants", "Savings"]
        spending_rate1 = [user_needs, user_wants, user_savings]
        spending_rate2 = [average_needs, average_wants, average_savings]

        plt.plot(spending_type, spending_rate1)
        plt.plot(spending_type, spending_rate2)

        plt.title('You vs Average American Spending')
        plt.xlabel('Type of Spending')
        plt.ylabel('Percentage of Income')
        plt.show()
 
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])  
    
            
class Loan_Calculator: 
    
    def credit_score(self, last_missed, outstanding_balance, credit_length, new_credit, credit_mix): # Thomas
        """ Estimates the user's credit score based on several attributes. The scale will assess how the 300-850
            point range looks on paper, by deeming it "very poor", "poor", "fair", "good", and "excellent. The
            points are 300-580, 580-640, 640-720, 720-780, and 780-850, respectively.
            
            Attributes:
                last_missed(int): number of months since last missed payment. 0 for never
                outstanding_balance(int): sum of unpaid debt in USD
                credit_length(int): length that credit has been established
                new_credit(int): number of inquiries in the last 6 months
                credit_mix(int): number of bankcard trade lines
            Returns:
                credit_score(int): credit score on the 300-850 point scale
        """
        credit_score = 0
        if last_missed == 0: credit_score += 300
        elif 0 < last_missed <= 5: credit_score += 105
        elif 5 < last_missed <= 11: credit_score += 150
        elif 11 < last_missed <= 23: credit_score += 200
        else: credit_score += 250
        
        if outstanding_balance == 0: credit_score += 255
        elif 0 < outstanding_balance <= 99: credit_score += 210
        elif 99 < outstanding_balance <= 499: credit_score += 170
        elif 499 < outstanding_balance <= 999: credit_score += 130
        else: credit_score += 90
        
        if credit_length >= 48: credit_score += 125
        elif 12 < credit_length <= 23: credit_score += 95
        elif 23 < credit_length <= 47: credit_score += 70
        else: credit_score += 45
        
        if new_credit == 0: credit_score += 85
        elif new_credit == 1: credit_score += 60
        elif new_credit == 2: credit_score += 50
        elif new_credit == 3: credit_score += 40
        else: credit_score += 30
        
        if credit_mix >= 4: credit_score += 85
        elif credit_mix == 3: credit_score += 60
        elif credit_mix == 2: credit_score += 50
        elif credit_mix == 1: credit_score += 40
        else: credit_score += 30
        
        return(credit_score)
    
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

class Retirement_Calculator: 
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
    
    
class loanCalculator:
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
        
        
        


