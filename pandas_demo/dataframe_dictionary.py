import pandas as pd

data = {

  "Name" : ["Poovalingam", "Saroja"],
  "Age" : [71,70],
  "Score" : [98,98]

}

df = pd.DataFrame(data)
print(df)