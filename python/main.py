import os

def word_count(file_path):
    print(f"Current working directory: {os.getcwd()}")  # Print current working directory
    with open(file_path, 'r') as file:
        text = file.read()
    
    words = text.split()
    
    word_counts = Counter(words)
    
    for word, count in word_counts.items():
        print(f"{word}: {count}")

file_path = r"D:\moti\python\vasu.txt"

word_count(file_path)
