# Creating and solving an 0/1 knapsack problem scenario using Dynamic programming


def maxVal(max_weight, num_packages, weights, values):

	## Create a 2D array to store options
	opts_arr = [ [0 for _ in range(max_weight + 1)] for _ in range(num_packages+ 1) ]  

	## i equals rows 0...num_packages
	## j equals columns 0...max_weight

	## leave first row as 0


	##recursively calculate the next row down
	for i in range(1, num_packages ):
		for j in range(max_weight ):

			## first set the next row as the first, this is for the case where the new object is not picked
			opts_arr[i][j] =  opts_arr[i -1][j]

            ## j is tracking the current max weight, if the previous object's weight is within the proper bound 
			if ((j >= weights[i-1]) 
					## if adding the new object increases our net value 
					and (opts_arr[i][j] < (opts_arr[i - 1][j - weights[i - 1]]) + values[i - 1])):

						## add the new object
						opts_arr[i][j] = opts_arr[i - 1][j - weights[i - 1]] + values[i - 1]


	for i in range(1, num_packages ):
		for j in range(max_weight ):
			print(opts_arr[i][j], end =" ")
		print("\n")

	maxVal = opts_arr[num_packages -1][max_weight - 1]
	return maxVal




def main():
	##
	max_weight = 12
	num_packages = 15

	## corresponding arrays with values and weights of 

	weight_arr = [0, 7, 3, 8, 5, 2, 9, 5,  2,  5, 4,  6,  2, 8,  6, ]
	values_arr = [0, 2, 4, 3, 5, 3, 2, 3, 56, 76, 2, 34, 12, 6, 65, ]
	## print(len(weight_arr ) == len(values_arr))

	max_val = maxVal(max_weight, num_packages, weight_arr, values_arr)

	print(max_val)


if __name__ == "__main__":
	main()