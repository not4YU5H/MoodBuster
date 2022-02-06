import json
import spotipy
import webbrowser

username = '6xn5njq2s8l4gup154dtxp6ug'
clientID = '999f4585cb7f4fc99b869b24594c2def'
clientSecret = 'a10fd44617564a4eb4c11ae65539aa5b'
redirectURI = 'http://google.com/'


oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user = spotifyObject.current_user()
print(json.dumps(user,sort_keys=True, indent=4))

choice = 0
searchResults = spotifyObject.search("lovely",1,0,"track")

def on_music(ch):
    choice = ch
    if ch==1:
        searchResults = spotifyObject.search("lovely",1,0,"track")
    elif ch==2:
        searchResults = spotifyObject.search("Smells Like Teen Spirit",1,0,"track")
    elif ch==3:
        searchResults = spotifyObject.search("Sunflower",1,0,"track")
    else:
        print("No song played")

    if choice!=0:
            # Get required data from JSON response.
            tracks_dict = searchResults['tracks']
            tracks_items = tracks_dict['items']
            song = tracks_items[0]['external_urls']['spotify']
            # Open the Song in Web Browser
            webbrowser.open(song)
            print('Song has opened in your browser.')

