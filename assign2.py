# Word Counter from Text File

filename = "sample.txt"

try:
    with open(filename, "r") as file:
        text = file.read()

    # Count lines
    lines = text.splitlines()
    line_count = len(lines)

    # Count words
    words = text.split()
    word_count = len(words)

    # Count characters
    character_count = len(text)

    print("===== WORD COUNTER =====")
    print("Number of lines      :", line_count)
    print("Number of words      :", word_count)
    print("Number of characters :", character_count)

except FileNotFoundError:
    print("File not found!")