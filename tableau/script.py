import pandas as pd
import os

from search_words import DRUGS_AND_PRECURSORS

def get_daily_mean(df):
    return float(f"{df[df['country'] == 'NL']['Daily mean'].mean():.2f}")

class DataManager():
    def __init__(self):
        self.datapaths = {
            'courtcases': "data/courtcases",
            'sewerdata': "data/sewerdata/emcdda",
            'casedata': "data/"
        }
        self.cases_df = pd.read_csv(
            f"{self.datapaths['casedata']}/cases3.csv", 
            sep=',',
            usecols = [
                'GerechtelijkProductType', 'Case ID', 
                'Proceduresoorten', 'Publicatiedatum', 
                'Rechtsgebieden', 'Tekstfragment', 
                'Titel', 'Uitspraakdatum', 'UitspraakdatumType'
            ]
        )
    
    def collect_sewerdata(self):
        years_of_interest = list(range(2011, 2021))
        folders = os.listdir(self.datapaths['sewerdata'])
        sewerdata = {}
        for folder in folders:
            sewerdata[folder] = []
            for year in years_of_interest:
                filename = f"WW-data-{folder}-{year}.csv"
                df = pd.read_csv(f"{self.datapaths['sewerdata']}/{folder}/{filename}", sep=',')
                daily_mean = get_daily_mean(df)
                sewerdata[folder].append(daily_mean)
            sewerdata[folder] = pd.Series(sewerdata[folder])
            sewerdata[folder].index = years_of_interest
        self.sewerdata = pd.DataFrame.from_dict(sewerdata)

    def collect_courtdata(self):
        case_count = len(os.listdir(self.datapaths['courtcases']))
        data = []
        for filename in os.listdir(self.datapaths['courtcases']):
            with open(f"{self.datapaths['courtcases']}/{filename}", 'r') as f:
                text_file = f.read()
                data.append([filename[:-4], text_file])
        verdict_df = pd.DataFrame(data, columns=['Case ID', 'Case Text'])
        merged_df = pd.merge(self.cases_df, verdict_df, on='Case ID', how='left')
        self.courtdata = merged_df

    def count_mentions(self, word_arr):
        date_and_count = []
        for _, row in self.courtdata.iterrows():
            current_date = row["Uitspraakdatum"]
            case_ID = row['Case ID']
            current_case_text = row['Case Text']
            occurrences = 0
            for word in word_arr:
                occurrences += current_case_text.lower().count(word.lower())
            date_and_count.append([current_date, case_ID, occurrences])

        results = pd.DataFrame(date_and_count, columns=['date', 'Case ID', 'count'])
        return results

    def count_cases(self, word_arr):
        date_and_counts = []
        for _, row in self.courtdata.iterrows():
            current_date = row['Uitspraakdatum']
            case_ID = row['Case ID']
            current_case_text = row['Case Text']
            occurrences = 0
            if any(x.lower() in current_case_text.lower() for x in word_arr):
                occurrences = 1
            date_and_counts.append([current_date, case_ID, occurrences])
        
        results = pd.DataFrame(date_and_counts, columns=['date', 'Case ID', 'count'])
        return results

    def process_search_words(self):
        data = {}
        for key, search_words in DRUGS_AND_PRECURSORS.items():
            pass
            # data[key] = 1
        



dm = DataManager()
dm.collect_sewerdata()
dm.collect_courtdata()
# x = dm.count_mentions(['safrol', 'isosafrol', 'safrool', 'isosafrool'])
# print(x[x['count'] > 0].head())