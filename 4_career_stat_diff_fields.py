import pandas as pd
import csv
from collections import defaultdict, Counter

#career statisfaction
with open('survey_results_public.csv') as f:
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

#for saving output in file
with open('job_statisfaction.txt', 'w') as f:
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
