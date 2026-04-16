def play_movie(title):
    print(f"Play {title}")

def add_to_favorite(title):
    print(f"Add {title} to favorite")

def show_movies(movie_list):
    for movie in movie_list:
        print(movie)

def handle_user_action(title, action):
    if action == "PLAY":
        play_movie(title)
    elif action == "FAVORITE":
        add_to_favorite(title)
    else:
        print("Invalid action")

movies = ["Wednesday", "Stranger Things", "Money Heist"]

show_movies(movies)
handle_user_action("Wednesday", "PLAY")
