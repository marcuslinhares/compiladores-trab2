class ASM:
	lookahead = None
	def __init__(self) -> None:
		self.code = []
		self.id = 0

	def run(self, code: str):
		self.code = list(code+'$')
		ASM.lookahead = self.code[self.id]
		try:
			print(".globl _start")
			print("_start:")
			self.E()
			self.emitln("mov $1, %eax")
			self.emitln("mov $0, %ebx")
			self.emitln("int $0x80")
		except:
			print("Error Generate Machine Code!!!")
		if self.current()!='$':
			print("Codigo não percurrido todo!")

	def E(self): #E -> T+T | T-T  and  T -> num
		self.T()
		self.emitln("mov %eax, %ebx")
		op = self.current()
		self.next()
		if(op == '+'):
			self.T()
			self.emitln("add %ebx, %eax")
		elif (op == '-'):
			self.T()
			self.emitln("sub %ebx, %eax")
			self.emitln("neg %eax")
		else:
			raise Exception("+ or - expected")
		
	def T(self):
		self.emitln("mov $" + self.getNum() + ", %eax")
		self.next()

	def emitln(self, s: str):
		print("    " + s)

	def match(self, c: str):
		return (ASM.lookahead == c)
	
	def getNum(self):
		number = None
		try:
			number = int(ASM.lookahead)
		except:
			print("Integer expected!")
		return str(number)
	
	def next(self):
		self.id = self.id + 1
		max = len(self.code) - 1
		if self.id > max:
			self.id = max
		ASM.lookahead = self.code[self.id]
	
	def current(self): return ASM.lookahead

if __name__ == "__main__":
	asm = ASM()
	asm.run("3+2")
#E -> T+T | T-T  and  T -> num
#OBS: num eh um terminal,digito unitario de 0 ate 9


