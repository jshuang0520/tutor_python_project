# -*- coding: utf-8 -*-
import ast
from collections import Counter
import argparse
from datetime import datetime
import os
import pandas as pd
import random
import time
import sys

pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)

parser = argparse.ArgumentParser()
parser.add_argument('--file_name',
                    help='choose a version of the error book. e.g. 20220817_errors_en_raw.csv')
parser.add_argument('--is_output_file',
                    help='True / False')

args = parser.parse_args()
# file_name = '20220817_errors_en_raw.csv'
file_name = args.file_name
is_output_file = ast.literal_eval(args.is_output_file)


file_base_path = os.getcwd()
# with open(f'{file_base_path}/{file_name}') as f:
with open(f'{file_base_path}/{file_name}') as f:
    lines = f.readlines()
# print(f'lines: {lines}')
en_lst = list()
for line in lines:
    element_lst = line.split(',')
    for x in element_lst:
        element = x.replace('\n', '').strip()
        en_lst.append(element)
# df = pd.DataFrame({'en': en_lst})
cnt = Counter(en_lst)
df = pd.DataFrame.from_dict(cnt, orient='index').reset_index().rename(columns={'index': 'vocab', 0: 'wrong_freq'}).sort_values(by=['wrong_freq', 'vocab'], ascending=[False, True])
print(df.head(5))
print(df.shape)
print(df.index.tolist())
output_file_name = file_name.replace('_raw', '_sorted')

if is_output_file:
    df.to_csv(f'{file_base_path}/{output_file_name}', index=False)


# sample command
# python parse_errors_en_raw.py --is_output_file="True" --file_name="20220825_errors_en_raw.csv"
