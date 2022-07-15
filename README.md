# [Stackoverflow Programming Survey](https://insights.stackoverflow.com/survey) Analysis
This contains scripts which analysed stackoverflow programming survey 2019 using python. 

## Requirements
python3.5 or above for analysing
matplotlib for plotting
[dataset](https://drive.google.com/file/d/1QOmVDpd8hcVYqqUXDXf68UMDWQZP0wQV/view) for data to analyse

## Setting up your Environment

First, clone this repository:

    git clone https://github.com/kush225/stackoverflow_survey_analysis.git

You can use pip, virtualenv and virtualenvwrapper to install the requirements:

    pip install -r requirements.txt
    
Run the server by running `python script_name.py`:

	python 1_coding_as_hobby.py
  
## Results


![Alt text](charts/coding_as_hobby.png?raw=true "1_coding_as_hobby.py pieresult")

![Alt text](charts/lang_popularity_hbar.png?raw=true "2_language_popularity.py hbarresult")

![Alt text](charts/lang_popularity_pie.png?raw=true "2_language_popularity.py pieresult")

![Alt text](charts/Edu_attain.png?raw=true "5_Edu_Attain.py pieresult")
