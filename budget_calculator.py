from argparse import ArgumentParser
import sys
import matplotlib.pyplot as plt
import numpy as np
    

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
            print("Your budgeting matches the 50-30-20 Rule") 
        else:
            print("Your budgeting does not match the 50-30-20 Rule")
    
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
 
def main(income, home, insurance, transport, food, loan, entertain, savings, retirement):
    calc = Budget_Calculator(income, home, insurance, transport, food, loan, entertain, savings, retirement)
    return calc.american_comparison(), calc.spending_graph(), calc.budget_rule()
    
def parse_args(arglist): #Maya
    """Parse and validate command line arguments.
    
    Args:
        arglist(list of str): list of arguments
    Returns: 
        namespace: parsed arguments
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

if __name__ == "__main__": #Anthony
    args = parse_args(sys.argv[1:])
    main(args.income, args.home, args.insurance, args.transport, args.food, args.loan, args.entertain, args.savings,  args.retirement)
    
    
