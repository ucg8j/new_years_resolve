import imdb
import pandas as pd
import os.path

if os.path.isfile('top_250_watched.csv'):
    raise Exception('file exists already - running this will overwrite inputted data')

ia = imdb.IMDb()

top = ia.get_top250_movies()

df = []

for i in range(0, len(top)):
  title = top[i].get('title')
  rank = i + 1

  df.append({
    'rank': rank,
    'title': title,
    'watched': str('')
  })

df = pd.DataFrame(df)

df.to_csv('top_250_watched.csv', index=False)
