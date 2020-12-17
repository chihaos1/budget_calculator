from argparse import ArgumentParser
import sys
import matplotlib.pyplot as plt
import numpy as np
from loan_calculator import Loan_Calculator
    

class Budget_Calculator:
    """Creates a graph to break down budget allocation, compares user's budget with the 
       50-30-20 rule and compares the user's spending to American spending. 
    
       Attributes: 
            income(float): monthly income
            home(float): monthly rent/mortgage
            insurance(float): monthly insurance payments
            transport(float): monthly transportation costs
            food(float): monthly food costs
            loan(float): monthly loan payments
            entertain(float): monthly enteratinment costs
            save(float): monthly savings
            retire(float): monthly retirement savings
    """
    def __init__(self,income, home, insurance, transport, food, loan, entertain, save, retire):     
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
        
    def spending_graph(self): 
        """ Visualizes the user's monthly spending habits into a pie chart, giving 
            percentages of how much each field consumes one's spending.
            
            Attributes:
                home(int): monthly cost of housing
                food(int): monthly cost of food
                transport(int): monthly cost of transportation
                insurance(int): monthly cost of insurance
                save(int): monthly cost devoted to savings
                retire(int): monthly cost devoted to retirement
                entertain(int): monthly cost for recreation
                loan(int): monthly dues for loans
                
            Side Effect:
                Display a pie chart that shows the spending percentage of each attribute
                
        """
        labels = "Housing", "Food", "Transportation", "Insurance", "Savings", "Retirement", "Entertainment", "Loan"
        sizes = self.home, self.food, self.transport, self.insurance, self.save,self.retire, self.entertain, self.loan
        explode = (0,0,0,0,0.1,0.1,0,0)
        
        plt.pie(sizes, explode = explode, labels = labels, autopct='%1.1f%%', 
                shadow=True, startangle=90)
        plt.axis('equal')
        plt.show()
    
    def budget_rule(self): 
        """Function to tell you if your budgeting matches the 50-30-20 Rule

            Args:
                needs (integer): The amount of money that you spend of necessities per month
                wants (integer); The amount of money that you spend of wants per month
                savings (integer): The amount of money that you save per month

            Returns:
                Message notifying users if spending fits into the 50-30-20 Rule
        """
        total = self.need+self.want+self.savings
        if (self.need/total) <= .5 and (self.want/total) <= .3 and (self.savings/total) >= .2:
            print("Your budgeting matches the 50-30-20 Rule") 
        else:
            print("Your budgeting does not match the 50-30-20 Rule")
    
    def american_comparison(self): 
        """Function to display a comparison about user's spending versus the average american spending

            Args:
                needs (integer): The amount of money that you spend of necessities per month
                wants (integer): The amount of money that you spend of wants per month
                savings (integer): The amount of money that you save per month

            Side Effect:
                Displays a bar graph of the user's inputted spending information 
                and compares it to the average american spending
        """
        average_needs = .748
        average_wants = .173
        average_savings = .079

        total = self.need + self.want + self.savings
        user_needs = self.need/total
        user_wants = self.want/total
        user_savings = self.savings/total

        user_spending = [user_needs, user_wants, user_savings]
        avg_spending  = [average_needs, average_wants, average_savings]
         
        X = np.arange(3)
        plt.figure(figsize=(10,5))
        width = 0.3
        
        plt.bar(X, user_spending, width, label = 'User Spending')
        plt.bar(X + width, avg_spending, width, label = 'American Spending')
        
        plt.title('User vs Average American Spending')
        plt.xlabel('Type of Spending')
        plt.ylabel('Percentage of Income')
        
        plt.xticks(X + width/2, ('Needs', 'Wants', 'Savings'))
        plt.legend(loc='best')
        plt.show()
        
    def use_loan_calc(self):
        """Asks users if they wish to use the loan calculator
        
           Side Effects:
                Call the Loan_Calculator class or end the program 
        """
        while True:
            print("\nPress 1 to use loan calculator", 
                  "Press 2 to check credit score",
                  "Press 3 to use retirement calculator",
                  "Press 4 to exit", sep="\n")
            method_call = input(">> ")
            if method_call == "1":
                try:
                    loan = Loan_Calculator(loan = float(input("Total loan amount: ")),
                                           loan_interest = float(input("Loan interest (in decimal): ")),
                                           payment = float(input("Total payment per month: ")),
                                           loan_term = int(input("Total years to pay off loan: ")),
                                           fee = float(input("Total fee for taking out loan: ")))
                    loan.loan_calc(), loan.annual_apr()
                except:
                    print("Input not valid, try again")
            elif method_call == "2":
                loan = Loan_Calculator
                try:
                    credit = loan.credit_score(self,
                                               last_missed = int(input("Total months since last missed payment (0 for none): ")),
                                               outstanding_balance = int(input("Total unpaid debt: ")),
                                               credit_length = int(input("Total years of credit history: ")),
                                               new_credit = int(input("Total number of new credit inquiries in the last 6 months: ")),
                                               credit_mix = int(input("Total number of bankcard trade lines: ")))
                    print(f"Your credit score is {credit}")
                except:
                    print("Input not valid, try again")
            elif method_call == "3":
                loan = Loan_Calculator
                try:
                    loan.retirement(self,
                                    current_age = int(input("Current age: ")),
                                    retirement_age = int(input("Retirement age: ")),
                                    pension_goal = int(input("Pension goal: ")),
                                    current_pension_saving = int(input("Total pension saved so far: ")),
                                    current_monthly_saving = int(input("Current monthly pension saving: ")))
                except:
                    print("Input not valid, try again")
            elif method_call == "4":
                return

def main(income, home, insurance, transport, food, loan, entertain, savings, retirement):
    """Creates a Budget_Calculator object and passes in values. 
       
       Args: 
            income(float): monthly income
            home(float): monthly rent/mortgage
            insurance(float): monthly insurance payments
            transport(float): monthly transportation costs
            food(float): monthly food costs
            loan(float): monthly loan payments
            entertain(float): monthly enteratinment costs
            save(float): monthly savings
            retire(float): monthly retirement savings
       
       Side Effects:
            Writes to stdout
    """
    calc = Budget_Calculator(income, home, insurance, transport, food, loan, entertain, savings, retirement)
    calc.spending_graph(), calc.american_comparison(), calc.budget_rule(), calc.use_loan_calc()
    
    
def parse_args(arglist):
    """Parse and validate command line arguments.
    
       Args:
            arglist(list of str): list of arguments
        
       Returns: 
            Parsed arguments
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
    return parser.parse_args(arglist)

if __name__ == "__main__": 
    args = parse_args(sys.argv[1:])
    main(args.income, args.home, args.insurance, args.transport, args.food, 
         args.loan, args.entertain, args.savings,  args.retirement)
    
    
