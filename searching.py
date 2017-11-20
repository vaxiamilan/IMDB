import bs4 as bs
import urllib.request

class IMDB:
	
	def __init__(self):
		self.title = input("Enter a movie or a TV show name  : ")
		self.title = "http://www.imdb.com/find?ref_=nv_sr_fn&q=" + self.title.replace(' ','+') + "&s=all"

	def searching_result(self):
		sourc = urllib.request.urlopen(self.title).read()
		source = bs.BeautifulSoup(sourc,'lxml')
		table = source.find('table')
		table_rows = table.find_all('tr')
		self.result=[]
		j=1
		k=1
		for tr in table_rows:
			td = tr.find_all('td')
			for i in td:
				if k%2==1:
					k=0
				else:
					print(str(j) +"."+ i.text)
					j = j + 1
					k=1
					self.result.append(i.a['href'])

	def information(self):
		select = int(input("Please select which one you are searching for, mention the number :"))
		newsourc = urllib.request.urlopen("http://www.imdb.com" + self.result[select-1]).read()
		self.newsource = bs.BeautifulSoup(newsourc,'lxml')

	def output(self):
		if((self.newsource.find("meta", {"property":"og:type"})['content'])=="video.movie"):
			print("It's a movie")
			print("  ")
			print(self.newsource.find("meta", {"name":"title"})['content'])
			print("  ")
			print("Description  :")
			print(self.newsource.find("meta", {"name":"description"})['content'])
			print("  ")
			print("  ")
			print("Rating  ::  " + self.newsource.select_one("span[itemprop=ratingValue]").text)
			print("  ")

		elif((self.newsource.find("meta", {"property":"og:type"})['content'])=="video.tv_show"):
			print("It's a TV Show")
			print("  ")
			print(self.newsource.find("meta", {"name":"title"})['content'])
			print("  ")
			print("Description  :")
			print(self.newsource.find("meta", {"name":"description"})['content'])
			print("  ")
			print("  ")
			print("Rating  ::  " + self.newsource.select_one("span[itemprop=ratingValue]").text)
			print("  ")
			print("Episodes...")
			for div in self.newsource.findAll('div', attrs={'class':'seasons-and-year-nav'}):
				print(div.text)


i=IMDB()
i.searching_result()
i.information()
i.output()
