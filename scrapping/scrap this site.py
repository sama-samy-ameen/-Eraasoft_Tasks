import requests
url="https://www.scrapethissite.com/pages/simple/"
type(url)
requests.get(url)
website=requests.get(url).text
print(website)
type(website)
  #we need to convert it into an html file , using beautiful soup
from bs4 import BeautifulSoup
myWebsite=BeautifulSoup(website,"html") 
type(myWebsite)
myWebsite.body

country1=myWebsite.find("div", class_="col-md-4 country")
print(country1)
name=country1.find("h3",class_="country-name").text
print(name)
population1=country1.find("span",class_="country-population").text
print(population1)
capital1=country1.find("span",class_="country-capital").text
print(capital1)
#class must be written this way class_ because class s is a reserved keyword in python 
area1=country1.find("span",class_="country-area").text
print(area1)
#since that they all have the same format,....,use find_all
countries=myWebsite.find_all("div", class_="col-md-4 country")
print(len(countries))
for country in countries:
    name=country.find("h3",class_="country-name").text
    population=country.find("span",class_="country-population").text
    capital=country.find("span",class_="country-capital").text
    area=country.find("span",class_="country-area").text
    print(name,'\n','population:',population,'\n','capital:',capital,'\n','area:',area)

    #this is for just one page of the website, but we can also scrap all the pages of the website loop for i in range the pages , the url is written with format url=f"https...{i}".... because the link is the same , but each page differs in i 
    
