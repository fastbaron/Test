import pandas as pd

# xlsxファイルを読み込む
df = pd.read_excel("clients_2.xlsx", sheet_name="Sheet1")

# clientsという名前のからのリストを作成する
clients_list = []

unique_clients = df.drop_duplicates(subset=["id", "name", "courses"])
