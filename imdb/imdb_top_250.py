import imdb
import pandas as pd

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
