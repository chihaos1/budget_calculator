# budget_calculator
A program that keeps track of the user's budget and provides financial
suggestions according to the user's needs. 

PURPOSE OF EACH FILE
-------------------------
budget_calculator.py:
	Creates a class that breaks down a user's budget allocation
	through multiple methods.

	__init__() method:
		Gathers expense data and initializes them into the
		function.

	spending_graph() method:
		Visualizes the user's monthly spending habits into
		a pie chart. Emphasizes savings and retirements.

	budget_rule() method:
		Notifies user if they are spending by the 50-30-20
		rule. Needs <= 50%, Wants <= 30%, Savings >= 20%.

	american_comparison() method:
		Dispays a comparison of spendings to the average
		American, based upon the 50-30-20 rule.

	main() method:
		Main method for the class, returns the three other
		methods based upon input.

	parse_args() method:
		Parses and validates command line arguments.
	

loan_calculator.py:
	Calculates how long it will take to pay off a loan and the apr
	of the loan.

	__init__() method:
		Gathers loan data and initializes them into the
		function.

	loan_calc() method:
		Calculates how long it will take ot pay off a loan in
		months.

	annual_apr() method:
		Calculates the annual percentage rate of loans.	

	credit_score() method:
		Estimates the user's credit score based on several
		attributes, within a range of 300-850.

	retirement() method:
		Calculates how much of monthly budget should be directed
		to retirement savings in order to reach pension goal.
	

test_calculator.py:
	Developer defined test scripts to verify integrity of multiple
	functions