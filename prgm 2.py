
def findTrailingZeros(n):
	
	if(n < 0):
		return -1

	count = 0

	while(n >= 5):
		n //= 5
		count += n

	return count


n = 100
print("Count of trailing 0s " +
	"in 100! is", findTrailingZeros(n))

