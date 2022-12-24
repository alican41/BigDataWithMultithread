from PyQt5.QtWidgets import QApplication
from gui1 import firstPage


app = QApplication([])
pencere = firstPage()
pencere.show()
app.exec_()

"""
df = pd.read_csv('C:/Users/alica/OneDrive/Masaüstü/rows.csv/rows.csv', low_memory=False)

df2 = df[["Product", "Issue", "Company", "State", "ZIP code", "Complaint ID"]]
df2.to_csv('new-result.csv')
df2 = pd.read_csv('new-result.csv')

df3 = df2.dropna()
df3.to_csv('result2.csv')
df3 = pd.read_csv('result2.csv')

df3['Product'] = [re.sub('[^\w\s]+', '', s) for s in df3['Product'].tolist()]
df3['Issue'] = [re.sub('[^\w\s]+', '', s) for s in df3['Issue'].tolist()]
df3['Company'] = [re.sub('[^\w\s]+', '', s) for s in df3['Company'].tolist()]
df3['State'] = [re.sub('[^\w\s]+', '', s) for s in df3['State'].tolist()]
df3['ZIP code'] = [re.sub('[^\w\s]+', '', s) for s in df3['ZIP code'].tolist()]
df3.to_csv('result3.csv')
df3 = pd.read_csv('result3.csv')

df3['Product'] = df3['Product'].str.lower()
df3['Issue'] = df3['Issue'].str.lower()
df3['Company'] = df3['Company'].str.lower()

# nltk.download('stopwords')
" ".join(stopwords.words('english'))
stop_words = set(stopwords.words('english'))


def remove_stop(x):
    return " ".join([word for word in str(x).split() if word not in stop_words])


df3['Product'] = df3['Product'].apply(lambda x: remove_stop(x))
df3['Issue'] = df3['Issue'].apply(lambda x: remove_stop(x))
df3['Company'] = df3['Company'].apply(lambda x: remove_stop(x))

df4 = df3[["Product", "Issue", "Company", "State", "ZIP code", "Complaint ID"]]

df4.to_csv('result4.csv')
df4 = pd.read_csv('result4.csv')

df5 = df4.sort_values('Product')
df5 = df5[["Product", "Issue", "Company", "State", "ZIP code", "Complaint ID"]]
df5.to_csv('result5.csv')
df5 = pd.read_csv('result5.csv')
"""



