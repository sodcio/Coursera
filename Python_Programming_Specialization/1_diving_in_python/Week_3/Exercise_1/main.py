from solution import FileReader
reader = FileReader('not_exist_file.txt')
text = reader.read()
text

with open('some_file.txt', 'w') as file:
    file.write('some text')

reader = FileReader('some_file.txt')
text = reader.read()
text
'some text'
type(reader)
