import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('File.xlsx', sheetname='Automata1')
df2 = pd.read_excel('File.xlsx', sheetname='Automata2')

