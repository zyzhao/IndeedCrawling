
url = "http://www.indeed.com/viewjob?jk=a011761bc5802863&q=Data+mining&tk=19hhjpu4e1a4h25g"
t = BeautifulSoup(urlopen(url).read(),'html')
nltk.clean_html(t)
t.get_text()


url = "http://www.indeed.com/viewjob?jk=a011761bc5802863&q=Data+mining&tk=19hhjpu4e1a4h25g"
html = urllib.urlopen(url).read()
readable_article = Document(html).summary()
readable_title = Document(html).short_title()
# f = open("/Users/zhiyuan/Documents/Projects/PySpider/Indeed/HTML/ttt.txt","w")
# print(readable_article.encode('utf-8'), file = f)
# f.close()

url = "http://www.indeed.com/viewjob?jk=a011761bc5802863&q=Data+mining&tk=19hhjpu4e1a4h25g"

Counter(re.split(r'\W', readable_article)).most_common()
tok = nltk.word_tokenize(readable_article.encode('utf-8').decode("utf8"))
nltk.pos_tag(tok)



sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),("dog", "NN"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(nltk.pos_tag(tok))
print(result)

result.draw()






from nltk.corpus import stopwords
sWords = stopwords.words('english')
s=set(sWords)

txt="a long string of text about him and her"
print(filter(lambda w: not w in s,readable_article.split()))

segWords = dict(Counter(re.split(r'\W', readable_article)).most_common())

tok = nltk.word_tokenize(re.split(r'\W', readable_article))
nltk.pos_tag(tok)

segWords["this"] = (1,2)

FreqDist(readable_article)



textSplit = re.split(r'\W', readable_article.lower())
yearInd = ["year" in s for s in textSplit].index(True)
yearStr = [textSplit[i] for i in range(yearInd-5,yearInd + 1)]
yearReq = re.findall(r'\d+',' '.join(yearStr))
yearReq = int(min(yearReq))

#========================================#

html = urllib.urlopen(url).read()
readable_article = Document(html).summary().lower()

textSplit = re.split(r'\W', readable_article)
yearInd = ["year" in s for s in textSplit].index(True)
yearStr = [textSplit[i] for i in range(yearInd-5,yearInd + 1)]
yearReq = re.findall(r'\d+',' '.join(yearStr))
yearReq = min(map(int,yearReq))

tok = nltk.word_tokenize(readable_article.encode('utf-8').decode("utf8"))
wordsTag = dict(nltk.pos_tag(tok))
wordsCount = dict(Counter(re.split(r'\W', readable_article)).most_common())

from collections import defaultdict
wordDict = defaultdict(list,wordsTag)

for key,value in wordsCount.items():
    wordDict[key] = [wordDict[key],value]
#========================================#

url = "http://www.indeed.com/rc/clk?jk=a2a8d03aa1021a1a"
html = urllib.urlopen(url).read()
readable_article = Document(html).summary().lower()

textSplit = re.split(r'\W', readable_article)
yearInd = [i for i in range(len(textSplit)) if "year" in textSplit[i]]
yearRange = list()
for ind in yearInd:
	yearRange.extend(range(ind-5,ind + 3))

yearStr = [textSplit[i] for i in yearRange]
yearReq = re.findall(r'\d+',' '.join(yearStr))
yearReq = int(min(yearReq))

tok = nltk.word_tokenize(readable_article.encode('utf-8').decode("utf8"))
wordsTag = dict(nltk.pos_tag(tok))
wordsCount = dict(Counter(re.split(r'\W', readable_article)).most_common())

from collections import defaultdict
wordDict = defaultdict(list,wordsCount)

for key,value in wordsCount.items():
	if key in wordsTag:
		try:
			wordDict[key] = [wordsTag[key],value]
		except KeyError:
			 err = 1
	else:
		del wordDict[key]
		# print("KeyError")
#========================================#

#========================================#
url = "https://hire.jobvite.com/CompanyJobs/Careers.aspx?k=Job&c=qGH9Vfwb&j=oOlv0fwo&s=Indeed"

textSplit = ["aa","year"]

tmp = pickle.load( open( dataFile, "rb" ) )

wordFreq = dict()
for i1,j1 in tmp.items():
	for i2,j2 in j1["wordDict"].items():
		try:
			if i2 in wordFreq:
				wordFreq[i2][2] += 1
				wordFreq[i2][1] = wordFreq[i2][1] + j2[1]
			else:
				wordFreq[i2] = j2
				wordFreq[i2].append(1)
		except KeyError:
			print("KeyError")

focusStr = "Oracle,SQL,Crystal, Designer, Spotfire, SSRS,R, JAVA,C,Python,Hadoop, Hive,Javascript, matlab, scipy,spss,sas,perl,shell,ruby,linux,unix,MS,VBA,Marketo,Tableau,CRM,Cognos,Octave,Weka,minitab,JMP,Spark,Map,Reduce,NoSQL,MongoDB,ETL"
focusWords = re.split(r',', focusStr.replace(" ","").lower())

for i,j in wordFreq.items():
	#if abs(j[1] - j[2]) <=1 : 
	if i in focusWords: 
		print(i + ": " + str(j[1]) + ","+ str(j[2]))

rYear = list()
for i,j in tmp.items():
	print(j["reqYear"])
	print(j["Link"])

# for i,j in wordFreq.items():
# 	#if abs(j[1] - j[2]) <=1 : 
# 	if j[2]>10 and j[2]<90 and "NN" in j[0]: 
# 		print(i + ": " + str(j[1]) + ","+ str(j[2]))





