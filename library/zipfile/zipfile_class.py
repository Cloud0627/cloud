import zipfile

#zipファイルを読み込む
files = zipfile.ZipFile("test.zip")

#内容を確認する
print(files.namelist())

#解凍する
files.extractall()

#ファイルを解放する
files.close()