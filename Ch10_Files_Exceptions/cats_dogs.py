from pathlib import Path

def read_files(path):
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        # print(f"Sorry, the file {path} does not exist.")
        pass
    else:
        print(f"\n{contents}")
              
file_names = ['cats.txt', 'dogs.txt', 'dragons.txt']

for file in file_names:
    path = Path(file)
    read_files(path)