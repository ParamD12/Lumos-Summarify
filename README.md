# Lumos-Summarify
Extractive Summarization using Gensim

Extractive Summarization: In this process, we focus on the vital information from the input sentence and extract that specific sentence to generate a summary. There is no generation of new sentences for summary, they are exactly the same that is present in the original group of input sentences.
Extractive text summarization involves the selection of phrases and sentences from the source document to make up the new summary. Techniques involve ranking the relevance of phrases in order to choose only those most relevant to the meaning of the source.

Using our front-end we will take the url of web-page and word-count of the summary that user wants, and then we will fetch the web-page from url, extract the content from web-page in a text format and then this text will be summarized. The summary generated will then be displayed on the screen as output.

The approach that we have used for this project is by TextRank algorithm, which our library Gensim uses. Gensim uses TextRank algorithm for summarization, where words are represented as vertices on a graph and the more connections a vertex has to other vertices in the graph indicates that the word at the vertex is more “important” and therefore it’s more likely that this word will appear in the summary. TextRank does not rely on any previous training data and can work with any arbitrary piece of text.
 
Tools Used
●	Google Colab
●	Jupyter Notebook

Technology
●	Gensim - Gensim is an open-source library for unsupervised topic modeling, document indexing, retrieval by similarity, and other natural language processing functionalities, using modern statistical machine learning. Gensim is implemented in Python and Cython for performance.
●	BeautifulSoup - Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.
●	Urllib - urllib is a package that collects several modules for working with URLs: urllib. request for opening and reading URLs.
●	Tkinter - Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, and is Python's de facto standard GUI. Tkinter is included with standard Linux, Microsoft Windows and macOS installs of Python. The name Tkinter comes from Tk interface.
●	Request - Requests is a HTTP library for the Python programming language. The goal of the project is to make HTTP requests simpler and more human-friendly. The current version is 2.28.0. Requests is released under the Apache License 2.0. Requests is one of the most popular Python libraries that is not included with Python.
