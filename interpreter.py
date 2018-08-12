class Interpreter(object):
	"""
	A simple python Interpreter class that 
	executes bytecode intructions
	"""
	
	def __init__(self):
		self.stack = []
		self.environment = {}
	
	def LOAD_VALUE(self, number):
		self.stack.append(number)

	def PRINT_ANSWER(self):
		answer = self.stack.pop()
		print(answer)

	def STORE_NAME(self, name):
		value = self.stack.pop()
		self.environment[name] = value

	def LOAD_NAME(self, name):
		value = self.environment.get(name)
		self.stack.append(value)

	def ADD_VALUES(self):
		second_number = self.stack.pop()
		first_number = self.stack.pop()
		answer = first_number + second_number
		self.stack.append(answer)

	def parse_arguments(self, intructions, argument, what_to_execute):
		names = ["LOAD_NAME", "STORE_NAME"]
		numbers = ["LOAD_VALUE"]


		if intructions in names:
			argument = what_to_execute['names'][argument]
		elif intructions in numbers:
			argument = what_to_execute['numbers'][argument]

		return argument

	def run_code(self, what_to_execute):
		instructions = what_to_execute['instructions']
		numbers = what_to_execute['numbers']
		names = what_to_execute['names']

		for instruction in instructions:
			#import pdb;pdb.set_trace()
			event, index = instruction
			arg = self.parse_arguments(event, index, what_to_execute)
			bytecode_method = getattr(self, event)
			if arg is None:
				bytecode_method()
			else:
				bytecode_method(arg)

what_to_execute = {
        "instructions": [("LOAD_VALUE", 0),
                         ("STORE_NAME", 0),
                         ("LOAD_VALUE", 1),
                         ("STORE_NAME", 1),
                         ("LOAD_NAME", 0),
                         ("LOAD_NAME", 1),
                         ("ADD_VALUES", None),
                         ("PRINT_ANSWER", None)],
        "numbers": [1, 2],
        "names":   ["a", "b"]
}

interpreter = Interpreter()
interpreter.run_code(what_to_execute)
