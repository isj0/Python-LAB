from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
# my_string = ''

for line in lines:
    line = line.replace('Python', 'C++')
    print(line)

    