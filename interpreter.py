class Interpreter(object):
	"""
	A simple python Interpreter class that 
	executes bytecode intructions
	"""
	
	def __init__(self):
		self.stack = []
	
	def LOAD_VALUE(self, number):
		self.stack.append(number)

	def PRINT_ANSWER(self):
		answer = self.stack.pop()
		print(answer)

	def ADD_TWO_VALUES(self):
		second_number = self.stack.pop()
		first_number = self.stack.pop()
		answer = first_number + second_number
		self.stack.append(answer)

	def run_code(self, what_to_execute):
		instructions = what_to_execute['instructions']
		numbers = what_to_execute['numbers']
		for instruction in instructions:
			event, index = instruction
			if event == 'LOAD_VALUE':
				number = numbers[index]
				self.LOAD_VALUE(number)
			elif event == 'ADD_TWO_VALUES':
				self.ADD_TWO_VALUES()
			elif event == 'PRINT_ANSWER':
				self.PRINT_ANSWER()


what_to_execute = {
	    "instructions": [("LOAD_VALUE", 0),  # the first number
                     ("LOAD_VALUE", 1),  # the second number
                     ("ADD_TWO_VALUES", None),
                     ("PRINT_ANSWER", None)],
    "numbers": [7, 5]
}

interpreter = Interpreter()
interpreter.run_code(what_to_execute)
