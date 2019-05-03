from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv


'''
############################################################

# online

movies_2018_link = 'https://www.imdb.com/list/ls058813655/'

movies_2017_link = ' '

movies_2016_link = ' '


u_client = uReq(movies_2018_link)
html_file = u_client.read()
u_client.close()

bsoup = soup(html_file, "html.parser")
lst = bsoup.findAll("h3", {"class": "lister-item-header"})


cur_dir = 'C:/Users/amit/Desktop/ai_project'
out_file = open( cur_dir + '/datasets/movies.csv', 'w', newline='')
k = 1

#write index
words  = ['title', 'reviews_link']
writer = csv.writer(out_file)
writer.writerow(words)

for item in lst:

    title_tag = item.find("a", href = True)
    title = title_tag.text.strip()
    link = 'https://www.imdb.com' + title_tag['href'].split('?')[0] + 'reviews?ref_=tt_urv'
    if not title or not link:
        continue
    
    words  = [title, link]
    writer = csv.writer(out_file)
    writer.writerow(words)
    print("\n\nTitle: " + title + "\nLink: " + link)

out_file.close()

############################################################


'''
############################################################

# offline 

html_file = 'C:/Users/amit/Desktop/ai_project/html_pages/movies_page.html'
bsoup = soup(open(html_file), "html.parser")
lst = bsoup.findAll("h3", {"class": "lister-item-header"})


cur_dir = 'C:/Users/amit/Desktop/ai_project'
out_file = open( cur_dir + '/datasets/movies.csv', 'w', newline='')
k = 1

#write index
words  = ['title', 'reviews_link']
writer = csv.writer(out_file)
writer.writerow(words)

for item in lst:

    title_tag = item.find("a", href = True)
    title = title_tag.text.strip()
    link = title_tag['href'].split('?')[0] + 'reviews?ref_=tt_urv'
    if not title or not link:
        continue
    
    words  = [title, link]
    writer = csv.writer(out_file)
    writer.writerow(words)
    print("\n\nTitle: " + title + "\nLink: " + link)

out_file.close()

#############################################################




