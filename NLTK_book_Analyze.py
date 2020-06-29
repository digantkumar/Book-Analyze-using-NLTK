# Digant Kumar
# Program that takes a novel form the ntlk gutenberg corpus and prints a summary of it

import nltk         # Using the nltk package for text processing
def analyze(book_name):
    word_dict = {}
    words = nltk.corpus.gutenberg.words(book_name)       # Storing the words
    chars = nltk.corpus.gutenberg.raw(book_name)         # Characters
    sentences = nltk.corpus.gutenberg.sents(book_name)   # Sentences
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    longest_word = sorted(word_dict, key=len, reverse=True)
    longest_sen = sorted(sentences, key=len, reverse=True)
    word_split = str(longest_sen[0]).split()
    longest_sentence = word_split[0] + word_split[1] + word_split[2] + '. . .' + word_split[len(word_split) - 2] + \
                       word_split[len(word_split) - 1]
    stemmer = nltk.stem.PorterStemmer()                      # For stemming
    vocab_stem = set([stemmer.stem(vocab) for vocab in set(words) if vocab.isalpha()])
    root_dict = {}
    for index in set(words):
        root_word = stemmer.stem(index)
        if root_word not in root_dict:
            root_dict[root_word] = [index]
        else:
            root_dict[root_word].append(index)
    stem_words = sorted(root_dict.values(), key=len, reverse=True)
    for index in root_dict:
        if root_dict[index] == stem_words[0]:
            stem_word = index
    print("Analysis of '%s'" %(book_name))
    print("# chars = %s" %(len(chars)))
    print("# words = %s" %(len(words)))
    print("# sentences = %s" %(len(sentences)))
    print("Longest word = '%s'" %(longest_word[0]))
    print("Longest Sentence = '%s [%s]' " %(longest_sentence, len(longest_sen[0])))
    print("Vocab Size = %s" %(len(vocab_stem)))
    print("Largest Stem Family '%s': %s" %(stem_word, stem_words[0]))

books = nltk.corpus.gutenberg.fileids()
print(analyze(books[2]))

