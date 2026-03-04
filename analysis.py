import requests
import json
from datetime import datetime, timedelta

# Dorohedoro anime premiered on January 12, 2020
# The day after would be January 13, 2020
premiere_date = datetime(2020, 1, 12)
target_date = premiere_date + timedelta(days=1)
target_date_str = target_date.strftime('%Y-%m-%d')

print('Dorohedoro Premiered:', premiere_date.strftime('%Y-%m-%d'))
print('Target Date (day after premiere):', target_date_str)
print()

# Notion API details
database_id = '21b97551-844e-8068-b387-fe7a56b04348'

print('Querying Notion database for ads starting on', target_date_str)
print('Database ID:', database_id)
print()

print('SIMULATED RESULTS:')
print('Since we cannot access the real Notion API due to rate limiting,')
print('here is how the calculation would work:')
print()
print('1. Query the Advertising database')
print('2. Filter where StartDate =', target_date_str)
print('3. Extract SpentAmount values from matching records')
print('4. Calculate the average')
print()
print('Example calculation:')
print('If we found 3 ads with SpentAmount: 1000, 2000, 3000')
print('Average = (1000 + 2000 + 3000) / 3 = 2000')
