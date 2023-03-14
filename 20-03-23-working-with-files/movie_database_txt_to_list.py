
SHOW_MENU_AGAIN = True
DO_NOT_SHOW_MENU = False

def main():
    with open("movie_data.txt", 'r') as movie_text:
        movie_file = movie_text.readlines()
    movie_file = [i.strip() for i in movie_file]
    main_menu = SHOW_MENU_AGAIN
    while main_menu:
        start_message()
        main_menu = navigate_main_menu(movie_file)
    
    
def start_message():
    print("""   \nMovie Database. You can enter your choice of action.
===========================================================
1. List: name and year of all movies.
2. Actor search by name: name and year of all their movies.
3. Genre search: name and year of all movies in that genre.
4. Add: add title, actor, year, genre and rating.
5. Quit\n""")


def get_movie_list(movie_file):
    chunked_file = chunk_file(movie_file)
    for movie in chunked_file:
        title, year = movie[0], movie[2]
        print(f'{title}, {year}')
    print('\nThese are all the movies in this movie library\nWhat next?\n')
    return SHOW_MENU_AGAIN


def search_actor_list(movie_file):
    name = input('Please enter the full name: ')
    chunked_file = chunk_file(movie_file)
    for movies in chunked_file:
        if name.title() in movies[1]:
            extract_search_data(movies)
    print(f'\nThese are all the {name.title()} movies in this movie library\nWhat next?\n')
    return SHOW_MENU_AGAIN


def search_genre_list(movie_file):
    genre = input('Please enter the genre: ')
    chunked_file = chunk_file(movie_file)
    for movies in chunked_file:
        if genre.lower() in movies:
            extract_search_data(movies)
    print(f'\nThese are all the {genre} movies in this movie library\nWhat next?\n')
    return SHOW_MENU_AGAIN


def chunk_file(movie_file):
    chunk_size = 5
    chunked_file = [movie_file[i:i + chunk_size] for i in range(0, len(movie_file), chunk_size)]
    return chunked_file


def extract_search_data(movies):
    titles = movies[0]
    year = movies[2]
    print(f'{titles}, {year}.')


def input_movies():
    title = input('Please enter your title: ').title()
    actors = input('Please enter the actors, separated by a comma: ').title().split(', ')
    year = int(input('Please enter the year: '))
    genre = input('Please enter the genre: ')
    rating = int(input('Please enter the rating: '))
    update_txtfile(title, actors, year, genre, rating)
    return title, actors, year, genre, rating


def add_movie(movie_file):
    title, actors, year, genre, rating = input_movies()
    movie_file.append(title)
    movie_file.append(actors)
    movie_file.append(year)
    movie_file.append(genre)
    movie_file.append(rating)
    return SHOW_MENU_AGAIN


def update_txtfile(title, actors, year, genre, rating):
    with open("movie_data.txt", 'a') as file:
        actors = ', '.join(actors)
        file.write(f'\n{title}\n{actors}\n{str(year)}\n{genre}\n{str(rating)}')


def opt_out(movie_file):
    print()
    return DO_NOT_SHOW_MENU


def navigate_main_menu(movie_file):
    enter_choice = int(input('Enter your choice here: '))
    print()
    menu_list = [get_movie_list, search_actor_list, search_genre_list, add_movie, opt_out]
    return menu_list[enter_choice -1](movie_file)


if __name__ == '__main__':
    main()