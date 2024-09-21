import re
from collections import Counter

# Function to count word frequency
def count_word_frequency(file_path, filter_words=None):
    if filter_words is None:
        filter_words = []
    
    # Read the file
    with open(file_path, 'r') as file:
        text = file.read().lower() # Convert to lower case
        
    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text)
    
    # Filter out unwanted words
    words = [word for word in words if word not in filter_words]
    
    # Count the frequency of each word
    return Counter(words)

# Function to print the summary
def print_summary(counter):
    for word, count in counter.most_common():
        print(f"{word}: {count}")

# Define a list of words to filter out
filter_words = ['self', 'init', '__init__', 'def', 'class', '__main__', '__name__']

# Path to your text file
file_path = '/Users/macsimova/totally-malware/CloudPythonUncategorized/predator_nov2023/predator_mr0x1_1a90d686ee9228f71e86511588b3ac9ab1ae8c71b6ed192ee382168927ca6394.py'

# Get the word frequency
word_freq = count_word_frequency(file_path, filter_words)

# Print the summary
print_summary(word_freq)
