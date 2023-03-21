import json
import requests
from secrets import spotify_user_id, discover_weekly_id
from datetime import date
from refresh import Refresh 

class SaveSongs:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = ""
        self.discover_weekly_id=discover_weekly_id
        self.tracks=""
        self.new_playlist_id=""
        self.seed_tracks = "2bdVgAQgosGUJoViVDNeOV"
        self.seed_artists = "3pc0bOVB5whxmD50W79wwO"
        self.seed_genres = "pop,rock"
        
    def find_songs(self):
        #loop through playlist tracks and add them to a list
        
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            discover_weekly_id
        )

        response = requests.get(query,
        headers={"Content-Type":"application/json",
        "Authorization":"Bearer {}".format(self.spotify_token)})  

        response_json = response.json()

        for i in response_json["items"]:
            self.tracks+=(i["track"]["uri"] +",")

        self.tracks = self.tracks[:-1]

        self.add_to_playlist()

    def recommend_songs(self):
        #find recommended songs based on preferences
        print("recommending songs")
        query = "https://api.spotify.com/v1/recommendations?limit=10&seed_artists={}&seed_genres={}&seed_tracks={}".format(self.seed_artists, self.seed_genres, self.seed_tracks)

        response = requests.get(query,
                                headers={"Content-Type":"application/json",
        "Authorization":"Bearer {}".format(self.spotify_token),})

        response_json = response.json()
        for i in response_json["tracks"]:
            self.tracks += (i["uri"]+",")
        self.tracks = self.tracks[:-1]

        self.add_to_playlist()

        

    def create_playlist(self):
        print ("Trying to Create Playlist...")
        today=date.today()
        todayFormatted = today.strftime("%d/%m/%y")

        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            spotify_user_id
        )
        request_body=json.dumps({
            "name": todayFormatted + " muse test",
            "description": "hello",
            "public": True
        })
        
        response = requests.post(query, data=request_body, headers={"Content-Type":"application/json",
        "Authorization":"Bearer {}".format(self.spotify_token)
        }) 

        response_json = response.json()
        print(response_json)
        
        return response_json["id"] 
        # print(self.new_playlist_id)
        
        

    def add_to_playlist(self):
        print("Adding songs...")

        self.new_playlist_id=self.create_playlist()

        query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(self.new_playlist_id, self.tracks)

        response = requests.post(query, headers={"Content-Type":"application/json",
        "Authorization":"Bearer {}".format(self.spotify_token)
        })   

        print (response.json)

    def call_refresh(self):
        print("refreshing token")
        refreshCaller = Refresh()
        self.spotify_token = refreshCaller.refresh()

        self.recommend_songs()

a = SaveSongs()
a.call_refresh()