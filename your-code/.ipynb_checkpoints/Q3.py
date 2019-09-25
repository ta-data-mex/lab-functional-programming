# In the next cell, use filter and lambda to return a list that contains positive numbers only. The output should be:
#
# [1, 4, 5]
import langdetect
from langdetect import detect
from functools import reduce

numbers = [1, 4, -1, -100, 0, 5, -99]
positive_nums_only = list(filter(lambda x: x > 0, numbers))
print("Positive Numbers only: ", positive_nums_only)

words = ['good morning', '早上好', 'доброго', 'おはようございます', 'everyone', '大家', 'каждый', 'みんな']
english_words_list = [x for x in words if langdetect.detect(x) == 'en']
english_words_var = " ".join(english_words_list)

print(english_words_list)
print(english_words_var)


