import ipsum
import lorem

# Laden des englischen Sprachmodells
model = ipsum.load_model("it")

# Gibt eine Liste von 3 Strings zurück, die jeweils einem Absatz in englischer Sprache ähneln
paragraphs = model.generate_paragraphs(3)
# print(paragraphs)

# Gibt eine Liste von 10 Strings zurück, die jeweils einem vollständigen Satz in englischer Sprache ähneln
sentences = model.generate_sentences(10)
print(sentences)

# Gibt eine Liste von 50 Wörtern zurück (enthält keine Interpunktion)
words = model.generate_words(5000)
# print(words)

import lorem

s = lorem.sentence() # 'Eius dolorem dolorem labore neque.'
print(s)
p = lorem.paragraph()
t = lorem.text()
print(p)
print(t)
