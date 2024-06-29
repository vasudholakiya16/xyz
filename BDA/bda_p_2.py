# import urllib.request

# # URL of the text file
# story_url = "http://sixty-north.com/c/t.txt"

# # Requesting the URL and handling response
# request = urllib.request.Request(story_url)
# response = urllib.request.urlopen(request)

# # Initialize an empty dictionary to store word counts
# word_counts = {}

# # Iterate through each line in the response
# for line in response:
#     # Decode each line from bytes to UTF-8 string and split into words
#     words = line.decode('utf-8').split()
    
#     # Iterate through each word in the list of words
#     for word in words:
#         # Remove punctuation or unwanted characters from each word if necessary
#         word = word.strip('.,?!-()[]{}')  # Example: you can strip common punctuation
        
#         # Convert to lowercase to ignore case sensitivity
#         word = word.lower()
        
#         # Update the word count dictionary
#         if word in word_counts:
#             word_counts[word] += 1
#         else:
#             word_counts[word] = 1

# # Now word_counts dictionary contains the count of each word
# # Print the word counts
# for word, count in word_counts.items():
#     print(f"{word}: {count}")


import urllib.request 
import random
from operator import itemgetter 
current_word = {}
current_count = 0
story ='http://sixty-north.com/c/t.txt'
request = urllib.request.Request(story)
response = urllib.request.urlopen(request)
each_word = []
words = None
count = 1
same_words ={}
word = []
"""looping the entire file"""
#Collect All the words into a list 
for line in response:
    #print "Line = " , line
    line_words = line.split()
    for word in line_words: 
        each_word.append(word)
for words in each_word:
    if words.lower() not in same_words.keys():
        same_words[words.lower()]=1
for line in response:
    line_words =line.split()
    for word in line_words:
        each_word.append(word)
for words in each_word:
    if words.lower() not in same_words.keys():
        same_words[words.lower()]=1
    else:
        same_words[words.lower()]=same_words[words.lower()]+1
for each in same_words.keys():
    print("word =",each, ", count =",same_words[each])