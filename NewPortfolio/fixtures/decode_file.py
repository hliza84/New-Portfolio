import chardet

# Detect the encoding of the file
with open("resume.json", "rb") as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    encoding = result["encoding"]

# Read the file using the detected encoding
with open("resume.json", "r", encoding=encoding) as file:
    data = file.read()

print(data)

with open("auth.json", "rb") as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    encoding = result["encoding"]

# Read the file using the detected encoding
with open("auth.json", "r", encoding=encoding) as file:
    data = file.read()
# Process the 'data' variable as needed
# For example, you can print the contents of the file
print(data)
