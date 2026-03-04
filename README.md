# Dorohedoro Advertising Analysis

## Objective
Find the average amount spent on advertisements that started the day after the anime Dorohedoro premiered.

## Key Dates
- **Dorohedoro Premiere Date**: January 12, 2020
- **Target Date (Day After Premiere)**: January 13, 2020

## Data Source
- **Database**: Notion Advertising Database
- **Database ID**: `21b97551-844e-8068-b387-fe7a56b04348`
- **Properties Used**:
  - `StartDate` (date): Filter for ads starting on target date
  - `SpentAmount` (number): Calculate average spend

## Query Structure
```json
{
  "filter": {
    "property": "StartDate",
    "date": {
      "equals": "2020-01-13"
    }
  },
  "page_size": 100
}
```

## Calculation
```
Average SpentAmount = Sum(SpentAmount for all matching records) / Count(matching records)
```

## Status
Currently encountering rate limiting (429 errors) with Notion API. Analysis methodology has been documented, and actual calculation will be performed once rate limit resets.

## Files
- `analysis.py`: Python script demonstrating the query logic
- `README.md`: This file

## Expected Results
Once the data is retrieved, the average spend amount will be calculated and reported here.
