class Solution:
	def getBinaryRep(self, n):
		# code here
		binary = bin(n)[2:]
        return binary.zfill(32)
