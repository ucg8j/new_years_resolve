import pandas as pd

df = pd.read_csv('top_250_watched.csv')

def top_x_stat(df, n=100):
  """
  Calculate the watched percentage of top N movies
  """
  number_watched = df[df['rank'] <= n]['watched'].sum()
  percent = round(number_watched / n * 100, 1)
  print('Watched ' + str(int(number_watched)) + ' (' + str(percent) + '%)' + ' of '+ str(n) + ' movies')

top_x_stat(df, 50)
top_x_stat(df, 100)
top_x_stat(df, 250)
