# Barcelona Player Performance Analysis

This project analyses FC Barcelona player performance using Python, pandas, and matplotlib.  
The aim is to demonstrate data analysis skills through feature engineering, filtering, and visualisation.

## Project Overview

Using player-level performance data, this project:
- Creates per 90 minute metrics (Goals, xG, xAG, Assists, Progressive actions)
- Filters players based on minutes played to ensure fair comparison
- Compares attacking output against expected goals (xG)
- Visualises insights using matplotlib

The analysis focuses on identifying attacking efficiency and contribution across the squad.

## Technologies Used

- Python
- pandas (data manipulation and analysis)
- matplotlib (visualisation)
- Git & GitHub (version control)

## Key Analysis Steps

- Constructed a pandas DataFrame from structured player data
- Engineered multiple per 90 statistics
- Cleaned data by removing players with zero minutes played
- Filtered attackers with 500+ minutes for meaningful comparison
- Created a bar chart comparing Goals per 90 vs xG per 90

## Example Insight

- Some attackers outperform their expected goals (xG), indicating strong finishing efficiency
- Filtering by minutes played significantly improves the reliability of comparisons
- Per 90 metrics allow fair evaluation across players with different playing time

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/barcelona-player-analysis.git
