import logging
import spacy

nlp = spacy.load('en_core_web_sm')# 
# a spaCy modelized object is conventionally called a "doc"
# use: docify('this is some text') -> spacy_doc

def display_dependencies(doc): # returns svg
    return spacy.displacy.render([doc], style='dep', page=False)

def extract_words(doc): # TODO: refactor: this is actually extracting token text incuding punc, not words
    return [token.text for token in doc]

def count_words(words): # TODO: refactor: words are actually outcome, not input - we're applying a definition
    return len([word for word in words if word.isalnum()])

def uniquify_words(words): # TODO: look into pipelining instead of repeated similar comprehensions
    return set([word.lower() for word in words if word.isalnum()])

def format_words(words):
    return u", ".join(sorted(words))

def prepare_text(preprocessed_text):
    doc = nlp(preprocessed_text) # concventionally spaCy text is called a "doc"
    return doc
