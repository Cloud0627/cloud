import json
#JSONデータの書き出し
#JSON形式のデータ
data = {
    "title":"JSONサンプル",
    "date":"2017.07.01",
    "items":[
        {
            "title":"タイトル1",
            "contents":"内容"
        },
        {
            "title":"タイトル2",
            "contents":"内容"
        }
    ]
}

#ファイルに書き込む
save_path = "sample.json"
with open(save_path,"w") as outfile:
    json.dump(data,outfile,ensure_ascii = False)

#文字列に変換する
json_str = json.dumps(data)
print(json_str)
json_str = json.dumps(data,ensure_ascii = False)
print(json_str)