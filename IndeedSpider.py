import sys
from __future__ import print_function
import pickle

from mechanize import ParseResponse, urlopen, urljoin
import mechanize
from bs4 import BeautifulSoup

import json
from pprint import pprint
import string
import urllib2
import urllib
import socket
from readability.readability import Document

import os
import errno
import re
from  collections import Counter
import nltk
from collections import defaultdict

domain = "http://www.indeed.com"
projDir = "/Users/zhiyuan/Documents/Projects/PySpider/Indeed/HTML"

# Create a Folder
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def IndeedCrawling(Keyword,Poz,maxPage = 1000):
	folderDir = projDir + "/" + Keyword + "/" + Poz
	make_sure_path_exists(folderDir)
	searchHTML = domain + "/jobs?" + "q=" + string.replace(Keyword," ","+") + "&l=" + Poz
	response =urllib2.urlopen(searchHTML)
	soup = BeautifulSoup(response,'html')
	f = open( folderDir + "/Index.html",'w')
	print(soup,file = f)
	f.close
	# Define total count of pages
	soup.find("div",id = "searchCount")
	searchCount = soup.find("div",id = "searchCount").text
	totalCount = int(string.replace(string.split(searchCount)[-1],",",""))
	# Loop for pages
	startPage = 10
	jobDict = dict()
	searchPage = min(totalCount,maxPage)
	while (startPage <= searchPage):
		pageDir = folderDir + "/" + str(startPage/10)
		make_sure_path_exists(pageDir)
		# Go to next page
		soupPage = simOpenURL(searchHTML + "&start=" + str(startPage))
		# Extract info of jobs on current page
		print("---------------" + "Page:" + str(startPage) + "---------------")
		jobDict.update(downloadJobLink(soupPage,startPage,folderDir = folderDir))
		startPage += 10
	return(jobDict)
		



def downloadJobLink(soup,pNum,folderDir):
	jobDictOnPage = dict()
	for div in soup.find_all("div", "row result"):
		h = div.h2
		if h != None:
			try:
				print(str(h["id"]))
				print(domain + h.a["href"])
				# f2 = open( folderDir + "/" + str(pNum/10) + "/" + h["id"] + ".html",'w')
				# reqJob = urllib2.Request(domain + h.a["href"])
				# reqJob.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')  
				# opener = urllib2.build_opener()  
				# resJob= opener.open(reqJob)  
				# soupJob = BeautifulSoup(resJob,'html')
				# print(BeautifulSoup(reqJob,'html'),file = f2)
				# f2.close
				# print(h["id"] + str(type(h["id"])))
				jobDictOnPage[h["id"]] = parseJobLink(domain + h.a["href"])
				jobDictOnPage[h["id"]].update({"Link": domain + h.a["href"]})
			except urllib2.HTTPError:
				print('There was an error with the request')
			except urllib2.URLError:
				print('There was an error with the request')
			except socket.timeout:
				print('There was an error with the request')
	return(jobDictOnPage)


def parseJobLink(URL):
	req = simOpenURL(URL,type = "request")
	html = req.read()
	readable_article = Document(html).summary().lower()
	textSplit = re.split(r'\W', readable_article)
	yearExist = ["year" in s for s in textSplit]
	if(sum(yearExist) != 0):
		yearInd = [i for i in range(len(textSplit)) if "year" in textSplit[i]]
		yearRange = list()
		for ind in yearInd:
			yearRange.extend(range(ind-5,ind + 3))
		yearStr = [textSplit[i] for i in yearRange]
		try:
			yearReq = re.findall(r'\d+',' '.join(yearStr))
			yearReq = min(map(int,yearReq))
		except ValueError:
			yearReq = 0
	else:
		yearReq = 0
	tok = nltk.word_tokenize(readable_article.encode('utf-8').decode("utf8"))
	wordsTag = dict(nltk.pos_tag(tok))
	wordsCount = dict(Counter(re.split(r'\W', readable_article)).most_common())
	wordDict = defaultdict(list,wordsCount)
	for key,value in wordsCount.items():
		if key in wordsTag:
			try:
				wordDict[key] = [wordsTag[key],value]
			except KeyError:
				 err = 1
		else:
			del wordDict[key]
	jobInfo = {"reqYear" : yearReq,"wordDict" : wordDict}
	return(jobInfo)



def simOpenURL(URL,type = "soup"):
	req = urllib2.Request(URL)
	req.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')  
	opener = urllib2.build_opener()  
	out = opener.open(req,timeout=10)  
	#out = BeautifulSoup(out,'html')
	if type == "soup":
		out = BeautifulSoup(out,'html')
	return(out)




searchResult = IndeedCrawling("SAS","CA",maxPage = 50)

dataFile = "/Users/zhiyuan/Documents/Projects/PySpider/Indeed/Data/Jobs_SAS.json"
pickle.dump( searchResult, open(dataFile, "wb" ))



for key,value in searchResult.items():
	print(value["reqYear"])
	print(value["Link"])

URL = "http://careers.deloitte.com/jobs/eng-US/details/j/E15NATCACSKL488-SO/visual-journalist-vizstudio?src=JB-16801"
req = urllib2.Request(URL)
req.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')  
opener = urllib2.build_opener()  
out = opener.open(req,timeout=10)  
#out = BeautifulSoup(out,'html')
if type == "soup":
	out = BeautifulSoup(out,'html')

try:
	simOpenURL("http://www.indeed.com/rc/clk?jk=773782f5576e3ef3")
except urllib2.HTTPError:
	print('There was an error with the request')
except urllib2.URLError:
	print('There was an error with the request')

