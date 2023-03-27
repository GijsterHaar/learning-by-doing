import movie_data

def main():
    movie_library = movie_data.movies
    freq_dict = actor_in_movies_dict(movie_library)
    count, most = the_most_movies_actor(freq_dict)
    print(f'\nThe actor appearing in most movies with {count} appearances is {most}\n')
    rating_dict =get_total_rating_dict(movie_library)
    rating_dict = average_rating_dict(rating_dict, freq_dict)
    best_actors, best_score = get_best_rating_actors(rating_dict)
    best_actors = ', '.join(best_actors)
    print(f'The best actors are {best_actors} with an average rating of {best_score}\n')
    eighties = check_eighties_only(movie_library)
    not_in_eighties(movie_library, eighties)

def actor_in_movies_dict(movie_library):
    freq_dict={}
    for movie in movie_library:
        for name in movie.get('actors'):
            if name in freq_dict:
                freq_dict[name] += 1
            else:
                freq_dict[name] = 1
    return freq_dict

def the_most_movies_actor(freq_dict):
    count, most = 0, ''
    for key, value in freq_dict.items():
        if value > count:
            count = value
            most = key
    return count, most

def get_total_rating_dict(movie_library):
    rating_dict = {}
    for movie in movie_library:
        for name in movie.get('actors'):
            if name in rating_dict:
                rating_dict[name] += movie.get('rating')
            else:
                rating_dict[name] = movie.get('rating')
    return rating_dict

def average_rating_dict(rating_dict, freq_dict):
    average = [float(r) / float(f) for r, f in zip(rating_dict.values(), freq_dict.values())]
    for  key in rating_dict:
        rating_dict[key] = average.pop(0)
    return rating_dict

def get_best_rating_actors(rating_dict):
    best_score, best_actors = 0, []
    for key in rating_dict:
        if rating_dict[key] > best_score:
            best_score = rating_dict[key]   
    for key in rating_dict:
        if rating_dict[key] == best_score:
            best_actors.append(key)
    return best_actors, best_score

def check_eighties_only(movie_library):
    eighties = []
    for movie in movie_library:
        if movie.get('year') >= 1980 and movie.get('year') < 1990:
            eighties.append(movie.get('genre'))
    return eighties

def least_in_eighties(eighties):
    eighties = min(set(eighties), key = eighties.count)
    print(f'The least popular genre in the eighties was {eighties}\n')

def not_in_eighties(movie_library, eighties):
    genre_list = []
    for movie in movie_library:
        genre = movie.get('genre')
        if genre not in eighties:
            genre_list.append(genre)
            print(f'The least popular genre in the eighties was {genre_list[0]}\n')
            break
    if len(genre_list) == 0:
        least_in_eighties(eighties)
            

            
if __name__ == '__main__':
    main()

