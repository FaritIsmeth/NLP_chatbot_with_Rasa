from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

# class ActionRecommendMovies(Action):
#     def name(self) -> Text:
#         return "action_recommend_movies"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         genre = next(tracker.get_latest_entity_values("genre"), None)
#
#         if not genre:
#             response_text = "I'm sorry, I couldn't detect the genre you're looking for."
#             dispatcher.utter_message(text=response_text)
#             return []
#
#         # Make API request to fetch movie recommendations based on genre
#         api_key = 'f62b899ae8cc28bf4c7321f9dbb3bcb5'  # Replace with your TMDb API key
#
#         # Fetch genre ID from TMDb API
#         genre_id = self.get_genre_id(genre, api_key)
#
#         if genre_id:
#             api_endpoint = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}'
#             response = requests.get(api_endpoint)
#
#             if response.status_code == 200:
#                 movies = response.json().get('results', [])
#                 if movies:
#                     recommended_movies = [movie['title'] for movie in movies]
#                     response_text = f"Sure! Here are some {genre} movie recommendations for you: "
#                     response_text += ", ".join(recommended_movies)
#                 else:
#                     response_text = "I'm sorry, I couldn't find any recommendations for that genre."
#             else:
#                 response_text = "Oops! Something went wrong while fetching recommendations. Please try again later."
#         else:
#             response_text = "I'm sorry, I couldn't find that genre in my database."
#
#         dispatcher.utter_message(text=response_text)
#
#         return []
#
#     def get_genre_id(self, genre, api_key):
#         genre_endpoint = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}'
#         response = requests.get(genre_endpoint)
#
#         if response.status_code == 200:
#             genres = response.json().get('genres', [])
#             for g in genres:
#                 if g['name'].lower() == genre.lower():
#                     return g['id']
#         return None

# class ActionShowDescription(Action):
#     def name(self) -> Text:
#         return "action_show_description"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         #genre = next(tracker.get_latest_entity_values("genre"), None)
#         genre = "comedy"
#         movie = next(tracker.get_latest_entity_values("movie"), None)
#
#         if not genre:
#             response_text = "Sorry, unable to understand your request"
#             dispatcher.utter_message(text=response_text)
#             return []
#
#         # Make API request to fetch movie recommendations based on genre
#         api_key = 'f62b899ae8cc28bf4c7321f9dbb3bcb5'  # Replace with your TMDb API key
#
#         # Fetch genre ID from TMDb API
#         genre_id = self.get_genre_id(genre, api_key)
#
#         if genre_id:
#             api_endpoint = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}'
#             response = requests.get(api_endpoint)
#             comedy_movie_list = [
#                 "Kung Fu Panda 4",
#                 "Migration",
#                 "Argylle",
#                 "Megamind vs. the Doom Syndicate",
#                 "Wonka",
#                 "Poor Things",
#                 "Ghostbusters: Frozen Empire",
#                 "Anyone But You",
#                 "Jaque Mate",
#                 "The Casagrandes Movie",
#                 "Skal - Fight for Survival",
#                 "Freelance",
#                 "The Thundermans Return",
#                 "Kung Fu Panda",
#                 "Irish Wish",
#                 "The Adventures",
#                 "The Super Mario Bros. Movie",
#                 "The Family Plan",
#                 "Cat and Dog",
#                 "Robot Dreams"]
#
#             if response.status_code == 200:
#                 movies = response.json().get('results', [])
#                 if movies:
#                     for movie in movies:
#                         movie_description = movie.get('overview', '')
#                         response_text = f"Sure! Here's the movie description for {movie}: {movie_description}"
#                         #dispatcher.utter_message(text=response_text)
#                 else:
#                     response_text = "I'm sorry, I couldn't find any recommendations for that genre."
#             else:
#                 response_text = "Oops! Something went wrong while fetching recommendations. Please try again later."
#         else:
#             response_text = "I'm sorry, I couldn't find that genre in my database."
#
#         dispatcher.utter_message(text=response_text)
#
#         return []
#
#     def get_genre_id(self, genre, api_key):
#         genre_endpoint = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}'
#         response = requests.get(genre_endpoint)
#
#         if response.status_code == 200:
#             genres = response.json().get('genres', [])
#             for g in genres:
#                 if g['name'].lower() == genre.lower():
#                     return g['id']
#         return None

# class ActionShowPoster(Action):
#     def name(self) -> Text:
#         return "action_show_poster"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         movie_poster = next(tracker.get_latest_entity_values("movie_poster"), None)
#         if movie_poster == "Anyone But You":
#             response_text = movie_poster
#             image_url = "/Users/fr/PycharmProjects/Chatbot_v1/RasaFlask/static/images/anyone-but-you.jpeg"
#             dispatcher.utter_message(text=response_text, image=image_url)
#         elif movie_poster == "Argylle":
#             response_text = movie_poster
#             image_url = "/Users/fr/PycharmProjects/Chatbot_v1/RasaFlask/static/images/argylle.jpeg"
#             dispatcher.utter_message(text=response_text, image=image_url)
#         elif movie_poster == "Cat and Dog":
#             response_text = movie_poster
#             image_url = "/Users/fr/PycharmProjects/Chatbot_v1/RasaFlask/static/images/cat-and-dog.jpeg"
#             dispatcher.utter_message(text=response_text, image=image_url)
#         elif movie_poster == "The Casagrandes Movie":
#             response_text = movie_poster
#             image_url = "/Users/fr/PycharmProjects/Chatbot_v1/RasaFlask/static/images/de-casagrandes.jpeg"
#             dispatcher.utter_message(text=response_text, image=image_url)
#         elif movie_poster == "Freelance":
#             response_text = movie_poster
#             image_url = "/Users/fr/PycharmProjects/Chatbot_v1/RasaFlask/static/images/freelance.jpeg"
#             dispatcher.utter_message(text=response_text, image=image_url)
#         elif movie_poster == "Ghostbusters: Frozen Empire":
#             response_text = movie_poster
#             image_url = "/Users/fr/PycharmProjects/Chatbot_v1/RasaFlask/static/images/ghostbusters-frozen-empire.jpeg"
#             dispatcher.utter_message(text=response_text, image=image_url)
#         elif movie_poster == "Irish Wish":
#             response_text = movie_poster
#             image_url = "/Users/fr/PycharmProjects/Chatbot_v1/RasaFlask/static/images/irish-wish.jpeg"
#             dispatcher.utter_message(text=response_text, image=image_url)
#         elif movie_poster == "Jaque Mate":
#             response_text = movie_poster
#             image_url = "/Users/fr/PycharmProjects/Chatbot_v1/RasaFlask/static/images/jaque-mate.jpeg"
#             dispatcher.utter_message(text=response_text, image=image_url)
#         elif movie_poster == "Kung Fu Panda 4":
#             response_text = movie_poster
#             image_url = "/Users/fr/PycharmProjects/Chatbot_v1/RasaFlask/static/images/kung-fu-panda-4.jpeg"
#             dispatcher.utter_message(text=response_text, image=image_url)
#         elif movie_poster == "Megamind vs. the Doom Syndicate":
#             response_text = movie_poster
#             image_url = "/Users/fr/PycharmProjects/Chatbot_v1/RasaFlask/static/images/megamind-vs-the-doom-syndicate.jpeg"
#             dispatcher.utter_message(text=response_text, image=image_url)
#         elif movie_poster == "Migration":
#             response_text = movie_poster
#             image_url = "/Users/fr/PycharmProjects/Chatbot_v1/RasaFlask/static/images/migration.jpeg"
#             dispatcher.utter_message(text=response_text, image=image_url)
#         elif movie_poster == "Poor Things":
#             response_text = movie_poster
#             image_url = "/Users/fr/PycharmProjects/Chatbot_v1/RasaFlask/static/images/poor-things.jpeg"
#             dispatcher.utter_message(text=response_text, image=image_url)
#         elif movie_poster == "Robot Dreams":
#             response_text = movie_poster
#             image_url = "/Users/fr/PycharmProjects/Chatbot_v1/RasaFlask/static/images/robot-dreams.jpeg"
#             dispatcher.utter_message(text=response_text, image=image_url)
#         elif movie_poster == "Skal - Fight for Survival":
#             response_text = movie_poster
#             image_url = "/Users/fr/PycharmProjects/Chatbot_v1/RasaFlask/static/images/skal.jpeg"
#             dispatcher.utter_message(text=response_text, image=image_url)
#         elif movie_poster == "The Adventures":
#             response_text = movie_poster
#             image_url = "/Users/fr/PycharmProjects/Chatbot_v1/RasaFlask/static/images/the-adventures.jpeg"
#             dispatcher.utter_message(text=response_text, image=image_url)
#         elif movie_poster == "The Family Plan":
#             response_text = movie_poster
#             image_url = "/Users/fr/PycharmProjects/Chatbot_v1/RasaFlask/static/images/the-family-plan.jpeg"
#             dispatcher.utter_message(text=response_text, image=image_url)
#         elif movie_poster == "The Super Mario Bros. Movie":
#             response_text = movie_poster
#             image_url = "/Users/fr/PycharmProjects/Chatbot_v1/RasaFlask/static/images/the-super-mario-bros-movie.jpeg"
#             dispatcher.utter_message(text=response_text, image=image_url)
#         elif movie_poster == "The Thundermans Return":
#             response_text = movie_poster
#             image_url = "/Users/fr/PycharmProjects/Chatbot_v1/RasaFlask/static/images/the-thundermans-return.jpeg"
#             dispatcher.utter_message(text=response_text, image=image_url)
#         elif movie_poster == "Wonka":
#             response_text = movie_poster
#             image_url = "https://m.media-amazon.com/images/M/MV5BMDBmYTZjNjUtN2M1MS00MTQ2LTk2ODgtNzc2M2QyZGE5NTVjXkEyXkFqcGdeQXVyNzAwMjU2MTY@._V1_SX300.jpg"
#             dispatcher.utter_message(text=response_text, image=image_url)
#
#         return []

class ActionShowAllMovies(Action):
    def name(self) -> Text:
        return "action_show_all_movies"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        title = ["leo", "barbie", "poor things", "the holdovers", "killers of the flower moon", "about dry grasses", "anatomy of a fall", "the promised land", "fallen leaves", "perfect days", "the taste of things", "spider-man: across the spider-verse", "the zone of interest", "american fiction", "the boy and the heron", "dungeons & dragons: honor among thieves", "mission: impossible - dead reckoning part one", "john wick: chapter 4", "guardians of the galaxy vol. 3", "godzilla minus one"]
        get_title_arr = []
        year = "2023"
        plot = "full"
        api_key = ""
        for i in range(len(title)):
            url = f"http://www.omdbapi.com/?t={title[i]}&y={year}&plot={plot}&apikey={api_key}"
            response = requests.get(url)
            movie_info = response.json()
            get_title_arr.append(movie_info.get("Title"))
            print("Movie Title:", get_title_arr[i])
        response_text = f"Sure! Here is the movie title: \n\n"
        response_text += ", ".join(get_title_arr)

        dispatcher.utter_message(text=response_text)
        return []

class ActionShowMovieRatings(Action):
    def name(self) -> Text:
        return "action_show_movie_ratings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        movie_ratings = next(tracker.get_latest_entity_values("movie_ratings"), None)
        #title = ["leo", "oppenheimer", "poor things", "the holdovers", "killers of the flower moon", "about dry grasses", "anatomy of a fall", "the promised land", "fallen leaves", "perfect days", "the taste of things", "spider-man: across the spider-verse", "the zone of interest", "american fiction", "the boy and the heron", "dungeons & dragons: honor among thieves", "mission: impossible - dead reckoning part one", "john wick: chapter 4", "guardians of the galaxy vol. 3", "godzilla minus one"]
        get_rating_arr = []
        year = "2023"
        plot = "full"
        api_key = ""
        #for i in range(len(title)):
        url = f"http://www.omdbapi.com/?t={movie_ratings.lower()}&y={year}&plot={plot}&apikey={api_key}"
        response = requests.get(url)
        movie_info = response.json()
        get_rating_arr.append(movie_info.get("Rated"))
        print("Movie Ratings:", get_rating_arr[0])
        response_text = f"The movie ratings for {movie_ratings} is: {get_rating_arr}"
        #response_text += ", ".join(get_title_arr)

        dispatcher.utter_message(text=response_text)
        return []

class ActionShowMovieReleased(Action):
    def name(self) -> Text:
        return "action_show_movie_released"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        movie_released = next(tracker.get_latest_entity_values("movie_released"), None)
        #title = ["leo", "oppenheimer", "poor things", "the holdovers", "killers of the flower moon", "about dry grasses", "anatomy of a fall", "the promised land", "fallen leaves", "perfect days", "the taste of things", "spider-man: across the spider-verse", "the zone of interest", "american fiction", "the boy and the heron", "dungeons & dragons: honor among thieves", "mission: impossible - dead reckoning part one", "john wick: chapter 4", "guardians of the galaxy vol. 3", "godzilla minus one"]
        get_released_arr = []
        year = "2023"
        plot = "full"
        api_key = ""
        #for i in range(len(title)):
        url = f"http://www.omdbapi.com/?t={movie_released.lower()}&y={year}&plot={plot}&apikey={api_key}"
        response = requests.get(url)
        movie_info = response.json()
        get_released_arr.append(movie_info.get("Released"))
        print("Movie Released Date:", get_released_arr[0])
        response_text = f"{movie_released} was released on: {get_released_arr}"
        #response_text += ", ".join(get_title_arr)

        dispatcher.utter_message(text=response_text)
        return []

class ActionShowMovieGenre(Action):
    def name(self) -> Text:
        return "action_show_movie_genre"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        movie_genre = next(tracker.get_latest_entity_values("movie_genre"), None)
        #title = ["leo", "oppenheimer", "poor things", "the holdovers", "killers of the flower moon", "about dry grasses", "anatomy of a fall", "the promised land", "fallen leaves", "perfect days", "the taste of things", "spider-man: across the spider-verse", "the zone of interest", "american fiction", "the boy and the heron", "dungeons & dragons: honor among thieves", "mission: impossible - dead reckoning part one", "john wick: chapter 4", "guardians of the galaxy vol. 3", "godzilla minus one"]
        get_genre_arr = []
        year = "2023"
        plot = "full"
        api_key = ""
        #for i in range(len(title)):
        url = f"http://www.omdbapi.com/?t={movie_genre.lower()}&y={year}&plot={plot}&apikey={api_key}"
        response = requests.get(url)
        movie_info = response.json()
        get_genre_arr.append(movie_info.get("Genre"))
        print("Movie Genres:", get_genre_arr[0])
        response_text = f"Here's the genre(s) for {movie_genre}: {get_genre_arr}"
        #response_text += ", ".join(get_title_arr)

        dispatcher.utter_message(text=response_text)
        return []

class ActionShowMovieDirector(Action):
    def name(self) -> Text:
        return "action_show_movie_director"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        movie_director = next(tracker.get_latest_entity_values("movie_director"), None)
        #title = ["leo", "oppenheimer", "poor things", "the holdovers", "killers of the flower moon", "about dry grasses", "anatomy of a fall", "the promised land", "fallen leaves", "perfect days", "the taste of things", "spider-man: across the spider-verse", "the zone of interest", "american fiction", "the boy and the heron", "dungeons & dragons: honor among thieves", "mission: impossible - dead reckoning part one", "john wick: chapter 4", "guardians of the galaxy vol. 3", "godzilla minus one"]
        get_director_arr = []
        year = "2023"
        plot = "full"
        api_key = ""
        #for i in range(len(title)):
        url = f"http://www.omdbapi.com/?t={movie_director.lower()}&y={year}&plot={plot}&apikey={api_key}"
        response = requests.get(url)
        movie_info = response.json()
        get_director_arr.append(movie_info.get("Director"))
        print("Movie Director:", get_director_arr[0])
        response_text = f"The director for {movie_director} is: {get_director_arr}"
        #response_text += ", ".join(get_title_arr)

        dispatcher.utter_message(text=response_text)
        return []

class ActionShowMovieActors(Action):
    def name(self) -> Text:
        return "action_show_movie_actors"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        movie_actors = next(tracker.get_latest_entity_values("movie_actors"), None)
        #title = ["leo", "oppenheimer", "poor things", "the holdovers", "killers of the flower moon", "about dry grasses", "anatomy of a fall", "the promised land", "fallen leaves", "perfect days", "the taste of things", "spider-man: across the spider-verse", "the zone of interest", "american fiction", "the boy and the heron", "dungeons & dragons: honor among thieves", "mission: impossible - dead reckoning part one", "john wick: chapter 4", "guardians of the galaxy vol. 3", "godzilla minus one"]
        get_actors_arr = []
        year = "2023"
        plot = "full"
        api_key = ""
        #for i in range(len(title)):
        url = f"http://www.omdbapi.com/?t={movie_actors.lower()}&y={year}&plot={plot}&apikey={api_key}"
        response = requests.get(url)
        movie_info = response.json()
        get_actors_arr.append(movie_info.get("Actors"))
        print("Movie Actors:", get_actors_arr[0])
        response_text = f"Here are the people that played in {movie_actors}: {get_actors_arr}"
        #response_text += ", ".join(get_title_arr)

        dispatcher.utter_message(text=response_text)
        return []

class ActionShowMoviePlot(Action):
    def name(self) -> Text:
        return "action_show_movie_plot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        movie_plot = next(tracker.get_latest_entity_values("movie_plot"), None)
        #title = ["leo", "oppenheimer", "poor things", "the holdovers", "killers of the flower moon", "about dry grasses", "anatomy of a fall", "the promised land", "fallen leaves", "perfect days", "the taste of things", "spider-man: across the spider-verse", "the zone of interest", "american fiction", "the boy and the heron", "dungeons & dragons: honor among thieves", "mission: impossible - dead reckoning part one", "john wick: chapter 4", "guardians of the galaxy vol. 3", "godzilla minus one"]
        get_plot_arr = []
        year = "2023"
        plot = "full"
        api_key = ""
        #for i in range(len(title)):
        url = f"http://www.omdbapi.com/?t={movie_plot.lower()}&y={year}&plot={plot}&apikey={api_key}"
        response = requests.get(url)
        movie_info = response.json()
        get_plot_arr.append(movie_info.get("Plot"))
        print("Movie Plot:", get_plot_arr[0])
        response_text = f"Here's the plot for {movie_plot}: {get_plot_arr}"
        #response_text += ", ".join(get_title_arr)

        dispatcher.utter_message(text=response_text)
        return []

class ActionShowMoviePoster(Action):
    def name(self) -> Text:
        return "action_show_movie_poster"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        movie_poster = next(tracker.get_latest_entity_values("movie_poster"), None)
        #title = ["leo", "oppenheimer", "poor things", "the holdovers", "killers of the flower moon", "about dry grasses", "anatomy of a fall", "the promised land", "fallen leaves", "perfect days", "the taste of things", "spider-man: across the spider-verse", "the zone of interest", "american fiction", "the boy and the heron", "dungeons & dragons: honor among thieves", "mission: impossible - dead reckoning part one", "john wick: chapter 4", "guardians of the galaxy vol. 3", "godzilla minus one"]
        get_poster_arr = []
        year = "2023"
        plot = "full"
        api_key = ""
        #for i in range(len(title)):
        url = f"http://www.omdbapi.com/?t={movie_poster.lower()}&y={year}&plot={plot}&apikey={api_key}"
        response = requests.get(url)
        movie_info = response.json()
        get_poster_arr.append(movie_info.get("Poster"))
        print("Movie Poster:", get_poster_arr[0])
        #response_text = f"Here's the plot for {movie_poster}: {get_poster_arr}"
        #response_text += ", ".join(get_title_arr)
        response_text = movie_poster
        image_url = get_poster_arr[0]
        dispatcher.utter_message(text=response_text, image=image_url)
        return []