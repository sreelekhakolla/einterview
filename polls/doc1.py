from .views import que
def quess():
    print(len(answers))
    for i in answers:
        doc1 = nlp(i)
        doc2 = nlp(transcript)
        print(doc1.similarity(doc2))