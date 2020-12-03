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
    args = parser.parse_args()
    return args
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
        
    
    def spending_graph(self): # Thomas
        """ Visualizes the user's monthly spending habits into a pie chart, giving percentages of how much each
            field consumes one's spending.
            
            Attributes:
                home(int): monthly cost of housing
                food(int): monthly cost of food
                transport(int): monthly cost of transportation
                insurance(int): monthly cost of insuranc
                save(int): monthly cost devoted to savings
                retire(int): monthly cost devoted to retirement
                entertain(int): monthly cost for recreation
                loan(int): monthly dues for loans
                
            Returns:
                pie chart that shows the spending percentage of each attribute
                
        """
        labels = "Housing", "Food", "Transportation", "Insurance", "Savings", "Retirement", "Entertainment", "Loan"
        sizes = self.home, self.food, self.transport, self.insurance, self.save, self.retire, self.entertain, self.loan
        explode = (0,0,0,0,0.1,0.1,0,0)
        
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
    Budget_Calculator(args.income, args.home, args.insurance, args.transport, args.food, args.loan, args.entertain, args.save, args.retire)
            
class Loan_Calculator: 
    """ Estimates credit score based on credit history, and calculates
        loan annual percentage rates with the credit score."""
    
    def __init__(self, last_missed, outstanding_balance, credit_length, new_credit, credit_mix): #Thomas
        self.last_missed = last_missed
        self.outstanding_balance = outstanding_balance
        self.credit_length = credit_length
        self.new_credit = new_credit
        self.credit_mix = credit_mix
    
    def credit_score(self): # Thomas
        """ Estimates the user's credit score based on several attributes.
            The scale will assess how the 300-850 point range looks on paper,
            by deeming it very poor, poor, fair, good, and excellent. The points
            are 300-580, 580-640, 640-720, 720-780, and 780-850, respectively.
            
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
        if self.last_missed == 0: credit_score += 300
        elif 0 < self.last_missed <= 5: credit_score += 105
        elif 5 < self.last_missed <= 11: credit_score += 150
        elif 11 < self.last_missed <= 23: credit_score += 200
        else: credit_score += 250
        
        if self.outstanding_balance == 0: credit_score += 255
        elif 0 < self.outstanding_balance <= 99: credit_score += 210
        elif 99 < self.outstanding_balance <= 499: credit_score += 170
        elif 499 < self.outstanding_balance <= 999: credit_score += 130
        else: credit_score += 90
        
        if self.credit_length >= 48: credit_score += 125
        elif 12 < self.credit_length <= 23: credit_score += 95
        elif 23 < self.credit_length <= 47: credit_score += 70
        else: credit_score += 45
        
        if self.new_credit == 0: credit_score += 85
        elif self.new_credit == 1: credit_score += 60
        elif self.new_credit == 2: credit_score += 50
        elif self.new_credit == 3: credit_score += 40
        else: credit_score += 30
        
        if self.credit_mix >= 4: credit_score += 85
        elif self.credit_mix == 3: credit_score += 60
        elif self.credit_mix == 2: credit_score += 50
        elif self.credit_mix == 1: credit_score += 40
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
    """ Checks if user's monthly pension saving is on track to meeting the pension goal
        
        Attributes:
                current_age(int): the current age of user. 
                retirement_age(int): the age the user plans to retire. 
                pension_goal(int): the planned amount of pension.  
                current_pension_saving(int): the current amount of pension saved. 
                current_monthly_saving(int): the current amount of monthy saving directed to pension.
    """
    def __init__(self,current_age, retirement_age, pension_goal, current_pension_saving, current_monthly_saving):
        self.current_age = current_age
        self.retirement_age = retirement_age
        self.pension_goal = pension_goal
        self.current_pension_saving = current_pension_saving
        self.current_monthly_saving = current_monthly_saving
        
    def retirement(self):
        """Calculates how much of monthly budget should be directed to retirement
           savings in order to reach pension goal.The user will be notified if the current monthly
           saving is on track to meeting the goal.
    
           Returns:
                A message that informs the user if his or her monthly retirement saving is on track to 
                meeting the pension goal. If not, user will be notified on how much they should increase
                to the monthly retirement saving. 
        
        """
        months_until_retirement = (self.retirement_age - self.current_age) * 12
        amount_until_pension_goal = self.pension_goal - self.current_pension_saving
        monthly_saving_needed = amount_until_pension_goal/months_until_retirement
        if monthly_saving_needed > self.current_monthly_saving:
            print('Your current monthly saving is not on track for reaching your pension goal.',
                  f'Increase the amount by ${monthly_saving_needed - self.current_monthly_saving}.',
                  sep='\n')
        else:
            print('You are on track to meeting your pension goal.')
    
    
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
        

    def budget_rule(self,needs, wants, savings):  # Anthony
        '''
        Function that determines whether the inputted information for budgeting matches the 50-30-20 Rule
        for splitting a needs, wants, and savings budget out of a total income

        Params:
            needs (integer): The monthly cost of necessities
            wants (integer): The monthly
            savings (integer): The amount of money that you save per month

        Returns:
            Boolean: Returns based on if your spending fits into the 50-30-20 Rule
        '''
        total = needs + wants + savings
        if (needs / total) <= .5 and (wants / total) <= .3 and (savings / total) >= .2:
            return True
        else:
            return False


    def american_comparison(self,needs, wants, savings):  # Anthony
        '''
        Function to display a comparison about your spending versus the average american

        Params:
            needs (integer): The amount of money that you spend of necessities per month
            wants (integer); The amount of money that you spend of wants per month
            savings (integer): The amount of money that you save per month

        Returns:
            None: Displays a line graph of the users inputted budgeting information and compares it to the average
                  american
        '''
        average_needs = .748
        average_wants = .173
        average_savings = .079

        total = needs + wants + savings
        user_needs = needs / total
        user_wants = wants / total
        user_savings = savings / total

        spending_type = ["Needs", "Wants", "Savings"]
        spending_rate1 = [user_needs, user_wants, user_savings]
        spending_rate2 = [average_needs, average_wants, average_savings]

        plt.plot(spending_type, spending_rate1)
        plt.plot(spending_type, spending_rate2)

        plt.title('You vs Average American Spending')
        plt.xlabel('Type of Spending')
        plt.ylabel('Percentage of Income')
        plt.show()


if __name__ == "__main__": #Anthony
    args = parse_args(sys.argv[1:])

    needs = args.home + args.insurance + args.transport + args.loans
    wants = args.entertain
    savings = args.income - (needs + wants)

    calc = Budget_Calculator()
    calc.budget_rule(needs=needs, wants=wants, savings=savings)
    calc.american_comparison(needs=needs, wants=wants, savings=savings)
