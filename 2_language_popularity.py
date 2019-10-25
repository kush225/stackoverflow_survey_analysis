import pandas as pd
import csv
from collections import defaultdict, Counter

#Percentage of 15 most popular programming Language. [response wise]
with open('survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)
    
    types = Counter()
    total = 0
    
    for line in csv_reader:
        languages = line['LanguageWorkedWith'].split(';')
        for language in languages: 
            types[language] += 1
        total += 1
    languages=[]
    popularity=[]
    popularity_pct=[]
    for key,value in types.most_common(15):
        percentage_lang = value/total * 100
        percentage_lang = round(percentage_lang, 2)
        
        languages.append(key)
        popularity_pct.append(percentage_lang)
        popularity.append(value)
        
#for plotting piechart
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

labels=["{0} ({1}%)".format(x,y) for x,y in zip(languages,popularity_pct)]
plt.pie(popularity_pct, labels=labels, wedgeprops={'edgecolor':'black'},
        shadow=True)
plt.title("Most Popular Languages")
plt.tight_layout()
plt.show()   


#plotting Horizontal bar Chart
plt.barh(languages,popularity)

plt.title("Most Popular Languages")
#plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()
plt.show()

#for printing results on screen
for i in range(len(languages)):
    print("Programming language {0} is used by {1} of people ({2}%)".format(languages[i],popularity[i],popularity_pct[i]))
