import pandas as pd

filename = 'non-iot.csv'
filelabel = 'non-iot_device.csv'

df = pd.read_csv(filename)
nonlist = pd.read_csv(filelabel)

df_label = df.merge(nonlist, how = 'left', left_on='eth.src', right_on='eth.src')

df.to_csv('labeled_'+filename, index = False)