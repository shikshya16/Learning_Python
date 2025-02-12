with open("test.txt", "w") as file:        #Write Mode
    # file.write("Hello Python File Handling")
    file.write("In Append Mode")

with open("test.txt", "a") as file:          #append mode
    file.write("\nThis is second line")

with open("test.txt", "w") as file:
    file.writelines(["This is line1\n", "This is line2"])

with open("test.txt") as file:
    for line in file:
        line = line.split(",")
        print(f"Name={line[0]}, Age={line[1]}, Address={line[2]}") 


with open("test.txt") as file:
    file.readline()
    for line in file:
        line = line.strip('\n').split("\t")
        print(line)
        #print(f"Name={line[0]}, Age={line[1]}, Address={line[2]}") 


import csv
with open ('test.txt')as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        print(line)


import csv
with open ('test.txt')as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    print(header)
    for line in csv_reader:
        print(line)

#Delimiter

import csv
with open ('test.txt')as file:
    csv_reader = csv.reader(file, delimiter="\t")
    header = next(csv_reader)
    print(header)
    for line in csv_reader:
        print(line)

import csv
data = [
    ['Name', 'Age', 'City'],
    ['Shikshya', '24', ''],
    ['Cixya', '22', 'Kathmandu']
]
with open('new.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)


import csv
with open('new.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)