import os
import requests

from collections import Counter
from dotenv import load_dotenv 

load_dotenv() 

cookies = {"session": os.getenv('SESSION_COOKIE')}

response = requests.get('https://adventofcode.com/2024/day/2/input', cookies=cookies)

def isLinear(prev_level, level, isDecreasing):
  if isDecreasing:
    return prev_level < level
  else:
    return prev_level > level

def isSubReportSafe(report, indexToRemove):
  report.pop(indexToRemove)
  isDecreasing = report[0] > report[-1]
  
  for i in range(1, len(report)):
    prev_level = report[i - 1]
    level = report[i]
      
    if abs(prev_level - level) > 3 or abs(prev_level - level) == 0 or isLinear(prev_level, level, isDecreasing):
      return False
  
  return True

def isReportSafe(report):
  isDecreasing = report[0] > report[-1]
  
  for i in range(1, len(report)):
    prev_level = report[i - 1]
    level = report[i]
      
    if abs(prev_level - level) > 3 or abs(prev_level - level) == 0 or isLinear(prev_level, level, isDecreasing):
      return isSubReportSafe(report.copy(), i) or isSubReportSafe(report.copy(), i-1)
  
  return True

safe_summary = 0
for line in response.iter_lines():
  report = list(map(lambda x: int(x), line.decode('utf-8').split()))

  if isReportSafe(report):
    safe_summary += 1

print(safe_summary)
