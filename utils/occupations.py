import random, csv


def open_da_occupations():
	data = {}
	#with the file open, iterate through each line and divide it into 2 columns, with the first being the keys and the second being the values
	with open("data/occupations.csv", "r") as infile:
		reader = csv.reader(infile)
		for row in reader:
			k = row[0]
			if k != "Job Class" and k != "Total":
				v = float(row[1])
				data[k] = v
	return data
				
def get_random_occupation():
	data = open_da_occupations() #create the dictionary
	occNum = random.random() * 99.8
	#print occNum
	#for each key in the data dict, subtract the value of the key from a random number unless the random number is negative, then you return the key which you are currently getting the value of
	for key in data:
		#print data[key]
		if occNum - data[key] > 0:
			occNum = occNum - data[key]
		else:
			return key
	
#test cases
if __name__ == "__main__":
	print open_da_occupations()
	print get_random_occupation()