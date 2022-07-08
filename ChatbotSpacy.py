from ntpath import join
import spacy
import nltk
from nltk.corpus import stopwords
from spacy.matcher import Matcher
from spacy import displacy
from spacy.lang.es.examples import sentences
from spellchecker import SpellChecker


spell = SpellChecker(language="es")
misspelled = ["abua"]
#misspelled = spell.unknown(misspelled)
for word in misspelled:
    print(word, spell.correction(word))

nlp = spacy.load("es_core_news_md")

stopword_es = nltk.corpus.stopwords.words('spanish')

text = "Hace muchas semanas que no tenemos agua. Ya hablamos al gobierno y no nos hicieron caso."
doc = nlp(text)
doc1 = nlp("Falta de agua")

print(doc.similarity(doc1))

tokenizer = nlp.tokenizer
tokens = tokenizer(text)

limp = [x.orth_ for x in tokens if (not x.is_punct and not x.is_stop)]
limp = " ".join(limp)
print(limp)
limp = nlp(limp)
for t in limp:
    print(t.text, t.pos_, t.lemma_)
