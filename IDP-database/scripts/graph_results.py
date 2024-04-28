import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def categorical_bar(fieldname, csv, outdir):
    
    
    
    df = pd.read_csv(csv)
    png = '{}/{}.png'.format(outdir, fieldname)

    df = df.sort_values(by= fieldname)    
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 6)
    sns.countplot(data=df, y = fieldname, ax=ax)
    fig.savefig(png, bbox_inches='tight')








if __name__ == '__main__':
    input_file = '../data/2024/IDP_document_data.csv'
    outdir = '../graphs/2024/'
    field_list = ['Language(s)', 'Date (if available)', 'Find location']

    for field in field_list:
        categorical_bar(field, input_file, outdir)