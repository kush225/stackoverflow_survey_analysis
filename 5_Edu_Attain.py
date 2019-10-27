import pandas as pd
from collections import Counter

#reading dataset
dataset = pd.read_csv('survey_results_public.csv')

#counting votes in each education Level
counter = Counter()
for i in dataset['EdLevel']:
    counter[i] += 1

#total number of votes
total=sum(counter.values())
   
#adding education & %age list 
ed_list, perc_list= [], []
for key, value in counter.items():
    percent_ed = value/total * 100
    percent_ed = round(percent_ed, 2)
    ed_list.append(str(key))
    perc_list.append(percent_ed)
    

#for plotting piechart
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

#for adding text & percentage in legend in decreasing order
labels=["{0} ({1}%)".format(x,y) for x,y in sorted(zip(ed_list,perc_list), key=lambda x: x[1],reverse=True)]
patches, text = plt.pie(perc_list, wedgeprops={'edgecolor':'black'},
         shadow=True)

plt.title("Educational Attainment")
plt.legend(patches, labels,  fontsize='xx-small')

plt.show()

