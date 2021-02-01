#take a file, turn it into a list
def read_file(file):
	myfile = open(file, "r")
	mylines = myfile.readlines()
	for c in mylines:
		words = c.split()
	return words
	myfile.close


#make a list write to a file one word per line
w = read_file("lab11_input.txt")
def write_list(listt, f):
	f = "lab11_output.txt"
	listt = w
	write_file = open(f, "w")
	for each in listt:
		write_file.write(each+"\n")
	write_file.close()

#same as above but ordered
def write_list_sort(A,B):
	A = w
	B = "lab11_output_sort.txt"
	A.sort()
	write_file_ = open(B, "w")
	for word in A:
		write_file_.write(word+"\n")
	write_file_.close()


#no punc or caps
def write_list_cleansort(x,y):
	x = w
	y = "lab11_output_cleansort.txt"
	oh = open(y, "w")
	for every in x:
		for t in every:
			t = t.lower()
			if t == ")":
				oh.write(t.replace(")", ""))
			if "(" in every:
				oh.write(every.replace("(", ""))
			if "," in every:
				oh.write(every.replace(",", ""))
			if "." in every:
				oh.write(every.replace(".", ""))
	oh.close()


