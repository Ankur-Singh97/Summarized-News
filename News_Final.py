import pickle
urls = []
from newspaper import Article
import newspaper

try:
	
	paper = newspaper.build('https://www.engadget.com/')
	for article in paper.articles:
		urls.append(article.url)

	if len(urls) <= 4:
		with open('/home/ankur/Desktop/y.txt', 'rb') as fp:
			urls = pickle.load(fp)

	else:
	    with open('/home/ankur/Desktop/y.txt', 'wb') as fp:
	        pickle.dump(urls, fp)

	class color:
	   PURPLE = '\033[95m'
	   CYAN = '\033[96m'
	   DARKCYAN = '\033[36m'
	   BLUE = '\033[94m'
	   GREEN = '\033[92m'
	   YELLOW = '\033[93m'
	   RED = '\033[91m'
	   BOLD = '\033[1m'
	   UNDERLINE = '\033[4m'
	   END = '\033[0m'

	if len(urls) > 20:
		x = 20
	else:
		x = len(urls)
	for i in range(x):
	    try:
	    	article = Article(urls[i])
	    	article.download()
	    	article.parse()
	    	article.nlp()
	    	print((color.BOLD + article.title + color.END) + "\n\n" + article.summary + "\n\n\n")
	    except:
	    	continue

except:
	pass