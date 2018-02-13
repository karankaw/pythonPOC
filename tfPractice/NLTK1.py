um# -*- coding: utf-8 -*-
"""
NLTK Python Set of Libraries
"""
# import nltk
# nltk.download()
#from nltk.tokenize import sent_tokenize, word_tokenize
import nltk as toolba
example_text = "Hello Mr. Smith, how are you doing today? The weather is great \
today and Python is awesome. The sky is having blue, grey and golden."
print(toolba.sent_tokenize(example_text))
print("-----------------------------------------------------------")

print(toolba.word_tokenize(example_text))



