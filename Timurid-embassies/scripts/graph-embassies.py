import os

# def regress_to_home(home='silk-roads-resources'):
#     current_dir = os.getcwd().split("\\")
#     print(current_dir)
#     while current_dir[-1] != 'silk-roads-resources':
#         new_dir = "\\".join(current_dir[:-1])
#         os.chdir(new_dir)
#         current_dir = os.getcwd().split("\\")
#         print(current_dir)

# regress_to_home()
# print(os.getcwd())
# from scripts.shared_graphing import categorical_bar

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def categorical_bar(fieldname, data, outdir, hue_field=None, csv=True):
   
    if csv:
        df = pd.read_csv(data)
    else:
        df = data

    png = '{}/{}.png'.format(outdir, fieldname)

    df = df.sort_values(by= fieldname)    
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 6)
    sns.countplot(data=df, y = fieldname, ax=ax, hue=hue_field)
    fig.savefig(png, bbox_inches='tight')

def catbar_split_field(fieldname, csv, outdir, splitter=", "):

    data = pd.read_csv(csv)[fieldname].to_list()
    new_data = []
    for row in data:
        split_row = row.split(splitter)
        new_data.extend(split_row)
    
    df = pd.DataFrame()
    df[fieldname] = new_data
    categorical_bar(fieldname, df, outdir, csv=False)

if __name__ == '__main__':
    input_file = '../data/Timurid Embassies-from Rossabi.csv'
    outdir = '../graphs/'
    split_field_list = ['Tribute', 'Chinese Gifts']

    for field in split_field_list:
        catbar_split_field(field, input_file, outdir)
    
    categorical_bar('Year', input_file, outdir, hue_field='Destination(s)')


