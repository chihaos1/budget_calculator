import numpy as np
import math 

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
        
    def loan_calc(self):
        """Calculates how long it will take to pay off a loan
            
            Side effect:
                prints months to pay off loan
        """

        time = np.round(np.nper(self.loan_interest/12, (-1*self.payment), self.loan), 0)

        print(f"The time required to repay the loan is {round(time)} months")         
    
    def annual_apr(self):
        """Calculates the annual percentage rate of loans. The function requires 
           loan amount, interest rate, loan term, and total fees
            
            Returns:
                A message that informs user of the APR of the loan. 
        """
        interest_total = self.loan * (self.loan_interest) * self.loan_term 
        total_loan_days = 365 * self.loan_term 
        apr = ((((self.fee + interest_total)/self.loan)/total_loan_days) * 365) * 100
        print(f"The apr of the loan is {round(apr, 2)}%")
    
    def credit_score(self, last_missed, outstanding_balance, credit_length, new_credit, credit_mix): # Thomas
        """ Estimates the user's credit score based on several attributes.
            The scale will assess how the 300-850 point range looks on paper,
            by deeming it very poor, poor, fair, good, and excellent. The points
            are 300-580, 580-640, 640-720, 720-780, and 780-850, respectively.
            
            Args:
                last_missed(int): number of months since last missed payment. 0 for never
                outstanding_balance(int): sum of unpaid debt in USD
                credit_length(int): length that credit has been established
                new_credit(int): number of inquiries in the last 6 months
                credit_mix(int): number of bankcard trade lines
            
            Returns:
                Credit score on the 300-850 point scale
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
        
        return credit_score

    def retirement(self, current_age, retirement_age, pension_goal, current_pension_saving, current_monthly_saving):
        """Calculates how much of monthly budget should be directed to retirement
           savings in order to reach pension goal.The user will be notified if 
           the current monthly saving is on track to meeting the goal.

           Args:
                current_age(int): the current age of user. 
                retirement_age(int): the age the user plans to retire. 
                pension_goal(int): the planned amount of pension.  
                current_pension_saving(int): the current amount of pension saved. 
                current_monthly_saving(int): the current amount of monthy saving 
                                             directed to pension.
                
           Returns:
                A message that informs the user if his or her monthly retirement 
                saving is on track to meeting the pension goal. If not, user will 
                be notified on how much they should increase
                to the monthly retirement saving. 
        
    """
        months_until_retirement = (retirement_age - current_age) * 12
        amount_until_pension_goal = pension_goal - current_pension_saving
        monthly_saving_needed = amount_until_pension_goal/months_until_retirement
        if monthly_saving_needed > current_monthly_saving:
            print('Your current monthly saving is not on track for reaching your pension goal',
                  f'Increase the amount by ${round(monthly_saving_needed - current_monthly_saving,2)}',
                  sep='\n')
        else:
            print('You are on track to meeting your pension goal')