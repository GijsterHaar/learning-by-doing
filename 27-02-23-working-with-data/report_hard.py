import movie_data

def main():
    count = 0
    most = ''
    freq_dict={}
    rating_dict={}
    genre_freq_dict = {}
    best_score = 0
    best_actors = []
    eighties = []

    movie_library = movie_data.movies
    freq_dict = movies_actor_dict(movie_library, freq_dict)
    count, most = the_most_movies_actor(freq_dict, count, most)
    print(f'\nThe actor appearing in most movies with {count} appearances is {most}\n')
    get_rating_dict(movie_library, rating_dict)
    rating_dict = average_rating_dict(rating_dict, freq_dict)
    best_actors, best_score = get_best_rating_actors(rating_dict, best_score, best_actors)
    best_actors = ', '.join(best_actors)
    print(f'The best actors are {best_actors} with an average rating of {best_score}\n')
    genre_freq_dict = genre_frequency_dict(movie_library, genre_freq_dict)
    eighties = check_eighties_only(movie_library, genre_freq_dict, eighties)
    least_in_eighties(movie_library, eighties)

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

def get_rating_dict(movie_library, rating_dict):
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

def get_best_rating_actors(rating_dict, best_score, best_actors):
    for key in rating_dict:
        if rating_dict[key] > best_score:
            best_score = rating_dict[key]   
    for key in rating_dict:
        if rating_dict[key] == best_score:
            best_actors.append(key)
    return best_actors, best_score

def genre_frequency_dict(movie_library, genre_freq_dict):
    for movie in movie_library:
        genre = movie.get('genre')
        if genre in genre_freq_dict:
            genre_freq_dict[genre] += 1
        else:
            genre_freq_dict[genre] = 1
    return genre_freq_dict

def check_eighties_only(movie_library, genre_freq_dict, eighties):
    for movie in movie_library:
        if movie.get('year') >= 1980 and movie.get('year') < 1990:
            eighties.append(movie.get('genre'))
    return eighties

def least_in_eighties(movie_library, eighties):
    genre_list = []
    for movie in movie_library:
        genre = movie.get('genre')
        if genre not in eighties:
            genre_list.append(genre)
            print(f'The least popular genre in the eighties was {genre_list[0]}\n')
            break

if __name__ == '__main__':
    main()

