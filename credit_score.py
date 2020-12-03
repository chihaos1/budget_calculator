class Credit_Score: 
    """ Estimates credit score based on credit history, and calculates
        loan annual percentage rates with the credit score.
        
        Attributes:
                last_missed(int): number of months since last missed payment. 0 for never
                outstanding_balance(int): sum of unpaid debt in USD
                credit_length(int): length that credit has been established
                new_credit(int): number of inquiries in the last 6 months
                credit_mix(int): number of bankcard trade lines
    """
    
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
            
            Returns:
                Credit score on the 300-850 point scale
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