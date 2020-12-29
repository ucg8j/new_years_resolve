# IMDB - get watched statistics
Have you watched the best movies humans have produced? Maybe you have a goal of having watched a certain proportion of the top movies of all time. These scripts help do the calculation.


## Steps to Use
1. Get the top 250 imdb movies

```
python3 imdb_top_250.py
```

This writes a csv `top_250_watched.csv`

2. Fill out the csv with a 1 in the `watched` column to mark those that you have watched.

3. Run `imdb_watched_stats.py`


## TODOs
- if user has an imdb account they may have used it to record what they have watched - get that data and merge it with any manually added data
- 
