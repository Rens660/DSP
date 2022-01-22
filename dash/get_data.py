import os, os.path
import numpy as np
import pandas as pd
from pathlib import Path


def full_data():
    path_parent = os.path.dirname(os.getcwd())
    dataPath = path_parent + '/data/data3/'
    caseCount = len(os.listdir(dataPath))
    data = []
    try:
        os.remove(dataPath + ".DS_Store")
    except:
        print("No file DS_Store")
    for filename in os.listdir(dataPath):
        f = open(os.path.join(dataPath, filename), encoding='utf-8')
        data.append([filename.replace('.txt', ''), f.read()])
    verdict_df = pd.DataFrame(data, columns=['Case ID', 'Case Text'])
    cases_df = pd.read_csv(path_parent + '/cases3.csv', usecols = ['GerechtelijkProductType', 'Case ID', 'Proceduresoorten', 'Publicatiedatum', 'Rechtsgebieden', 'Tekstfragment', 'Titel', 'Uitspraakdatum', 'UitspraakdatumType'])
    merged_df = cases_df.join(verdict_df.set_index('Case ID'), on='Case ID', how='left')
    return merged_df