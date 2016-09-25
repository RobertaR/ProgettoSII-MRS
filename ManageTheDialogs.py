#### PROGETTO SII - MOVIE RECOMMENDER SYSTEM

#### ROBERTA ROMANO

from PyQt4 import QtCore, QtGui
from ClassUsers_Items import *
from sklearn.cluster import KMeans

import secondDialog
import finalDialog

import sys
import numpy as np
import pickle
import random
import operator

import time

user = []
item = []
movies_one_genre = []
movies_more_genres = []
current_user = []

d = Dataset()
d.load_users("data/u.user", user)
d.load_items("data/u.item", item)
d.load_items("data/first_check_movies.item", movies_one_genre)
d.load_items("data/movies_with_more_genres.item", movies_more_genres)

n_users = len(user)
n_items = len(item)

utility_matrix = pickle.load( open("utility_matrix.pkl", "rb") )

# Find the average rating for each user and stores it in the user's object
for i in range(0, n_users):
    x = utility_matrix[i]
    user[i].avg_r = sum(a for a in x if a > 0) / sum(a > 0 for a in x)

# Find the Pearson Correlation Similarity Measure between two users
def p_corr_simil(x, y, ut):
    num = 0
    den1 = 0
    den2 = 0
    A = ut[x - 1]
    B = ut[y - 1]
    num = sum((a - user[x - 1].avg_r) * (b - user[y - 1].avg_r) for a, b in zip(A, B) if a > 0 and b > 0)
    den1 = sum((a - user[x - 1].avg_r) ** 2 for a in A if a > 0)
    den2 = sum((b - user[y - 1].avg_r) ** 2 for b in B if b > 0)
    den = (den1 ** 0.5) * (den2 ** 0.5)
    if den == 0:
        return 0
    else:
        return num / den

# Perform clustering on items

movie_genre = []

for movie in item:
    movie_genre.append([movie.unknown, movie.action, movie.adventure, movie.animation, movie.childrens, movie.comedy,
                        movie.crime, movie.documentary, movie.drama, movie.fantasy, movie.film_noir, movie.horror,
                        movie.musical, movie.mystery, movie.romance, movie.sci_fi, movie.thriller, movie.war, movie.western])

movie_genre = np.array(movie_genre)
cluster = KMeans(n_clusters=19)
cluster.fit_predict(movie_genre)

############### MOVIE - NEW USER #################
rating_map = {}

def random_search():
    result_genres = []
    result_movies = []
    rand_ask = random.sample(movies_one_genre, 200)   
    i = 0
    while len(result_movies)<10:
        if len(rand_ask[i].getGenres()) > 0:
            str_genre = rand_ask[i].getGenres()[0]
            if str_genre not in result_genres:
                result_genres.append(str_genre)
                result_movies.append(rand_ask[i])
        i += 1

    rating_map = {result_genres[0] : 0, result_genres[1] : 0, result_genres[2] : 0, result_genres[3] : 0, result_genres[4] : 0, result_genres[5] : 0,result_genres[6] : 0, result_genres[7] : 0, result_genres[8] : 0, result_genres[9] : 0}

    return result_movies

ask = random_search()

new_user = np.zeros(19)

final_list_of_movies = []

def addValues(movie, a):
    #save rating with genre
    rating_map[movie.getGenres()[0]] = a 
    removeMovie(movie)

    d.load_current_user("data/us.user", current_user)

    if new_user[cluster.labels_[movie.id - 1]] != 0:
        new_user[cluster.labels_[movie.id - 1]] = (new_user[cluster.labels_[movie.id - 1]] + a) / 2
    else:
        new_user[cluster.labels_[movie.id - 1]] = a

    utility_new = np.vstack((utility_matrix, new_user))

    length = len(current_user) - 1
    user.append(User(len(user), current_user[length].age, current_user[length].sex , current_user[length].occupation, 110018))

    p_corr_simil_matrix = np.zeros(n_users)

    if len(ask) > 0:
        load_a_newDialog()
    else:
        ################## END ###################
        #print "Finding users which have similar preferences."
        for i in range(0, n_users + 1):
            if i != 943:
                p_corr_simil_matrix[i] = p_corr_simil(944, i + 1, utility_new)

        user_index = []
        for i in user:
            user_index.append(i.id - 1)
        user_index = user_index[:943]
        user_index = np.array(user_index)

        top_5 = [x for (y,x) in sorted(zip(p_corr_simil_matrix, user_index), key=lambda pair: pair[0], reverse=True)]
        top_5 = top_5[:5]

        top_5_genre = []
        for i in range(0, 5):
            maxi = 0
            maxe = 0
            for j in range(1, 19):
                if maxe < utility_matrix[top_5[i]][j]:
                    maxe = utility_matrix[top_5[i]][j]
                    maxi = j

            top_5_genre.append(maxi)

        ###COSTRUISCO MAPPA###
        genres = {1:"action", 2:"adventure",3:"animation",4:"childrens",5:"comedy",6:"crime",7:"documentary",8:"drama",9:"fantasy",10:"film_noir",11:"horror",12:"musical",13:"mystery",14:"romance",15:"science fiction",16:"thriller",17:"war", 18:"western"}
        new_top = []
        alternative_array = []

        for t in top_5_genre:
            if genres.has_key(t):
                if genres[t] not in new_top:
                    new_top.append(genres[t])
                else:
                     alternative_array.append(genres[t])         

        count = 0 
        check_separate = False 
        array_to_see = []
        array_genres_updated = []
        bool_first_check = True
        new_top_support = []

        for nt in new_top:
            new_top_support.append(nt)

        while len(final_list_of_movies) < 5:
            #first step
            array_genres_updated = alternative_array #puo essere anche vuoto
            array_to_see = movies_more_genres

            if bool_first_check:
                array_genres_updated = new_top
                bool_first_check = False

                if len(new_top) == 1:
                    array_to_see = movies_one_genre

            elif len(new_top) == 5:
                element1 = random.choice(new_top)
                element2 = random.choice(new_top)
                while element1 == element2:
                    element2 = random.choice(new_top)

                array_genres_updated.append(element1)
                array_genres_updated.append(element2)

                if count == 10: #dopo 10 tentativi rinuncio
                    new_top = []


            elif len(new_top) == 4:
                #non ho trovato un film con tutti e 4 i generi
                #ora prendo 2 generi alla volta da aggiungere all'array
                #rimuovendo il genere duplicato dall'array
                if alternative_array[0] in new_top_support:
                    new_top_support.remove(alternative_array[0])

                if(count == 1):
                    array_genres_updated.append(new_top_support[0])
                    array_genres_updated.append(new_top_support[1])
                elif(count == 2):
                    array_genres_updated.append(new_top_support[1])
                    array_genres_updated.append(new_top_support[2])
                elif(count == 3):
                    array_genres_updated.append(new_top_support[0])
                    array_genres_updated.append(new_top_support[2])
                elif(count == 4): 
                #scelgo solo il duplicato 
                    array_to_see = movies_one_genre
                    new_top = []

            
            elif len(new_top) == 3:
                if len(alternative_array) > 0:
                    #### DIVERSI ma gia controllato solo i due diversif
                    if alternative_array[0] != alternative_array[1] and check_separate:
                        array_genres_updated = []
                        if count == 2:
                            array_genres_updated.append(alternative_array[0])
                        elif count == 3:
                            array_genres_updated.append(alternative_array[1])
                        elif count == 4:
                            if alternative_array[0] in new_top_support and alternative_array[1] in new_top_support:
                                new_top_support.remove(alternative_array[0])
                                new_top_support.remove(alternative_array[1])
                            array_genres_updated = new_top_support #prendo quello che rimane
                            new_top = []

                        array_to_see = movies_one_genre
                    #### UGUALI
                    elif alternative_array[0] == alternative_array[1]:
                        array_genres_updated.pop() #elimino l'ultimo elemento della lista
                        if alternative_array[0] in new_top_support:
                            new_top_support.remove(alternative_array[0])

                        if(count == 1):
                            array_genres_updated.append(new_top_support[1])
                        elif(count == 2):
                            array_genres_updated.append(new_top_support[2])
                            new_top = []
                    else: 
                        check_separate = True
                #mi serve per vedere un primo check con i due film in alternative_array insieme
                #se mi va nella ipotesi della scelta dei rating dell'utente 
                else:
                    array_genres_updated = []

                    if(count == 1):
                        array_genres_updated.append(new_top[0])
                        array_genres_updated.append(new_top[1])
                    elif(count == 2):
                        array_genres_updated.append(new_top[1])
                        array_genres_updated.append(new_top[2])
                    elif(count == 3):
                        array_genres_updated.append(new_top[0])
                        array_genres_updated.append(new_top[2])
                    elif(count == 4): 
                        array_genres_updated.append(new_top[0])
                        array_to_see = movies_one_genre
                    elif(count == 5):
                        array_genres_updated.append(new_top[1])
                        array_to_see = movies_one_genre
                    elif(count == 6):
                        array_genres_updated.append(new_top[2])
                        array_to_see = movies_one_genre
                        new_top = []
                                  

            elif len(new_top) == 2:
                array_genres_updated =[]
                #caso 1: 3 duplicati uguali
                #cerco i due generi separatamente
                if(count == 1):
                    array_genres_updated.append(new_top[0])
                elif(count == 2):
                    array_genres_updated.append(new_top[1])
                    new_top = []

                #caso2: 2 di un genere e 1 diverso
                array_to_see = movies_one_genre

            ### CASO 1 GENERE
            elif len(new_top) == 1:
                #se sono qui vuol dire che non ho trovato 5 film diversi nel file "one_genre"
                #quindi li cerco in "more_genres"
                array_to_see = movies_more_genres
                new_top = []


            ### CASO estremo - non si sono trovati abbastanza film, prendo i generi piu votati dall'utente, in base alle proprie votazioni
            else:
                new_top = []
                count = 0
                alternative_array = []
                sorted_x = sorted(rating_map.items(), key=operator.itemgetter(1), reverse=True)
                count_new_top = 0
                while len(new_top) < 3: #prendo solo i primi 3
                    new_top.append(sorted_x[count_new_top][0])
                    count_new_top += 1

                array_genres_updated = new_top

            #### FINE SERIE IF-ELIF
            #INCREMENTO COUNT
            count += 1

            ##### INIZIO SCORRIMENTO FILM ##########################

            # print "array to see length: " + str(len(array_to_see))
            # print "array_genres_updated: " + str(array_genres_updated)[1:-1]
            # print "array_genres_updated length: " + str(len(array_genres_updated))

            for mov in array_to_see:
                bool_contains = True
                
                if len(final_list_of_movies) < 5:
                    #controllo tutti i generi
                    if len(array_genres_updated) > 1:
                        for gen in array_genres_updated:
                            if gen not in mov.getGenres():
                                bool_contains = False
                                break
                                
                    elif(mov.getGenres() != array_genres_updated): #se ha solo un genere
                         bool_contains = False

                    if bool_contains:
                        #controllo eventuale duplicato dei film votati o film nell'array finale
                        if mov not in ask and mov not in final_list_of_movies:
                            final_list_of_movies.append(mov)                

        load_finalWindow()

def getMovies():
    return ask

def getFinalListMovies():
    return final_list_of_movies

def load_a_newDialog():
    #secondDialog.openDescription()
    secondDialog.main()

def load_finalWindow():
    finalDialog.main()

def removeMovie(x):
    if len(ask) !=0:
        ask.remove(x)
