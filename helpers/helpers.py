import pandas as pd
from pathlib import Path
import sqlite3
from bs4 import BeautifulSoup as bs

def save_text(text_):
    path = 'data/text_html.txt'
    with open(path, 'w') as f:
        f.write(str(text_))

def form_dataframe(list_: list) -> bs:
    df = pd.DataFrame(list_)
    print(df.info())
    return df

def to_sqlite(df: pd.DataFrame) -> None:
    path = Path("data/movies.db")
    con = sqlite3.connect(path)
    df.to_sql("tomatoes", con, if_exists='replace', index=False)
    print(f"dataframe saved to {path}")

if __name__ == '__main__':
    print('wrong file run')

