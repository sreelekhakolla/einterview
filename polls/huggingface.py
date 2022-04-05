import spacy
nlp=spacy.load("en_core_web_sm")
def parse():
    doc1=nlp("i am sreelekha")
    doc2=nlp("who are you , are you sreelekha")
    print(doc1.similarity(doc2))
