# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import matplotlib.pyplot as plt


with open("C:\\Users\\aleks\\OneDrive\\Pulpit\\CCS\\CCSPythonProject\\dataset_results.csv") as results:
    csv_reader =csv.DictReader(results)
    
    
    # for row in results :
    #     category_counter.update(row['Categories'].split(';'))
    categories = [] # empty list of positive , controversial, negative
    result = []  #number of pos, cos and neg
    
    for row in csv.reader(results):
        categories.append(row[0])
        result.append(row[1])

plt.bar(categories,result)
plt.title('Number of obtained reviews in categories')
plt.xlabel('Categories')  
plt.ylabel('Number of reviews')

plt.show()