
def convertOpposite(str):
	ln = len(str)

	for i in range(ln):
		if str[i] >= 'a' and str[i] <= 'z':

			str[i] = chr(ord(str[i]) - 32)

		elif str[i] >= 'A' and str[i] <= 'Z':

			str[i] = chr(ord(str[i]) + 32)

if __name__ == "__main__":
	str = "inTERshiP.speCTrum.coM "
	str = list(str)

	convertOpposite(str)

	str = ''.join(str)
	print(str)

