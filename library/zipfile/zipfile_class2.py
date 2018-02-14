import zipfile

#ZIPファイルを書き込みモードで生成する
zip_file = zipfile.ZipFile("test.zip",mode="w")

#ファイルを追加する
zip_file.write("test1.txt")
zip_file.write("test2.txt")
zip_file.write("test3.txt")

zip_file.close()