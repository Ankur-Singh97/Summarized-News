import pickle
urls = []
from newspaper import Article
import newspaper
paper = newspaper.build('https://edition.cnn.com')
for article in paper.articles:
    urls.append(article.url)

if urls == []:
    with open('y.txt', 'rb') as fp:
        urls = pickle.load(fp)

else:
    with open('y.txt', 'wb') as fp:
        pickle.dump(urls, fp)

for url in urls:
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    print(article.title + "\n\n" + article.summary + "\n\n\n")
    
