
def isPerfect( n ):

	sum = 1

	i = 2
	while i * i <= n:
		if n % i == 0:
			sum = sum + i + n/i
		i += 1

	
	return (True if sum == n and n!=1 else False)

user = int(input("Enter the value of n "))  
n = 2
count=1
for n in range (1000):
        if (count <= user):
                if isPerfect (n):
                        print(n , " is a perfect number")
                        count=count+1

