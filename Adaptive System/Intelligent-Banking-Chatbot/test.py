import nltk
nltk.download('punkt')

# Ensure nltk_data path is correctly set
nltk.data.path.append('C:\\Users\\admin\\AppData\\Roaming\\nltk_data')

# Sample text
text = "Hello, how are you today?"
tokens = nltk.word_tokenize(text)

print(tokens)
