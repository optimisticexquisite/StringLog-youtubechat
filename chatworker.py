import time
import collections
import csv
import operator
while 1>0:
    file31=""
    file1=open("chatfile2.txt","r")
    variable=[]
    def CountFrequency(variable):
        return collections.Counter(variable)
    a=file1.readline()
    b=0
    while a!="":
        variable.append(a)
        b+=1
        a=file1.readline()
    #variable.append(file1.readline())
    #print(variable[5])
    freq=CountFrequency(variable)
    with open('names1.csv', 'w', newline='') as csvfile:
        fieldnames = ['moves', 'frequency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for (key,value) in freq.items():
            keystring=str(key)
            keystring1=str.rstrip(keystring)
            valuestring=str(value)
            #file3=open("chatfinal.txt","w")
            file31=(file31+(keystring1+ ","+valuestring)+"\n")
            writer.writerow({'moves':keystring1,'frequency':valuestring})
        #file3.close()
    file3=open("chatfinal.txt","w")
    file3.write(file31)
    file3.close()
    #This is the framework of how the csv file was written on loop.
    #with open('chatcsv.csv', mode='w') as employee_file:
        #chat_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #chat_writer.writerow(file31)


        #writer.writeheader()
        #writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        #writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        #writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

        # Create object that maps rows to a dictionary.
    reader = csv.DictReader(open('names1.csv', 'r'))
    # Sort rows in object by key name 'author' via lambda function.
    result = sorted(reader, key=lambda d: d['frequency'])

    # Create object that maps dictionaries onto output rows.
    writer2 = csv.DictWriter(open('names2.csv', 'w'), reader.fieldnames)
    # Write row with assigned fieldnames in 'analysis.csv'.
    writer2.writeheader()
    # Write newly sorted rows to output file.
    writer2.writerows(result)

    #print("Sort complete!")
    #print("New csv outfile created.")
    time.sleep(1)
