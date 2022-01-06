# Textify-A Text Preprocessing Web Application
## A text preprocessing web application which helps a user to get the summary of an Article and also a text generator which generates text based on user input

### Technologies used
+ [Flask](https://flask.palletsprojects.com/en/2.0.x/) (**A micro web Framework**)
+ [nltk](https://www.nltk.org/) (**Python Library**)
+ [Hugging Face GPT-2](https://huggingface.co/) (**For text generation**)
+ [HTML,CSS,JS](https://www.w3schools.com/whatis/) (**Frontend Landing Page**)
+ [Pyhton](https://www.python.org/) (**Programming language For Backend**)
+ [Pytorch](https://pytorch.org/) (**For text generation**)
+ [Tensorflow](https://www.tensorflow.org/) (**An end-to-end open source machine learning platform**)
---
## Working of this application
Firstly the Application is Command line based executable under Python Environment and uses popular Python micro web framework that is FLASK.This Application consist of 2 main pages runs in LocalHost wherein intially a form is given to the user based on the content entered and on submit by the user,Accordingly the Summarizied Content is analyzed with support and importing of some python packages.This data is exported to the next connecting page.

**For text generation**
Hugging Face is an NLP focused startup that shares a large open-source community and provides an open-source library for Natural Language Processing. Their core mode of operation for natural language processing revolves around the use of Transformers. This python based library exposes an API to use many well-known architectures that help obtain the state of the art results for various NLP tasks like text classification, information extraction, question answering, and text generation. All the architectures provided come with a set of pre-trained weights utilizing deep learning that help with ease of operation for such tasks.These transformer models come in different shape and size architectures and have their ways of accepting input data tokenization. A tokenizer takes an input word and encodes the word into a number, thus allowing faster processing.

## This Project Comprises of 3 Modules namely
+ Landing Page
+ Summarized Content as Output
+ Text Generation as Output

Run the these Commands in the Windows Terminal:

**Note Before Running the text-summarisation run these commands**

`pip install nlp`

**For exporting and processing the data,run the following script in new .py file before ruuning the application as follows:**

```python
   import nltk
   nltk.download('stopwords')
   nltk.download('word_tokenize')
   nltk.download('sent_tokenize')
```
**In order to run and intialize the application there are 2 alternative methods:**
+ Method - 1 : Run from Editor in venv and view localhost application in any Browser with link 
(http://127.0.0.1:5000/)
+ Method - 2 : Run from command prompt with specified path location of project by using following command

```
 python __init__.py
```
**Landing Page**

![alt text](https://github.com/VivekChoudhary77/Textify-text-preprocessing/blob/master/Images/Screenshot%20(6).png)
