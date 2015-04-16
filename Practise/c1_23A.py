# 23A)Given an arithmatic expression, transform the expression into postfix expression, 
# suppose the expression only contains "+", "-", "*", "/", "(", ")" and numbers are integers.
operators = set(['+','-','*','/'])
stack = list()

def precedence(operator):
	if operator == '+' or operator == '-' :
		return 0
	if operator == '*' :
		return 1
	if operator == '/' :
		return 2
	if operator == '(' :
		return -1
def infixToPostfix(expression):
	for char in expression:
		if char in operators:
			while stack and precedence(char) < precedence(stack[-1]) :
				print stack.pop(),
			stack.append(char)
		elif char == '(' :
			stack.append(char)
		elif char == ')':
			while stack[-1] != '(':
				print stack.pop(),
			stack.pop()
		else:
			print char,
	while stack:
		print stack.pop(),
expression = raw_input("Enter infix expression")
infixToPostfix(expression)