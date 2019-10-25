import pandas as pd
import csv
from collections import defaultdict, Counter


#Top 5 languages Percentage in different field types.
with open('survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)

    dev_dict = {}

    for line in csv_reader:
        dev_types = line['DevType'].split(';')
        for dev_type in dev_types:
            dev_dict.setdefault(dev_type,{ 'total' : 0,
                                          'language_counter' : Counter()})
            lang_types = line['LanguageWorkedWith'].split(';')
            dev_dict[dev_type]['language_counter'].update(lang_types)
            dev_dict[dev_type]['total'] +=1


##for printing results on screen
#for dev_type, info in dev_dict.items():
#    print(dev_type)
#    for language, value in info['language_counter'].most_common(5):
#        language_pct = (value/info['total'])*100
#        language_pct = round(language_pct,2)
#
#        print(f'{language}: {language_pct}%')
#    print()
#

#for saving output in file
with open('lang_pop_diff_fields.txt','w') as f:
    for dev_type, info in dev_dict.items():
        dev_types.append(dev_type)
        f.write(dev_type+" : ")
        f.write("\n")
        for language, value in info['language_counter'].most_common(5):
            language_pct = (value/info['total'])*100
            language_pct = round(language_pct,2)

            f.write(f'{language}: {language_pct}% \n')
        f.write('\n')
        f.write("---------------------------------------")
        f.write("\n")

