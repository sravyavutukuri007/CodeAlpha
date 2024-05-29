#importing the required packages
import pandas as pd


#Reading the dataset file from the local system
tracks=pd.read_csv("C:\\Users\\adila\\Downloads\\spotify_tracks.csv")


# Taking the input of favorite songs from the user
ids = input('Enter comma-separated ids of your favorite songs\n> ').strip().split(',')


# search the specified ids in this dataset and get the tracks
favorites = tracks[tracks.track_id.isin(ids)]


# code to sort find out the maximum occuring cluster number according to user's favorite track types
cluster_numbers = list(favorites['track_genre'])
clusters = {}
for num in cluster_numbers:
  clusters[num] = cluster_numbers.count(num)


# sort the cluster numbers and find out the number which occurs the most
user_favorite_cluster = [(k, v) for k, v in sorted(clusters.items(), key=lambda item: item[1])][0][0]


#Giving the user's favorite music genre based on the above analysis 
print('\nFavorite cluster:', user_favorite_cluster, '\n')


# finally get the tracks of that cluster
suggestions = tracks[tracks.track_genre == user_favorite_cluster]


# now print the first 5 rows of the data frame having that cluster number as their music Genre
#Now showing the suggestions according to the user's favorite music genre
print(suggestions.head())
