import spacy
import nltk
from nltk.corpus import stopwords
from spacy.matcher import Matcher
from spacy import displacy
from spacy.lang.es.examples import sentences 

nlp = spacy.load("es_core_news_md")
doc = nlp(sentences[3])

#print(statement1.similarity(statement2))

doc = nlp("No hay agua en mi colonia.")

stopword_es = nltk.corpus.stopwords.words('spanish')

matcher = Matcher(nlp.vocab)
P_FaltaDeAgua = [{"TEXT": "no"}, {"TEXT": "hay"}, {"TEXT": "agua"}]
P_FaltaDeLuz = [{"TEXT": "no"}, {"TEXT": "hay"}, {"TEXT": "luz"}]
matcher.add("NO_HAY_AGUA", [P_FaltaDeAgua])
matcher.add("NO_HAY_LUZ", [P_FaltaDeLuz])
matches = matcher(doc)
print("Matches: ", [doc[start:end].text for match_id, start, end in matches])

NotStopWords=[]
for token in doc:
    if str(token).lower() not in stopword_es:    
        NotStopWords.append(token)
print(NotStopWords)

for token in doc:
    print(token.text, token.pos_, token.dep_)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

displacy.serve(doc, style="dep")
displacy.serve(doc, style="ent")
