# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 16:47:42 2020

@author: hina
"""

print ()

import math
from operator import itemgetter

# definie class similarity
class similarity:
    
    # Class instantiation 
    def __init__ (self, ratingP, ratingQ):
        self.ratings1 = ratingP
        self.ratings2 = ratingQ

    # Minkowski Distance between two vectors
    def minkowski(self, r):
    
        # calcualte minkowski distance
        distance = 0       
        for k in (set(self.ratings1.keys()) & set(self.ratings2.keys())):
            p = self.ratings1[k]
            q = self.ratings2[k]
            distance += pow(abs(p - q), r)
    
        # return value of minkowski distance
        return pow(distance,1/r)

    # Pearson Correlation between two vectors
    def pearson(self):
        
        # Step 1.1
        # set n to the number of common keys
        # do not hardcode! 
        # this should work no matter which 2 dictionares I provide
        set_userX = set(self.ratings1.keys()) 
        set_userY = set(self.ratings2.keys())
        set_combined = set_userX & set_userY
        n = len(set_combined)
        
        # Step 1.2
        # error check for n==0 condition, and
        # return -2 if n==0
        if(n ==0):
            return -2
        
         
        # Step 1.3
        # use a SINGLE for loop to calculate the partial sums
        # in the computationally efficient form of the pearson correlation   
        sumpq = 0
        sump = 0
        sumq = 0
        sump2 = 0
        sumq2 = 0
        for i in set_combined:
            sumpq = sumpq + self.ratings1[i] * self.ratings2[i]
            sump = sump + self.ratings1[i]
            sumq = sumq + self.ratings2[i]
            sump2 = sump2 + pow(self.ratings1[i],2)
            sumq2 = sumq2 + pow(self.ratings2[i],2)
            
          
        # Step 1.4
        # calcualte the numerator term for pearson correlation
        # using relevant partial sums
        num = sumpq - ((sump * sumq)/n)
        
        # Step 1.5
        # calcualte the denominator term for pearson correlation
        # using relevant partial sums
        den = math.sqrt(sump2 - pow(sump,2)/n) * math.sqrt(sumq2 - pow(sumq,2)/n)
        
        # Step 1.6
        # error check for denominator==0 condition
        # return -2 if denominator==0
        if den ==0:
            return -2

        # Step 1.7
        # calcualte the pearson correlation 
        # using the numerator and deonomminator
        # and return the pearson correlation
        pc = round(num/den,2)
        return (pc)
        
    def pearson_knn(self, pc):
        pc_new = round((pc + 1)/2,2)
        return pc_new
            

# user ratings - this is the same data as we used in the User Recommendation Lecture
songData = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

# for whom are we making recommendations?
userX = input("Input name of User you want recommendation? - {Angelica,Bill,Chan,Dan,Hailey,Jordyn,Sam,Veronica}")
print()
userXRatings = songData[userX]


# Step 2.1
# find the similarity measure (pearson correlation) between userX's ratings, and each of the other user's ratings.
# DO NOT include userX's similarity measure from userX.
# use a for loop to get at the other users and their ratings - DO NOT hard code.
# use the similarity class to caclulate the simialrity measure (pearson correlation) between user ratings.
# assign list of (user, similarityMeasure) tuples to a variable called userSimilarities.
# Example of how userSimilarities might look: [('Angelica', 0.42), ('Bill', 0.0), ('Chan', 0.5), ('Dan', 0.39), ('Jordyn', 0.61), ('Sam', -2), ('Veronica', -2)]
userSimilarities = []
for userY in songData.keys():
    if (userY != userX):
        userYRatings = songData[userY]
        userXY= similarity(userXRatings, userYRatings)
        userXY_simscore_old = userXY.pearson()
        userXY_simscore = userXY.pearson_knn(userXY_simscore_old)
        userSimilarities.append([userY,userXY_simscore])

print("User similarity scores with ",userX, "\n", userSimilarities)
print()


# Step 2.2
# sort the list of tuples by highest simialrity to lowest similarity.
# assign the sorted list to a variable called sortedUserSimilarities.
# Example of how sortedUserSimilarities might look: [('Jordyn', 0.61), ('Chan', 0.5), ('Angelica', 0.42), ('Dan', 0.39), ('Bill', 0.0), ('Sam', -2), ('Veronica', -2)]
userSimilarities.sort( key = itemgetter(1), reverse = True)
sortedUserSimilarities  = userSimilarities
print("Sorted User similarity scores with ",userX, "\n",sortedUserSimilarities)
print()


#Get new weights for n nearest neighbours using knn function
n = 3
sum_n_similarities = 0
set_movies_n_neighbor = set()
for user in range(n):
    sum_n_similarities = sum_n_similarities + sortedUserSimilarities[user][1]
for user in range(n):
    print("Nearest neighbour",user, sortedUserSimilarities[user][0])
    sortedUserSimilarities[user][1] = round(sortedUserSimilarities[user][1]/sum_n_similarities,2)
    set_1 = (set(songData[sortedUserSimilarities[user][0]].keys()))
    set_movies_n_neighbor = set_movies_n_neighbor | set_1 
    
print()  
print("Updated weightes for" ,n, "similarity scores with ",userX, "\n",sortedUserSimilarities)
print()
print("Set of movies rated by ",n, "nearest neighbours", set_movies_n_neighbor)
print()

#find items not rated by userx which can be recommeneded and find predicted rating using nearest neighbours
set_movies_userx = set(songData[userX].keys())
set_movies_recom = set_movies_n_neighbor - set_movies_userx

# calculate predicted ratings for recommended movies for userx using weighted average
userXRecos = []
for movie in set_movies_recom:
    
    rating = 0
    
    for user in range(n):
        
        if (movie in songData[sortedUserSimilarities[user][0]].keys()):
            
            rating += songData[sortedUserSimilarities[user][0]][movie] * sortedUserSimilarities[user][1] 
            
    userXRecos.append((movie,round(rating,2)))
    
print("Songs recommendation list based on similar user\n",userXRecos)
print()


# Step 2.5
# sort list of tuples by highest rating to lowest rating.
# assign sorted list to a varaible userXSortedRecos.
# Example of how userXSortedRecos might look: [('Phoenix', 5.0), ('Slightly Stoopid', 4.5)]
userXRecos.sort( key = itemgetter(1), reverse = True)
userXSortedRecos  = userXRecos
print("Sorted recommendation list based on similar user\n",userXSortedRecos)
print()



print ("Final Recommendations for", userX)
print ("----------------------------------")
print ()
print (userXSortedRecos)
