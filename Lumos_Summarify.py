#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox
from gensim.summarization.summarizer import summarize
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_text(url):
    page = urlopen(url)
    soup = BeautifulSoup(page, "lxml")
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return soup.title.text, text

def summarize_text():
    url = entry_url.get()
    word_count = int(entry_word_count.get())
    text = get_text(url)
    number_of_words2 = len(str(text).split())
    summary = summarize(str(text), word_count=word_count)
    lines = summary.split()
    number_of_words = len(lines)
    soup = BeautifulSoup(urlopen(url))
    title = soup.title.get_text()
    result = f"Summary:\n\n{title}\n{summary}\n\nMetrics - \n\nOriginal text character length - {len(str(text))}\nSummarized text character length - {len(summary)}\nOriginal text word count - {number_of_words2}\nSummarized text word count - {number_of_words}"
    messagebox.showinfo("Summary", result)

root = tk.Tk()
root.title("Text Summarizer")

frame = tk.Frame(root)
frame.pack()

label_url = tk.Label(frame, text="Enter URL:")
label_url.grid(row=0, column=0, padx=10, pady=10)

entry_url = tk.Entry(frame)
entry_url.grid(row=0, column=1, padx=10, pady=10)

label_word_count = tk.Label(frame, text="Enter word count of summary:")
label_word_count.grid(row=1, column=0, padx=10, pady=10)

entry_word_count = tk.Entry(frame)
entry_word_count.grid(row=1, column=1, padx=10, pady=10)

button = tk.Button(frame, text="Summarize", command=summarize_text)
button.grid(row=2, column=1, pady=10)

root.mainloop()

