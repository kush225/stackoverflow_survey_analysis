import pandas as pd
import csv
from collections import defaultdict, Counter

#Percentage of Hobbyist & not Hobbyist. [%age of people coding as a hobby??]
with open('survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)
    
    #hobbyist_counter= {'Yes':0,
    #                  'No': 0
    #                 }
    #hobbyist_counter = defaultdict(int)
    hobbyist_counter = Counter()
    
    for line in csv_reader:
        hobbyist_counter[line["Hobbyist"]] += 1
    
    total = hobbyist_counter['Yes'] + hobbyist_counter['No']
    
    percentage_yes = hobbyist_counter['Yes']/total * 100
    percentage_yes = round(percentage_yes,2)
    
    percentage_no = hobbyist_counter['No']/total * 100
    percentage_no = round(percentage_no,2)
    
    
    print(f'Percentage of people that do coding as a hobby: {percentage_yes}')
    print(f'Percentage of people that don\'t coding as a hobby: {percentage_no}')

#for plotting results
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

slices = [ percentage_yes, percentage_no ]
labels = ['people that like', 'people that don\'t']
explode= [ 0, 0.1 ]

plt.pie(slices, labels=labels, wedgeprops={'edgecolor':'black'},
        explode=explode,shadow=True, startangle=90, autopct='%1.1f%%')
plt.title("Coding As a Hobby")
plt.tight_layout()
plt.show()   

