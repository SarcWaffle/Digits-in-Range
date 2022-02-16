# Write Python3 code here
def numberOf2sinRange(n):
	s = ""
	for i in range(0,n+1):
		s+=str(i)
	return(list(s).count('8'))

# Driver code
n = 2000000
print(numberOf2sinRange(n))
