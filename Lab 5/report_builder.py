import pandas as pd
from tabulate import tabulate

def build_html_report(data):
    df = pd.DataFrame(data)
    return df.to_html(index=False)

def build_text_report(data):
    df = pd.DataFrame(data)
    return tabulate(df, headers='keys', tablefmt='github')
