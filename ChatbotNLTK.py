import nltk
from nltk.corpus import cess_esp
cess_esp._tagset = "es-cast3lb"
nltk.tag.mapping._load_universal_map("es-cast3lb")  # initialize; normally loaded on demand
mapdict = nltk.tag.mapping._MAPPINGS["es-cast3lb"]["universal"]

oraciones = cess_esp.tagged_sents()
print(oraciones[0])
#defaultTagger = nltk.DefaultTagger('NOUN')
#unigramTagger = nltk.UnigramTagger(oraciones, backoff=defaultTagger)
#bigramTagger = nltk.BigramTagger(oraciones, backoff=unigramTagger)
#trigramTagger = nltk.TrigramTagger(oraciones, backoff=bigramTagger)
#print(trigramTagger.tag("Este banco está ocupado por un padre y por un hijo. El padre se llama Juan y el hijo ya te lo he dicho".split()))