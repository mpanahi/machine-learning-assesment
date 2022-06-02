from nltk.util import ngrams
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import os


st = StanfordNERTagger(os.pardir+'/src/english.all.3class.distsim.crf.ser.gz',
                       os.pardir+'/src/'stanford-ner.jar',
                       encoding='utf-8')


class Event:

    def __init__(self, name):
        lines = []

        with open(os.pardir+'/data/artists.txt') as f:
            lines = f.readlines()

        artists = []
        for line in lines:
            if line.find("\n") != -1:
                artists.append(line.replace("\n", "").lower())

        self.artists = set(artists)
        self.event_name = name

    def get_lineup(self):
        line_up = {}
        if self.event_name.lower() in self.artists:

            line_up[self.event_name] = 100


        else:

            text = self.event_name
            tokenized_text = word_tokenize(text)
            sequenceTagging = []
            for i in range(len(tokenized_text)):
                sequenceTagging.append("O")
            to_be_tokenized = len(tokenized_text) - 1

            while (to_be_tokenized >= 1):
                ng = list(ngrams(tokenized_text, to_be_tokenized))

                for n in ng:
                    index = tokenized_text.index(n[0])

                    allOut = True
                    for i in range(index, index + len(n)):
                        if sequenceTagging[i] != "O":
                            allOut = False
                            break
                    if allOut == True:
                        name = ""
                        for i in range(0, len(n)):
                            name = name + n[i] + " "
                        name = name.strip()
                        if name.lower() in self.artists:
                            line_up[name] = 100
                            index = tokenized_text.index(n[0])
                            for i in range(index, index + len(n)):
                                sequenceTagging[i] = "lineup"

                to_be_tokenized = to_be_tokenized - 1
            # post-processing

            delim = [",", "and", "with", "&", "+", "vs"]
            text_splitted = word_tokenize(text)
            indices = []
            for i in range(len(text_splitted)):
                if text_splitted[i].lower() in delim:
                    indices.append(i)
            text_splitted_new = []
            if len(indices) > 0:

                name = ""
                for j in range(len(text_splitted)):
                    if j not in indices:
                        name = name + text_splitted[j] + " "
                        if j == len(text_splitted) - 1:
                            name = name.strip()
                            text_splitted_new.append(name)

                    else:
                        if name != "":
                            name = name.strip()
                            text_splitted_new.append(name)
                            name = ""
                        else:
                            continue

            text_splitted = text_splitted_new

            keys = ["-", "/", "at", ".", ":", "live", "in", "|", "//"]
            if len(text_splitted) > 1:
                for t in text_splitted:
                    tokenized_text = word_tokenize(t)
                    for k in range(0, len(tokenized_text)):
                        if tokenized_text[k] in keys:
                            for j in range(k, len(tokenized_text)):
                                tokenized_text[j] = ""
                            break
                    name = ""
                    for k in tokenized_text:
                        name = name + k + " "
                    if name != "":
                        higher_confidence = False
                        name = name.strip()
                        if name in text_splitted:
                            index = text_splitted.index(name)
                            if (index - 1) >= 0 and (index + 1) < len(text_splitted):
                                if text_splitted[index - 1] in line_up or text_splitted[index + 1] in line_up:
                                    higher_confidence = True
                            else:
                                if (index - 1) >= 0:
                                    if text_splitted[index - 1] in line_up:
                                        higher_confidence = True
                                if (index + 1) < len(text_splitted):
                                    if text_splitted[index + 1] in line_up:
                                        higher_confidence = True

                        for l in line_up:
                            if len(word_tokenize(l)) == 1 and l in word_tokenize(name):
                                line_up[name] = line_up.pop(l)

                        # if name not in line_up:
                        already_in = False
                        for l in line_up:
                            if name in word_tokenize(l):
                                already_in = True
                        if name in line_up:
                            already_in = True
                        if already_in == False:
                            if higher_confidence == True:
                                line_up[name] = 80
                            else:
                                line_up[name] = 60

        if len(line_up) == 0:
            classified_text = st.tag(word_tokenize(text))

            Found_name = False

            for c in classified_text:

                if c[1] == "PERSON":
                    if Found_name == False:
                        name = c[0]
                        Found_name = True
                    else:
                        name = name + " " + c[0]
                        line_up[name] = 80
                        name = ""

        return (line_up)

















