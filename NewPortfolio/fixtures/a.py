import chardet

with open("file.txt", "rb") as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    encoding = result["encoding"]

with open("file.txt", "r", encoding=encoding) as file:
    data = file.read()
