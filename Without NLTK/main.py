import string
from collections import Counter
import matplotlib.pyplot as plt

# Opening the file that we want to analys
text = open('read.txt', encoding='utf=8').read()

# Covert all the text to lower case
text_lower = text.lower()

# Remove all the special character
cleaned_text = text_lower.translate(str.maketrans("", "", string.punctuation))

# Tokenized/Convert all the sentence to a single string
tokenized_text = cleaned_text.split()

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Filtering the stop words
final_words = []
for word in tokenized_text:
    if word not in stop_words:
        final_words.append(word)

# Filtering the emotions.txt
emotions_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", "").replace(",", "").replace("'", "").strip()
        word, emotion = clear_line.split(":")

        if word in final_words:
            emotions_list.append(emotion)

print(emotions_list)
# Count the emotions
w = Counter(emotions_list)
print(w)

# Show the analysis on graph
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('grap.png')
plt.show()
