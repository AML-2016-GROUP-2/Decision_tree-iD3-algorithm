import csv
import re
import sys
from nltk.tokenize import TweetTokenizer

tweets = []
newtweets = []
category = []

def clean_data():
	i=0;
	q = re.compile(r'\bRT\b')
	r = re.compile(r'\bhttps\b')
	with open('dataset_v1.csv') as f:
		reader = csv.reader(f)
		tokenizer = TweetTokenizer()
		for row in reader:
			tweets.append(row[0])
			category.append(row[1])
			i+=1

		for row in tweets:
			rownew = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",row).split())
			rownewer = ' '.join(re.sub(q," ",rownew).split())
			rownewer1 = ' '.join(re.sub(r," ",rownewer).split())
			newtweets.append(rownewer1)

			#data saved to clean_data.csv 
	with open('clean_data.csv', 'w') as fp:
		a = csv.writer(fp, delimiter=',')
		data = zip(newtweets,category)
		a.writerows(data)
		print data

def get_trainfile():
	if len(sys.argv) <3 :
		print "please enter the training file "
		training_filename  = sys.stdin.readline().strip()
	else :
		training_filename  = sys.argv[1]

	try :
		traintweet = open(training_filename,"r")
	except IOError:
		print "Error: could not find the training file specified" %training_filename
		sys.exit(0)

		return traintweet

def get_testfile():
	if len(sys.argv) < 3:
		print "please enter a test file"
		test_filename = sys.stdin.readline().strip()
	else:
		test_filename = sys.argv[2]

	try:
		testtweet = open(test_filename,"r")
	except IOError:
		 print "Error: could not find the test file specified" %test_filename
		 sys.exit(0)
	return testtweet

#while extracting the data from dataset_v2 we need to tokenize it (use tokenizer = TweetTokenizer()) 
clean_data()
