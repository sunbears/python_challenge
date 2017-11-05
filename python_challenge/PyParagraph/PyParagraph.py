
# coding: utf-8

# In[86]:


#HW#3 PyParagraph
#Your task is to create a Python script to automate the analysis of any such passage using these metrics. 

#Dependencies
import os
import csv


# In[87]:


#Import a text file filled with a paragraph of your choosing.

textpath = os.path.join("PyParagraphText.txt")

text = open(textpath, "r").read()

print(text)


# In[88]:


#Approximate word count

words = text.split(" ")
word_count = len(words)

#Commmas are included in the word which I don't want.
#Remove Commas from words

for z in words:
    z=z.replace(',','')

print('Approximate Word Count: ', word_count)


# In[89]:


#Approximate sentence count
sentences = text.split(".")


# In[90]:


#The last string in the list is empty because the last period makes a split between two strings.
#Remove last item in the sentences list because it's an empty string.
del sentences[-1]
print(sentences)


# In[91]:


#Now we see that the last string that was empty has been dropped.
#Calculate Approximate sentence count
sentence_count = len(sentences)
print('Approximate Sentence Count: ', sentence_count)


# In[92]:


#Approximate letter count (per word)

word_length_list = []

for x in words:
    word_length_list.append(len(x))

avg_word_length = sum(word_length_list)/word_count

print('Average Letter Count: ', avg_word_length)


# In[93]:


#Average sentence length (in words)

sentence_length_list = []

for y in sentences:
    sentence_length_list.append(len(y.split(" ")))

avg_sentence_length = sum(sentence_length_list)/sentence_count

print('Average Sentence Length: ', avg_sentence_length)


# In[94]:


#Putting it all together
print('Paragraph Analysis')
print('------------------')
print('Approximage Word Count: ', word_count)
print('Approximate Sentence Count: ', sentence_count)
print('Average Letter Count: ', avg_word_length)
print('Average Sentence Length: ', avg_sentence_length)

