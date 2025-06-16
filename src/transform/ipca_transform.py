import pandas as pd

class TransformIPCA:
   def __init__(self, data) -> None:
      self._data = data
      self._df = None

   def transform(self):
      dataframe = pd.DataFrame(self._data)
      dataframe.to_csv('ipca.csv')
