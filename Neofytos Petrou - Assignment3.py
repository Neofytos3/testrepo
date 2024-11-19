{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "fce255d5-02f4-4126-b62b-3adab1f7ab89",
   "metadata": {},
   "source": [
    "# **Assignment 3**\n",
    "\n",
    "### *Neofytos Petrou*"
   ]
  },
  {
   "attachments": {
    "fbf02d0b-74da-4829-8369-45386e86c50c.png": {
     "image/png": "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"
    }
   },
   "cell_type": "markdown",
   "id": "59db87b5-ed04-48ae-a621-3f1e957487bf",
   "metadata": {},
   "source": [
    "## Part I (80%)\n",
    "\n",
    "Write a class that implements the [Vector Space Model](https://en.wikipedia.org/wiki/Vector_space_model) and more precisely the [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) weighting scheme $tf-idf$. This scheme is a way to represent with a vector a natural language document. In order to build such a representation for each document in a collection of documents (for example, list of stings in Python terms), one needs to first create a vocabulary which holds (in its simplest variation) all the distinct words (or tokens) in the collection. For example, if our collection consists of the following documents:\n",
    "\n",
    "```python\n",
    "corpus = ['This is the first document.',\n",
    "          'This document is the second document.',\n",
    "          'And this is the third one.',\n",
    "          'Is this the first document?']\n",
    "```\n",
    "the corresponding vocabulary would be the following:\n",
    "\n",
    "```python\n",
    "['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this']\n",
    "```\n",
    "\n",
    "Once a vocabulary is established we can vectorize each document in the collection.\n",
    "For example, if we use a simple binary scheme that denotes the absence or the presence of word in the document one could obtain a vector as depicted in the following figure.\n",
    "\n",
    "![vector_space_model.png](attachment:fbf02d0b-74da-4829-8369-45386e86c50c.png)\n",
    "\n",
    "Note that the index of each value in the vectorized document corresponds to the index of each work in the vocabulary. The word `and` at index 0, the word `document` at index 1 etc.\n",
    "\n",
    "Why it is important to represent as vectors? Simply because we can perform mathematical operations which enable us to solve tasks as Document Retrieval or Document Classification (more info [here](https://en.wikipedia.org/wiki/Information_retrieval_applications)).\n",
    "\n",
    "The $tf-idf$ scheme is the product of two statistics, the term frequency of a word in the document, that is how many time appears in the document and the **inverse document frequency** which measures how frequent is the term on the full collection of documents. More formally for a term $t$ in a document $d$:\n",
    "$$\n",
    "tf(t,d) = f_{t,d},\n",
    "$$\n",
    "where $f_{t,d}$ is the number of times term $t$ occurs in document $d$.\n",
    "\n",
    "The inverse document frequency for a term $t$ in a collection of documents $D$ is defined as:\n",
    "$$\n",
    "idf(t,D) = \\log\\frac{1+N}{n_t+1} + 1\n",
    "$$\n",
    "where $N=|D|$ is the number of the documents in collection $D$ and $n_t$ is the number of documents the term $t$ appears.\n",
    "\n",
    "Finally, the $tf-idf(t,d,D)$ weighting scheme is calculated as their product: $tf(t,d)*idf(t,d,D)$ \n",
    "\n",
    "\n",
    "### Details\n",
    "The class that you will implement should have two methods:\n",
    " - A method (called `fit()`) that takes as input a list of documents (strings) and learns the vocabulary as well as the appropriate statistics of the collection (`idf`). Note that we learn once the vocabulary on a certain collection of documents. The same vocabulary will be used to transform any new collection of documents.\n",
    " - A method (called `transform()`) that take as input a list of documents (strings) and returns a list of lists (matrix) where each list corresponds to a document of the input list and represents it in terms of the $tf-idf$ weighting scheme.\n",
    " \n",
    "You will need to [tokenize](https://en.wikipedia.org/wiki/Lexical_analysis#Tokenization) each document. To do so just split the document using the white space by just using the `split()` function. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bdcd2df9-c5d4-4a44-8415-8005f373df52",
   "metadata": {},
   "outputs": [],
   "source": [
    "# An example\n",
    "collection = [\"This is a document\",\"This is a second document\"]\n",
    "tokenized_docs = [s.split() for s in collection] # lowercase and then split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "94e47a3f-6fc8-4b97-81ea-4a8a27962ad8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['This', 'is', 'a', 'document'], ['This', 'is', 'a', 'second', 'document']]\n"
     ]
    }
   ],
   "source": [
    "print(tokenized_docs)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "78615a93-1b2a-4a30-9673-634ffc458600",
   "metadata": {},
   "source": [
    "The class that you will define should have at least the following properties in the `__init__` function:\n",
    "\n",
    "- The maximum size of the vocabulary (`v_max`). If the vocabulary on the collection exceeds this number then you should truncate it by keeping the `v_max` most frequent terms. **Hint: the function [sorted()](https://docs.python.org/3/library/functions.html#sorted) may be of use.**\n",
    "- A boolean flag which indicates whether you should lowercase each document before tokenizing it."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4ed0ae0e-89e8-442c-9563-aa9dca88b890",
   "metadata": {},
   "source": [
    "### Hints\n",
    "\n",
    "- For the tokenization you can use the code provided in the previous cells. For lowercasing you can just use the corresponding function in the [string class](https://docs.python.org/2/library/string.html#string-functions).\n",
    "- Sorted can be handy for those that want to use it. For example, if one wanted to sort a dictionary by the value in reverse order one can use the following snippet:\n",
    "```python\n",
    "sorted({\"a\":1,\"b\":3,\"c\":6,\"d\":2}.items(),key=lambda k: k[1],reverse=True)\n",
    "```\n",
    "Here we used a `lambda` function which is a simple way of [creating functions](https://www.w3schools.com/python/python_lambda.asp). In the previous example, it will just take the argument `k` which is a tuple (as returned by the `items()` function of the dictionary) and will return the value. This tells to the function `sorted()` to sort the items in the dictionary by their value."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "203debb3-d83d-417c-8d66-d549df2b6c04",
   "metadata": {},
   "source": [
    "### Example input and output\n",
    "For the following example collection:\n",
    "\n",
    "```python\n",
    "corpus = ['The hotel and the stay were great',\n",
    "          'This was a great stay',\n",
    "          'Great stay in a great destination',\n",
    "          'Great destination']\n",
    "```\n",
    "\n",
    "the transform method should return the following list of lists with the $tf-idf$ representation:\n",
    "\n",
    "```python\n",
    "[[1.91629073 1.91629073 1.91629073 1.91629073 1.22314355 1.91629073 1.22314355 0. 0. 0. 0. 0. 0. ]\n",
    "[0. 0. 0. 0. 1.22314355 0. 1.22314355 1.91629073 1.91629073 0. 0. 0. 1.51082562]\n",
    "[0. 0. 0. 0. 1.22314355 0. 1.22314355 0. 0. 1.51082562 1.91629073 1.51082562 1.51082562]\n",
    "[0. 0. 0. 0. 0. 0. 0. 0. 0. 1.51082562 0. 1.51082562 0. ]]\n",
    "```\n",
    "\n",
    "which corresponds to the following vocabulary: ['The',\n",
    "'hotel',\n",
    "'and',\n",
    "'the',\n",
    "'stay',\n",
    "'were',\n",
    "'great',\n",
    "'This',\n",
    "'was',\n",
    "'Great',\n",
    "'in',\n",
    "'destination',\n",
    "'a']\n",
    "\n",
    "Note that for this example we used the same collection of documents to learn the vocabulary. Your class should be able transform any new collection of documents.\n",
    "\n",
    "So, if we used the above `corpus` to fit the vocabulary and then we would like to transform another collection like,\n",
    "\n",
    "```python\n",
    "collection2 = ['This was a wonderful stay',\n",
    "               'Dear customer thanks for your review',\n",
    "              ]\n",
    "```\n",
    "\n",
    "the transform function should return:\n",
    "\n",
    "```python\n",
    "[[0. 0. 0. 0. 1.22314355 0. 0. 1.91629073 1.91629073 0. 0. 0. 1.51082562]\n",
    "[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. ]]\n",
    "```\n",
    "\n",
    "You will observe that the second document gets a vector of zeros. This is normal as none of the words in it is found in the vocabulary that was fit in the previous corpus."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4eee32d1-c6eb-4fcc-8290-cd68101ba786",
   "metadata": {},
   "source": [
    "## Solution Part I"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "801e6148-6cad-4c11-9b90-44cb8fae0f41",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Solution Part I\n",
    "import math\n",
    "\n",
    "class TFIDF:\n",
    "    def __init__(self,v_max,lowercase=True):\n",
    "        self.v_max = v_max\n",
    "        self.lowercase = lowercase\n",
    "        self.idf = {}\n",
    "        self.vocabulary = []\n",
    "        \n",
    "    def calculate_statistics(self, corpus):\n",
    "        tokenized_corpus=[s.split() for s in corpus] #tokenize each document\n",
    "        vocabulary_shell=[]\n",
    "        \n",
    "        for i in tokenized_corpus: #turning the list of lists into a single list\n",
    "            vocabulary_shell=vocabulary_shell+i\n",
    "\n",
    "        if self.lowercase: #creating the boolean flag\n",
    "            vocabulary_shell=[s.lower() for s in vocabulary_shell] #turning words to lowercase\n",
    "        else:\n",
    "            vocabulary_shell\n",
    "\n",
    "        \n",
    "        self.vocabulary=list(set(vocabulary_shell))#we know that sets contain only unique values/strings so we turn the vocabulary into a set and then back to list\n",
    "        #We set the vocabulary lets go to the other statistics\n",
    "\n",
    "        #We need to find the number of documents that each term appears in\n",
    "        terms=len(self.vocabulary)\n",
    "        number_of_documents=[0,]*terms #create a list that will count the frequency\n",
    "        number_of_documents=dict(zip(self.vocabulary,number_of_documents)) #make it into a dictionary to have as key-value the term-frequency\n",
    "        for i in tokenized_corpus:\n",
    "            for j in set(i): \n",
    "                if j in number_of_documents:\n",
    "                    number_of_documents[j]+=1\n",
    "        \n",
    "        #Sort the the terms by most frequent and then from the sorted terms we sort the self.vocabulary\n",
    "        number_of_documents1=dict(sorted(number_of_documents.items(),key=lambda k: k[1],reverse=True))\n",
    "        self.vocabulary=[key for key in number_of_documents1]\n",
    "        self.vocabulary=[word for word in self.vocabulary[:self.v_max]] #Make v_max decide the size of the vocabulary\n",
    "\n",
    "        #Setting the vectorized document\n",
    "        #Find tf\n",
    "        vectorized_documents=[] \n",
    "        for i in tokenized_corpus:\n",
    "            term_times1=[i.count(term) for term in self.vocabulary]\n",
    "            vectorized_documents.append(term_times1) #vectorize each document\n",
    "            \n",
    "        \n",
    "        \n",
    "\n",
    "        #Find idf\n",
    "        self.idf={}\n",
    "        documents=len(corpus)\n",
    "        for key,value in number_of_documents1.items(): \n",
    "            self.idf[key]=math.log((1+documents)/(1+value))+1\n",
    "        a=list(self.idf.values())\n",
    "\n",
    "        \n",
    "        \n",
    "        #Check the processes   \n",
    "        #return print(tokenized_corpus, '\\n \\n ' , vocabulary_shell , '\\n \\n ' ,self.vocabulary, '\\n \\n ' , vectorized_documents,'\\n \\n',number_of_documents,'\\n \\n',number_of_documents1, '\\n \\n' , self.idf, '\\n \\n ', a)\n",
    "        return print(\"The vocabulary is : \",'\\n',self.vocabulary,'\\n')\n",
    "\n",
    "    \n",
    "    def fit(self, corpus):\n",
    "        self.calculate_statistics(corpus)\n",
    "        #return print(self.vocabulary) \n",
    "        \n",
    "    def transform(self,corpus):\n",
    "        \n",
    "        tokenized_corpus=[s.split() for s in corpus]\n",
    "   \n",
    "        a=list(self.idf.values())\n",
    "\n",
    "        vectorized_documents=[]\n",
    "        tf_idf=[]\n",
    "        \n",
    "        for i in tokenized_corpus:\n",
    "            term_times1=[i.count(term) for term in self.vocabulary]\n",
    "            vectorized_documents.append(term_times1) #vectorize each document\n",
    "\n",
    "        vectorized_documents=[[float(k) for k in i] for i in vectorized_documents]\n",
    "        for i in range(len(vectorized_documents)):\n",
    "            tf_idf.append([vectorized_documents[i][j]*a[j] for j in range(len(vectorized_documents[i]))])\n",
    "        return print('The tf-idf representation is:','\\n \\n', tf_idf, '\\n \\n')\n",
    "        \n",
    "    \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "10b83a85-240c-49b8-9592-999ff2f71486",
   "metadata": {},
   "outputs": [],
   "source": [
    "corpus1=['The hotel and the stay were great',\n",
    "          'This was a great stay',\n",
    "          'Great stay in a great destination',\n",
    "          'Great destination']\n",
    "\n",
    "corpus2 = ['This is the first document',\n",
    "          'This document is the second document',\n",
    "          'And this is the third one',\n",
    "          'Is this the first document']\n",
    "corpus3 = ['This was a wonderful stay',\n",
    "               'Dear customer thanks for your review']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "6dde1f91-d6e4-4336-a5a6-382daa093f5d",
   "metadata": {},
   "outputs": [],
   "source": [
    "test= TFIDF(v_max=13,lowercase=False) #Without lowercase\n",
    "test2= TFIDF(v_max=13,lowercase=True) #With Lowercase"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "0fa039e1-43bf-4cd6-b6b3-32e83ab77e69",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The vocabulary is :  \n",
      " ['stay', 'great', 'a', 'Great', 'destination', 'hotel', 'were', 'This', 'in', 'and', 'the', 'The', 'was'] \n",
      "\n",
      "The vocabulary is :  \n",
      " ['stay', 'great', 'a', 'destination', 'hotel', 'were', 'in', 'and', 'the', 'was', 'this'] \n",
      "\n"
     ]
    }
   ],
   "source": [
    "test.fit(corpus1)\n",
    "test2.fit(corpus1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "d6ccb413-7b42-437e-90b9-5e73d8df4a73",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The tf-idf representation is: \n",
      " \n",
      " [[1.2231435513142097, 1.2231435513142097, 0.0, 0.0, 0.0, 1.916290731874155, 1.916290731874155, 0.0, 0.0, 1.916290731874155, 1.916290731874155, 1.916290731874155, 0.0], [1.2231435513142097, 1.2231435513142097, 1.5108256237659907, 0.0, 0.0, 0.0, 0.0, 1.916290731874155, 0.0, 0.0, 0.0, 0.0, 1.916290731874155], [1.2231435513142097, 1.2231435513142097, 1.5108256237659907, 1.5108256237659907, 1.5108256237659907, 0.0, 0.0, 0.0, 1.916290731874155, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.5108256237659907, 1.5108256237659907, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]] \n",
      " \n",
      "\n",
      "The tf-idf representation is: \n",
      " \n",
      " [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.916290731874155, 0.0, 0.0, 1.916290731874155, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.916290731874155, 0.0, 0.0, 1.916290731874155, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.916290731874155, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.916290731874155, 0.0, 0.0]] \n",
      " \n",
      "\n",
      "The tf-idf representation is: \n",
      " \n",
      " [[1.2231435513142097, 0.0, 1.5108256237659907, 0.0, 0.0, 0.0, 0.0, 1.916290731874155, 0.0, 0.0, 0.0, 0.0, 1.916290731874155], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]] \n",
      " \n",
      "\n"
     ]
    }
   ],
   "source": [
    "#Tf-idf for corpus1 without lowercase then tf-idf for corpus2 and corpus3 based of corpus1's vocabulary\n",
    "vectors_corpus1=test.transform(corpus1)\n",
    "vectors_corpus2=test.transform(corpus2)\n",
    "vectors_corpus3=test.transform(corpus3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "8ed2cabc-fff4-46b9-8629-940efe7c87ae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The tf-idf representation is: \n",
      " \n",
      " [[1.2231435513142097, 1.2231435513142097, 0.0, 0.0, 1.916290731874155, 1.916290731874155, 0.0, 1.916290731874155, 1.916290731874155, 0.0, 0.0], [1.2231435513142097, 1.2231435513142097, 1.5108256237659907, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.916290731874155, 0.0], [1.2231435513142097, 1.2231435513142097, 1.5108256237659907, 1.5108256237659907, 0.0, 0.0, 1.916290731874155, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.5108256237659907, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]] \n",
      " \n",
      "\n"
     ]
    }
   ],
   "source": [
    "#Tf-idf for corpus1 with lowercase\n",
    "vectors_corpus4=test2.transform(corpus1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "00704f4c-4576-4e1d-9935-987ba1e3985e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The vocabulary is :  \n",
      " ['stay', 'great', 'a', 'Great', 'destination', 'hotel', 'were', 'This', 'in', 'and', 'the', 'The', 'was'] \n",
      "\n",
      "The vocabulary is :  \n",
      " ['stay', 'great', 'a', 'Great', 'destination'] \n",
      "\n",
      "The tf-idf representation is: \n",
      " \n",
      " [[1.2231435513142097, 1.2231435513142097, 0.0, 0.0, 0.0, 1.916290731874155, 1.916290731874155, 0.0, 0.0, 1.916290731874155, 1.916290731874155, 1.916290731874155, 0.0], [1.2231435513142097, 1.2231435513142097, 1.5108256237659907, 0.0, 0.0, 0.0, 0.0, 1.916290731874155, 0.0, 0.0, 0.0, 0.0, 1.916290731874155], [1.2231435513142097, 1.2231435513142097, 1.5108256237659907, 1.5108256237659907, 1.5108256237659907, 0.0, 0.0, 0.0, 1.916290731874155, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.5108256237659907, 1.5108256237659907, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]] \n",
      " \n",
      "\n",
      "The tf-idf representation is: \n",
      " \n",
      " [[1.2231435513142097, 1.2231435513142097, 0.0, 0.0, 0.0], [1.2231435513142097, 1.2231435513142097, 1.5108256237659907, 0.0, 0.0], [1.2231435513142097, 1.2231435513142097, 1.5108256237659907, 1.5108256237659907, 1.5108256237659907], [0.0, 0.0, 0.0, 1.5108256237659907, 1.5108256237659907]] \n",
      " \n",
      "\n"
     ]
    }
   ],
   "source": [
    "#Checking and comparing v_max for test= TFIDF(v_max=13,lowercase=False)\n",
    "test6= TFIDF(v_max=5,lowercase=False)\n",
    "test.fit(corpus1)\n",
    "test6.fit(corpus1)\n",
    "vectors_corpus1=test.transform(corpus1)\n",
    "vectors_corpus7=test6.transform(corpus1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "03b760a4-f8f6-4552-927e-f5f483e2fe5e",
   "metadata": {},
   "source": [
    "## Part II (20%)\n",
    "\n",
    "Extend the previous class by adding a stop-word removal component. [Stop words](https://en.wikipedia.org/wiki/Stop_word) are words that are the most common ones in a language. For example, words like articles `the, he, she, it` or words like `and, or` they do not bring any information and usually are removed from the vocabulary.\n",
    "\n",
    "The extended class should implement the removal of the stop words from the vocabulary. For this purpose, the class should have a boolean flag that indicates whether we wish to apply stop-word removal and a property that keeps the stop words in a list. This can be given as an argument in the `__init__` function.\n",
    "\n",
    "Note that as you will inherit from the previous class, you should re-use its functions and only modify what is needed to enable stop-word removal.\n",
    "\n",
    "A typical list of stop words you can use is the following:\n",
    "\n",
    "```python\n",
    "stopwords = [\"and\", \"a\", \"the\",\"it\",\"he\",\"she\",\"where\",\"was\",\"for\"]\n",
    "```\n",
    "You can find more stop words at the links section of the [Wikipedia page](https://en.wikipedia.org/wiki/Stop_word).\n",
    "\n",
    "### Hints\n",
    "\n",
    "In lists you can use the `in` operator to check whether an element exists in a list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 269,
   "id": "5328ec3b-0315-4887-9919-5e70a84fec01",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 269,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Example of in operator\n",
    "stopwords = [\"and\", \"a\", \"the\",\"it\",\"he\",\"she\",\"where\",\"was\",\"for\"]\n",
    "\"and\" in stopwords"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "37ba667e-74ca-4fa6-98fa-cbbfcf840477",
   "metadata": {},
   "source": [
    "## Solution Part II"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "ac4c7041-0d9f-47d2-8255-dc0b3809ef6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "class STOP_WORD(TFIDF):\n",
    "    \n",
    "    def __init__(self,v_max,lowercase=True,stop_word=True,wordlist=None):\n",
    "        super().__init__(v_max,lowercase)\n",
    "        \n",
    "        self.stop_word = stop_word\n",
    "        self.wordlist = wordlist\n",
    "\n",
    "    def fit(self, corpus):\n",
    "        super().fit(corpus)\n",
    "        if self.stop_word:\n",
    "            vocabulary_removal=self.vocabulary #create a copy of the vocabulary\n",
    "            self.vocabulary=[]    #empty the vocabulary we had to create the new one after we remove the words\n",
    "            for i in vocabulary_removal:  \n",
    "                if i not in self.wordlist:\n",
    "                    self.vocabulary.append(i)\n",
    "            \n",
    "        else:\n",
    "            self.vocabulary\n",
    "        return print('The vocabulary after removing the words : ','\\n ',self.vocabulary,'\\n')\n",
    "\n",
    "    def transform(self,corpus):\n",
    "        super().transform(corpus)\n",
    "\n",
    "\n",
    "stopwords = [\"The\",\"and\", \"a\", \"the\",\"it\",\"he\",\"she\",\"where\",\"was\",\"for\",\"This\"]    \n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "6028970d-2076-4016-b231-16d04fe1422a",
   "metadata": {},
   "outputs": [],
   "source": [
    "test3= STOP_WORD(v_max=13,lowercase=False,stop_word=True,wordlist=stopwords) #Without lowercase documents\n",
    "test4= STOP_WORD(v_max=13,lowercase=True,stop_word=True,wordlist=stopwords) #With lowercase documents\n",
    "test5= STOP_WORD(v_max=5,lowercase=True,stop_word=True,wordlist=stopwords) #With lowercase and v_max"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "c7299573-a7a3-4a6a-8b86-fd977c964536",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The vocabulary is :  \n",
      " ['stay', 'great', 'a', 'Great', 'destination', 'hotel', 'were', 'This', 'in', 'and', 'the', 'The', 'was'] \n",
      "\n",
      "The vocabulary after removing the words :  \n",
      "  ['stay', 'great', 'Great', 'destination', 'hotel', 'were', 'in'] \n",
      "\n",
      "The vocabulary is :  \n",
      " ['stay', 'great', 'a', 'destination', 'hotel', 'were', 'in', 'and', 'the', 'was', 'this'] \n",
      "\n",
      "The vocabulary after removing the words :  \n",
      "  ['stay', 'great', 'destination', 'hotel', 'were', 'in', 'this'] \n",
      "\n",
      "The vocabulary is :  \n",
      " ['stay', 'great', 'a', 'destination', 'hotel'] \n",
      "\n",
      "The vocabulary after removing the words :  \n",
      "  ['stay', 'great', 'destination', 'hotel'] \n",
      "\n"
     ]
    }
   ],
   "source": [
    "#Vocabulary before and after\n",
    "test3.fit(corpus1)\n",
    "test4.fit(corpus1)\n",
    "test5.fit(corpus1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "32693767-9684-43d4-a7b4-f3235fe1d586",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The tf-idf representation is: \n",
      " \n",
      " [[1.2231435513142097, 1.2231435513142097, 0.0, 0.0, 1.5108256237659907, 1.916290731874155, 0.0], [1.2231435513142097, 1.2231435513142097, 0.0, 0.0, 0.0, 0.0, 0.0], [1.2231435513142097, 1.2231435513142097, 1.5108256237659907, 1.5108256237659907, 0.0, 0.0, 1.916290731874155], [0.0, 0.0, 1.5108256237659907, 1.5108256237659907, 0.0, 0.0, 0.0]] \n",
      " \n",
      "\n",
      "The tf-idf representation is: \n",
      " \n",
      " [[1.2231435513142097, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]] \n",
      " \n",
      "\n",
      "The tf-idf representation is: \n",
      " \n",
      " [[1.2231435513142097, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]] \n",
      " \n",
      "\n"
     ]
    }
   ],
   "source": [
    "#Tf-idf after word removal without lowercase\n",
    "vectors_corpus5=test3.transform(corpus1)\n",
    "vectors_corpus6=test3.transform(corpus3)\n",
    "vectors_corpus8=test5.transform(corpus3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "2f18fdb8-0ca1-41bd-ad5c-6c49e844e0a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The tf-idf representation is: \n",
      " \n",
      " [[1.2231435513142097, 1.2231435513142097, 0.0, 1.5108256237659907, 1.916290731874155, 0.0, 0.0], [1.2231435513142097, 1.2231435513142097, 0.0, 0.0, 0.0, 0.0, 0.0], [1.2231435513142097, 1.2231435513142097, 1.5108256237659907, 0.0, 0.0, 1.916290731874155, 0.0], [0.0, 0.0, 1.5108256237659907, 0.0, 0.0, 0.0, 0.0]] \n",
      " \n",
      "\n"
     ]
    }
   ],
   "source": [
    "#Tf-idf after word removal with lowercase\n",
    "vectors_corpus9=test4.transform(corpus1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "4475f145-4979-4d8b-baf3-c8a381172a99",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['great', 'stay', 'a', 'Great', 'destination', 'were', 'was', 'hotel', 'The', 'the', 'This', 'in', 'and']\n",
      "['great']\n",
      "['great', 'stay']\n",
      "['great', 'stay', 'Great']\n",
      "['great', 'stay', 'Great', 'destination']\n",
      "['great', 'stay', 'Great', 'destination', 'were']\n",
      "['great', 'stay', 'Great', 'destination', 'were', 'hotel']\n",
      "['great', 'stay', 'Great', 'destination', 'were', 'hotel', 'in']\n",
      "['great', 'stay', 'Great', 'destination', 'were', 'hotel', 'in']\n"
     ]
    }
   ],
   "source": [
    "#I recorded the process of 'removing' the words and I thought to leave it here\n",
    "test3= STOP_WORD(v_max=13,lowercase=False,stop_word=True,wordlist=stopwords)\n",
    "test3.fit(corpus1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "aaf54e72-8ab6-41ba-8c75-a4c19d6d0a9b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The vocabulary is :  \n",
      " ['stay', 'great', 'a', 'Great', 'destination', 'hotel', 'were', 'This', 'in', 'and', 'the', 'The', 'was'] \n",
      "\n",
      "The vocabulary after removing the words :  \n",
      "  ['stay', 'great', 'Great', 'destination', 'hotel', 'were', 'in'] \n",
      "\n",
      "The tf-idf representation is: \n",
      " \n",
      " [[1.2231435513142097, 1.2231435513142097, 0.0, 0.0, 1.5108256237659907, 1.916290731874155, 0.0], [1.2231435513142097, 1.2231435513142097, 0.0, 0.0, 0.0, 0.0, 0.0], [1.2231435513142097, 1.2231435513142097, 1.5108256237659907, 1.5108256237659907, 0.0, 0.0, 1.916290731874155], [0.0, 0.0, 1.5108256237659907, 1.5108256237659907, 0.0, 0.0, 0.0]] \n",
      " \n",
      "\n"
     ]
    }
   ],
   "source": [
    "test3= STOP_WORD(v_max=13,lowercase=False,stop_word=True,wordlist=stopwords)\n",
    "test3.fit(corpus1)\n",
    "vectors_corpus5=test3.transform(corpus1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b15ab408-1906-4a95-813a-af1ba38308d9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
