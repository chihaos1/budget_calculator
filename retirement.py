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