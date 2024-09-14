from Memory import MemoryManager
from ASM import ASM

class CodeGEN:
	def run(self, semanticNode):
		res = semanticNode.visit(MemoryManager.instanceOfMemoryManager())
		return res

