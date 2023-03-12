import movie_data
"""
This program will import the movie data, and then provide a menu of options to the user.
The user can select an option, the program will do it, and afterwards the program should return to the main menu. The options are:
    1. *List :* List the name and year of all movies, separated by a comma.
    2. *Actor Search :* Prompt for an actor's name, then list the name and year of all their movies.
    3. *Genre Search :* Prompt for a genre name, then list the name and year of every movie in that genre.
    4. *Add :* Prompts for a title, actors, year, genre, and a rating, then adds that movie to the database in memory. This new movie should show up in the other searches.
    5. *Quit :* Ends the program.
"""

def main():
    start_message()
    main_choice = enter_main_menu()
    print()
    navigate_main_menu(main_choice)


def start_message():
    print("""\n   Movie Database. You can enter your choice of action.
===========================================================
1. List: name and year of all movies.
2. Actor search by name: name and year of all their movies.
3. Genre search: name and year of all movies in that genre.
4. Add: add title, actor, year, genre and rating.
5. Quit\n""")

def enter_main_menu():
    return int(input('Enter your choice here: '))

def get_movie_list():
    movie_library = movie_data.movies
    for movie in movie_library:
        title, year = movie.get('title'), movie.get('year')
        print(f'{title}, {year}.')
    print()       

def get_actor_data():
    print(2)

def get_movies_by_genre():
    print(3)

def add_movies():
    print(4)

def opt_out():
    print(5)

def navigate_main_menu(main_choice):
    menu_list = [get_movie_list, get_actor_data, get_movies_by_genre, add_movies, quit]
    return menu_list[main_choice -1]()







if __name__ == '__main__':
    main()