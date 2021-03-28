import pandas as pd
from datetime import timedelta
import numpy as np
from os import walk
import ast

SEPARATOR = ";"
HISTORY_PATH = "../resources/history_files/squash/"
_, _, DEALS_HISTORY_FILE_NAMES_LIST = next(walk(HISTORY_PATH))


frames = [pd.read_csv(HISTORY_PATH+file_name, sep=SEPARATOR) for file_name in DEALS_HISTORY_FILE_NAMES_LIST]
df = pd.concat(frames)

df = df.set_index("deal_id")
print(df.head())
df.to_csv(HISTORY_PATH+"Viktoria_202010323_paper.csv", sep=SEPARATOR)