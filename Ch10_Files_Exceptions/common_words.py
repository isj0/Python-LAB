from pathlib import Path

path = Path('metamorphosis.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the number of times a word appears in this text
    count = contents.lower().count('the ')
    print(f"The word 'the' appears {count} times.")