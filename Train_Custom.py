from __future__ import unicode_literals, print_function

import random
from pathlib import Path
import random

import spacy
from spacy.gold import GoldParse
from spacy.tagger import Tagger

model_name = 'en'
entity_label = 'DRUG'
output_directory = 'E:\Twilight\Projects\Python\Spacy_Wednesday\spaCy\spacy\data\en'

def train_ner(nlp, train_data, output_dir):
    for raw_text, _ in train_data:
        doc = nlp.make_doc(raw_text)
        for word in doc:
            _ = nlp.vocab[word.orth]
    random.seed(0)
    nlp.entity.model.learn_rate = 0.001
    for itn in range(1000):
        random.shuffle(train_data)
        loss = 0.
        for raw_text, entity_offsets in train_data:
            doc = nlp.make_doc(raw_text)
            gold = GoldParse(doc, entities=entity_offsets)
            nlp.tagger(doc)
            loss += nlp.entity.update(doc, gold, drop=0.9)
        if loss == 0:
            break
    nlp.end_training()
    if output_dir:
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.save_to_directory(output_dir)


def main("en", output_directory=None):
    print("Loading initial model", "en")
    nlp = spacy.load('en')
    if output_directory is not None:
        output_directory = Path(output_directory)

    train_data = [
    ("paracetamol is a drug",
    [(0, 11, 'DRUG')]),
    ("Drug name is paracetamol",
    [(13, 24, 'DRUG')]),
    ("Paracetamol is a pain reliever",
    [(0, 11, 'DRUG')]),
    ("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol can be used as a drug",
    [(0, 11, 'DRUG')]),
	("Shall I use Paracetamol",
    [(12, 23, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol should me used",
    [(0, 11, 'DRUG')]),
	("I will use Paracetamol",
    [(11, 22, 'DRUG')]),
	("What is Paracetamol",
    [(8, 19, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("paracetamol is a drug",
    [(0, 11, 'DRUG')]),
    ("Drug name is paracetamol",
    [(13, 24, 'DRUG')]),
    ("Paracetamol is a pain reliever",
    [(0, 11, 'DRUG')]),
    ("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol can be used as a drug",
    [(0, 11, 'DRUG')]),
	("Shall I use Paracetamol",
    [(12, 23, 'DRUG')]),
	("Paracetamol will reduce fever",
    [(0, 11, 'DRUG')]),
	("Paracetamol should me used",
    [(0, 11, 'DRUG')]),
	("I will use Paracetamol",
    [(11, 22, 'DRUG')]),
	("What is Paracetamol",
    [(8, 19, 'DRUG')]),
]
    nlp.entity.add_label('DRUG')
    train_ner(nlp, train_data, output_directory)

    doc = nlp('Do you like horses?')
    print("Ents in 'Do you like horses?':")
    for ent in doc.ents:
        print(ent.label_, ent.text)
    if output_directory:
        print("Loading from", output_directory)
        nlp2 = spacy.load('en', path=output_directory)
        nlp2.entity.add_label('DRUG')
        doc2 = nlp2('Do you like horses?')
        for ent in doc2.ents:
            print(ent.label_, ent.text)


if __name__ == '__main__':
    import plac
    plac.call(main)