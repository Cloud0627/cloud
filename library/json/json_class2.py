import json
#JSONデータの書き出し2
#JSON形式のデータ
try:
    #ローカルJSONファイルを読み込む
    with open("sample.json","r") as f:
        data = json.load(f)
        print("data")
        print(data["title"])
        print(data["date"])
        print(data["items"])
except json.JSONDecodeError as e:
    print('JSONDecodeError:',e)
