from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv
import time


cur_dir = 'C:/Users/amit/Desktop/ai_project'
out_file = open( cur_dir + '/datasets/reviews.csv', 'w', newline='', encoding="utf-8")
k = 1

head  = ['imdb_link', 'review', 'rating']
writer = csv.writer(out_file)
writer.writerow(head)

data_path = cur_dir + '/datasets/movies.csv'
movies_list = open(data_path).read().split('\n')

#ignore first row, as it has header only
for movie in movies_list[1:len(movies_list)-1]:
    reviews_link = movie.split(',')[1]
    
    print(reviews_link + "\n")
    
    u_client = uReq(reviews_link)
    html_file = u_client.read()
    u_client.close()

    bsoup = soup(html_file, "html.parser")
    #bsoup = bsoup.encode("utf-8")
    lst = bsoup.findAll("div", {"class": "lister-item-content"})

    for item in lst:

        title_tag = item.find("a", {"class": "title"})
        rating_tag = item.find("span", {"class": "rating-other-user-rating"})
        review_tag = item.find('div', {'class': 'text show-more__control'})
        if not rating_tag:
            continue

        imdb_link = reviews_link
        review_title = title_tag.text.strip()
        rating = rating_tag.findChildren('span')[0].text.strip()
        # review_text = review_tag.text.strip()
        
        # print("\n\nReview title: " + review_title
        #       + "\nReview text: " + review_text
        #       + "\nRating: " + rating)

        # currently not using review text
        # words = [imdb_id, review_title, review_text, rating]
        
        words = [imdb_link, review_title, rating]
        writer = csv.writer(out_file)
        writer.writerow(words)

    # waiting for few seconds, so that imdb does not 
    # recognise our system as bot and does not block our ip
    time.sleep(3)
    
        
out_file.close()
