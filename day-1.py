import os
import requests

from collections import Counter
from dotenv import load_dotenv 

load_dotenv() 

cookies = {"session": os.getenv('SESSION_COOKIE')}

response = requests.get('https://adventofcode.com/2024/day/1/input', cookies=cookies)

# Part One
list_1 = []
list_2 = []

for line in response.iter_lines():
  l, r = line.decode('utf-8').split()
  list_1.append(int(l))
  list_2.append(int(r))

list_1.sort()
list_2.sort()

sum = 0;

for val_1, val_2 in zip(list_1, list_2):
  sum += abs(val_1 - val_2)

print(f'Total distance between lists: {sum}')

# Part Two

right_list_counter = Counter(list_2)
similarity_score = 0

for val in list_1:
  similarity_score += val * right_list_counter.get(val, 0)

print(f'Total similarity score: {similarity_score}')