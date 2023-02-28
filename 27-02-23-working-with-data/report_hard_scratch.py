import movie_data

# Actor appearring in most movies
# Actor with best average rating
# Least popular genre in the 1980's

def main():
    count = 0
    most = ''
    freq_dict={}
    rating_dict={}
    movie_library = movie_data.movies
    freq_dict = movies_actor_dict(movie_library, freq_dict)
    count, most = the_most_movies_actor(freq_dict, count, most)
    print(f'\nThe actor appearing in most movies with {count} appearances is {most}\n')

    combined_rating_dict(movie_library, rating_dict)
    average_rating_dict(count, rating_dict, freq_dict)


def movies_actor_dict(movie_library, freq_dict):
    for movie in movie_library:
        for name in movie.get('actors'):
            if name in freq_dict:
                freq_dict[name] += 1
            else:
                freq_dict[name] = 1
    return freq_dict

def the_most_movies_actor(freq_dict, count, most):
    for key, value in freq_dict.items():
        if value > count:
            count = value
            most = key
    return count, most




def combined_rating_dict(movie_library, rating_dict):
    for movie in movie_library:
        for name in movie.get('actors'):
            if name in rating_dict:
                rating_dict[name] += movie.get('rating')
            else:
                rating_dict[name] = movie.get('rating')       
    return rating_dict

def average_rating_dict(count, rating_dict, freq_dict):
    pass




 

            


        









if __name__ == '__main__':
    main()

