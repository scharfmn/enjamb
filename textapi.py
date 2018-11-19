import textprep as prep
import textproc as nlp

def process_text(text):
    preprocessed = prep.preprocess(text)
    doc = nlp.prepare_text(text)
    words = nlp.extract_words(doc)
    unique = nlp.uniquify_words(words)
    return {
        'svg': nlp.display_dependencies(doc),
        'word_count': nlp.count_words(words),
        'words': nlp.format_words(unique),
    }