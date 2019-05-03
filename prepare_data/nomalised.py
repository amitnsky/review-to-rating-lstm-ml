
import csv


cur_dir = 'C:/Users/amit/Desktop/ai_project'

dataset = train_file = open(cur_dir + '/datasets/reviews.csv', 'r', newline='', encoding="utf-8")
train_file = open(cur_dir + '/datasets/train.csv', 'w', newline='', encoding="utf-8")
test_file = open(cur_dir + '/datasets/test.csv', 'w', newline='', encoding="utf-8")

#write index
words  = ['review', 'rating']
writer = csv.writer(train_file)
writer.writerow(words)

writer = csv.writer(test_file)
writer.writerow(words)


reviews = dataset.read().split("\n")

print("Train dataset\n")
k = 1
  
for line in reviews[1:(len(reviews)*9//10)-1]:
    words = line.split(',')
    review = ",".join(words[1:len(words)-1])
    rating = words[len(words)-1]
    words  = [review, rating]
    writer = csv.writer(train_file)
    writer.writerow(words)
    if k<10:
        print("\n\nReview: " + review + "\nRating: " + rating)
    k=k+1

print("Test dataset\n")
k=1
      
for line in reviews[(len(reviews)*9//10): len(reviews)-1]:
    words = line.split(',')
    review = ",".join(words[1:len(words)-1])
    rating = words[len(words)-1]
    words  = [review, rating]
    writer = csv.writer(test_file)
    writer.writerow(words)
    if k<10:
        print("\n\nReview: " + review + "\nRating: " + rating)
    k=k+1
        

test_file.close()
train_file.close()
dataset.close()

