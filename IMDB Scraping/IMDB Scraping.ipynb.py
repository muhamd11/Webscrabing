

from bs4 import BeautifulSoup
import requests





url = 'https://www.imdb.com/chart/top/'
client = requests.get(url)
html = client.text
soup = BeautifulSoup(html,'html.parser')

film_name = soup.find_all('td' ,{'class':'titleColumn'})
year = soup.find_all('span',{'class':'secondaryInfo'})
rating =  soup.find_all('td',{'class':'ratingColumn imdbRating'})





film_name[0].text.strip().split('\n')[1].strip().replace('(',"").replace(')',"")





film_names = []
film_year = []
film_rating = []

for i in range(len(film_name)):
    film_names.append(film_name[i].text.strip().split('\n')[1].strip())
for i in range(len(year)):
    film_year.append(film_name[i].text.strip().split('\n')[2].strip().replace('(',"").replace(')',""))
for i in range(len(rating)):
    film_rating.append(rating[i].text.strip())
    
    



import pandas as pd





df = pd.DataFrame({"film name":film_names , 'year':film_year , 'rating':film_rating})
print(df)

