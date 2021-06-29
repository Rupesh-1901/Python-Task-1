
def kthSmallest(arr, n, k):


	arr.sort()

	
	return arr[k-1]


if __name__=='__main__':
	arr = [7, 15, 3, 4, 18, 1]
	n = len(arr)
	k = 2
	print("K'th smallest element is",
		kthSmallest(arr, n, k))

