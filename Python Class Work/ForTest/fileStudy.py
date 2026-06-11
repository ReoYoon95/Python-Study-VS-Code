infile = open("phones.txt", "r")

for line in infile:
    line = line.rstrip()
    word_list = line.split()
    for word in word_list:
        print(word)
infile.close()



import csv

f = open("weather.csv")
data = csv.reader(f)
header = next(data)
for row in data:
    print(row)
f.close()

f = open("weather.csv")
header = next(data)

for line in f:
    word_list = line.rstrip().split(",")
    print(word_list)
f.close()
