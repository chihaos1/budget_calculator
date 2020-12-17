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
	of the loan. Also calculates credit score and retirement saving.

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

RUNNING THE PROGRAM
-------------------------
The program is ran through budget_calculator.py. The command line argument takes
9 variables then processes them using the argparse module. After inputting the
values of the variables, two graphs and a message will be generated. The terminal
will then prompt the users to select from 4 options that either lead them to access
the methods in loan_calculator.py or exit the program. 

USING THE PROGRAM
-------------------------
The spending_graph method ouputs a pie chart that breaks down user's spending. User
will be able to see how the monthly budget is being allocated and thereby decide whether
to increase or decrease certain spendings. 

The american_comparision method outputs a bar graph that compares user's spending
with the average American spending categorized by needs, wants, and savings. 

The budget_rule method prints a message that notifies the user if his or her
budgeting meets the conventional 50-30-20 Rule. 

The loan_calc method prints a message that tells the user how many months it would
take to repay a specific amount of loan. He or she can use this information to decide
whether to increase or decrease the amount of monthly repayment. 

The annual_apr method prints the apr of the loan. User can use this information to
see if the loan package is suitable for him or her. 

The credit_score method returns the credit score of the user. User will be able to 
know if he or her could become qualified for taking out loans. The minimum credit score
to qualify for loan is typically 610 to 640. 

The retirement method prints a message that notifies the user if he or she is 
on tracking to meeting the pension goal. If the user is not on track, the message 
will inform the user on how much more monthly budget should be directed to retirement
saving in order to reach the goal. 