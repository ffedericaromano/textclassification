from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class text_classification:

    stemmer = SnowballStemmer("italian")
    stop_words = set(stopwords.words('italian'))

    def __init__(self):
        self.words=[]

    def readFile(self, fileName):
        f = open(fileName, "r", encoding="utf-8")
        s = f.read()
        return s

    #lista con le parole del testo
    def tokenizeWords(self, string):
        return list(word_tokenize(string))

    def lower_cleanString(self, string):
        string=string.lower()
        d={",":"",".":"","?":"","!":"",":":"","'":"",'"':"",";":"","(":"",")":""}
        for lettera in string:
            if lettera.isnumeric():
                string=string.replace(lettera,"")
            if lettera in d:
                string=string.replace(lettera,d[lettera])

        return string

    def removeStopWords(self):
        filtered_words=[]
        for word in self.words:
            if word not in self.__class__.stop_words:
                filtered_words.append(word)
        self.words=filtered_words

    def stemWords(self):
        stemmed_words=[]
        for word in self.words:
            stemmed_words.append(self.__class__.stemmer.stem(word))
        self.words=stemmed_words

    def classificazione(self,diz):
        score={}
        for argomento in diz:
            score[argomento]=0
            for word in self.words:
                if word in diz[argomento]:
                    score[argomento]+=1/len(diz[argomento])
        max=0
        for argomento in score:
            if score[argomento]>max:
                max=score[argomento]
                argomento_max=argomento

        return argomento_max


#testi conosciuti: dizionario con argomenti e corrispondenti liste delle parole

testo_gossip=text_classification()
stringa=testo_gossip.readFile("gossip.txt")
stringa=testo_gossip.lower_cleanString(stringa)
testo_gossip.words=testo_gossip.tokenizeWords(stringa)
testo_gossip.removeStopWords()
testo_gossip.stemWords()
dizionario_argomenti={}
dizionario_argomenti["Gossip"]=testo_gossip.words

testo_sport=text_classification()
stringa=testo_sport.readFile("sport.txt")
stringa=testo_sport.lower_cleanString(stringa)
testo_sport.words=testo_sport.tokenizeWords(stringa)
testo_sport.removeStopWords()
testo_sport.stemWords()
dizionario_argomenti["Sport"]=testo_sport.words

testo_musica=text_classification()
stringa=testo_musica.readFile("musica.txt")
stringa=testo_musica.lower_cleanString(stringa)
testo_musica.words=testo_musica.tokenizeWords(stringa)
testo_musica.removeStopWords()
testo_musica.stemWords()
dizionario_argomenti["Musica"]=testo_musica.words

#testo incognito: cerca argomento

testo_incognito=text_classification()
stringa=testo_incognito.readFile("incognito.txt")
stringa=testo_incognito.lower_cleanString(stringa)
testo_incognito.words=testo_incognito.tokenizeWords(stringa)
testo_incognito.removeStopWords()
testo_incognito.stemWords()
print(f'Il testo incognito parla di {testo_incognito.classificazione(dizionario_argomenti)}')


