#23) Given an arithmatic expression, evaluate the value of the expression, 
#suppose the expression only contains "+", "-", "*", "/", "(", ")" and numbers are integers.

# Algorithm:

# 1.Create an empty operator stack
# 2.Create an empty operand stack
# 3.For each token in the input string
# 	1.Get the next token in the infix string.
# 	2.If the next token is an operand, place it on the operand stack.
# 	3.If the next token is opening parenthesis, place it on the operator stack.
# 	4.If the next token is closing parenthesis
# 		1.Do until opening parenthesis is not encountered in operator stack.
# 			Pop one operator from operator stack and two operands from operand stack, evaluate it and push result onto operand stack.
# 		2.Remove opening parenthesis from the operator stack.
# 	5.If the next token is an operator
# 		1.Do until operator stack is not empty or contain higher precedence operator than next token.
# 			Pop one operator from operator stack and two operands from operand stack, evaluate it and push result in operand stack
# 		2.Push next token onto operator stack.
# 4.Do until operators stack are not empty.
# 	Pop operator and two operands. Evaluate it and push result onto operand stack.
# 5.Pop the result from the operand stack

operators = set(['+','-','*','/'])
operandStack=list()
operatorStack = list()
def precedence(operator):
	if operator == '+' or operator == '-' :
		return 0
	if operator == '*' :
		return 1
	if operator == '/' :
		return 2
	if operator == '(' :
		return -1

def process(value1,value2,operator):
	if(operator == '+'):
		return int(value1) + int(value2)
	if(operator == '-'):
		return int(value1) - int(value2)
	if(operator == '*'):
		return int(value1) * int(value2)
	if operator == '/':
		return int(value1) / int(value2)


def doArithmetic(operandStack,operatorStack):
	value2 = operandStack.pop()
	value1 = operandStack.pop()
	operator = operatorStack.pop()
	return process(value1,value2,operator)


def evaluate(expression):
	for char in expression:
		if char.isspace():
			continue
		if char in operators:
			while operatorStack and precedence( operatorStack[-1] ) > precedence(char):
				result = doArithmetic(operandStack,operatorStack)
				operandStack.append(result)
			operatorStack.append(char)
		elif char == '(' :
			operatorStack.append(char)
		elif char == ')':
				while operatorStack[-1] != '(' :
					result = doArithmetic(operandStack,operatorStack)
					operandStack.append( result )
				operatorStack.pop()
		else:
			operandStack.append(char)
	while operatorStack:
				result = doArithmetic(operandStack,operatorStack)
				operandStack.append(result)
	return operandStack.pop()

expression = raw_input("Enter the expression : ")
print evaluate(expression)