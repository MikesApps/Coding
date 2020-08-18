#conda create -n shiny_new_env
#conda env list
#conda activate shiny_new_env
#pip freeze > requirements.txt

#pip install -r requirements.txt
#https://medium.com/@boscacci/why-and-how-to-make-a-requirements-txt-f329c685181e






#ANd now, onto the program
import nltk
#nltk.download('words')
from nltk.corpus import words
#"fine" in words.words()


def drop_char_index(s, i):
    if i == 0:
        return s[1:]
    elif i == len(s) - 1:
        return s[:i]
    else:
        return s[:i] + s[i+1:]


def recurse(word):
    if word in ('a', 'i'):
        return word
    l = len(word)
    for i in range(l):
        nWord = drop_char_index(word,i)
        if nWord in words.words():
            bleh = recurse(nWord)
        else
