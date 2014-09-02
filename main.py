import urllib2
from BeautifulSoup import BeautifulSoup

def getRuntimeFromUrl(url):
	newSoup = BeautifulSoup(urllib2.urlopen(url).read())

	time = newSoup.find("time").string.strip().split()[0]

	return int(time)

soup = BeautifulSoup(urllib2.urlopen("http://www.imdb.com/chart/top").read())
titles = soup.findAll("td", "posterColumn")
urls = []
runningMins = 0
counter = 0

for title in titles:
	urls.append("http://www.imdb.com" + title.find("a")["href"])

for url in urls:
	runningMins += getRuntimeFromUrl(url)
	counter += 1
	print(str((counter / 250.0) * 100.0) + "%")

print(runningMins / 60.0)
