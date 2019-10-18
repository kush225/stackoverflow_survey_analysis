import pandas as pd
import csv
from collections import defaultdict, Counter

doc1 = pd.read_csv('data/survey_results_public.csv')
doc2 = pd.read_csv('data/survey_results_schema.csv')
doc3 = doc1.iloc[:,[12,17]]

#Task1 Percentage of Hobbyist & not Hobbyist. [%age of people coding as a hobby??]
with open('data/survey_results_public.csv') as f:
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
    
    
#Task2 Percentage of 5 most popular programming Language. [response wise]
with open('data/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)
    
    types = Counter()
    total = 0
    
    for line in csv_reader:
        languages = line['LanguageWorkedWith'].split(';')
        for language in languages: 
            types[language] += 1
        total += 1
    with open('programming_popularity','w') as f:
        for key,value in types.items():
            percentage_lang = value/total * 100
            percentage_lang = round(percentage_lang, 2)
        
            f.write(f'Percentage of {key} is {percentage_lang}% ')
            f.write("\n")


#Task3 Top 5 languages Percentage in different field types.
with open('data/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)
    
    dev_dict = {}
    
    for line in csv_reader:
        dev_types = line['DevType'].split(';')
        for dev_type in dev_types:
            dev_dict.setdefault(dev_type,{ 'total' : 0, 
                                          'language_counter' : Counter()})
            lang_types = line['LanguageWorkedWith'].split(';')
            dev_dict[dev_type]['language_counter'].update(lang_types)
            dev_dict[dev_type]['total'] += 1
       
            
for dev_type, info in dev_dict.items():
    print(dev_type)
    for language, value in info['language_counter'].most_common(5):
        language_pct = (value/info['total'])*100
        language_pct = round(language_pct,2)
        
        print(f'{language}: {language_pct}%')
    print()

with open('analysis.txt','w') as f:
    for dev_type, info in dev_dict.items():
        f.write(dev_type+" : ")
        f.write("\n")
        for language, value in info['language_counter'].most_common(5):
            language_pct = (value/info['total'])*100
            language_pct = round(language_pct,2)

            f.write(f'{language}: {language_pct}% ')
        f.write('\n')
        f.write("---------------------------------------")
        f.write("\n")
        
        
        
        
#Task4 career statisfaction
with open('data/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)
    
    dev_dict ={}
    
    for line in csv_reader:
        dev_types = line['DevType'].split(';')
        for dev_type in dev_types:
            dev_dict.setdefault(dev_type,{ 'total' : 0, 
                                          'Statisfaction_counter' : Counter()})

            job_stat = line['JobSat'].split(";")
            dev_dict[dev_type]['Statisfaction_counter'].update(job_stat)
            dev_dict[dev_type]['total'] += 1

with open('job_statisfaction', 'w') as f:
    for dev_type, info in dev_dict.items():
        f.write(dev_type+" : ")
        f.write("\n")
        for statisfaction, value in info['Statisfaction_counter'].items():
#            print(statisfaction,value)
            statisfaction_pct = (value/info['total'])*100
            statisfaction_pct = round(statisfaction_pct,2)

            f.write(f'{statisfaction}: {statisfaction_pct}% ')
            f.write("\n")
        f.write('\n')
        f.write("---------------------------------------")
        f.write("\n")