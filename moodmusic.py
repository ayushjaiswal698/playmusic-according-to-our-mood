import webbrowser
from textblob import TextBlob
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# 🎯 Step 1: Detect Mood (Extended with Keyword Matching)
def get_mood_from_text(text):
    text = text.lower()

    mood_keywords = {
        "happy": ["happy", "joy", "excited", "great"],
        "sad": ["sad", "down", "upset", "depressed"],
        "chill": ["calm", "chill", "relaxed", "okay"],
        "party": ["party", "celebrate", "dance"],
        "lonely": ["alone", "lonely", "isolated"],
        "very sad": ["heartbroken", "crying", "devastated"],
        "spiritual": ["peaceful", "meditate", "spiritual", "god"],
        "patriotic": ["country", "nation", "patriotic", "india"],
        "motivated": ["motivated", "pumped", "driven"],
        "angry": ["angry", "mad", "furious"],
        "romantic": ["love", "romantic", "crush", "date"],
        "retro": ["retro", "old school", "classic", "vintage"]
    }

    for mood, keywords in mood_keywords.items():
        if any(word in text for word in keywords):
            return mood

    # If nothing matches, fall back to sentiment analysis
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "happy"
    elif polarity < -0.2:
        return "sad"
    else:
        return "chill"

# 🎵 Step 2: Recommend Songs Using Spotify
def get_playlist_for_mood(mood):
    mood_queries = {
        "happy": "happy mood",
        "sad": "sad songs",
        "chill": "lofi chill beats",
        "party": "party dance hits",
        "lonely": "lonely acoustic songs",
        "very sad": "heartbreak songs",
        "spiritual": "spiritual mantra",
        "patriotic": "patriotic songs india",
        "motivated": "motivational workout music",
        "angry": "hard rock angry music",
        "romantic": "romantic love songs",
        "retro": "retro classics hits"
    }

    query = mood_queries.get(mood, "chill")
    results = sp.search(q=query, type='track', limit=5)

    print(f"\n🎶 Recommended songs for your mood ({mood}):")
    for i, track in enumerate(results['tracks']['items']):
        name = track['name']
        artist = track['artists'][0]['name']
        url = track['external_urls']['spotify']
        print(f"{i+1}. {name} - {artist}")
        print(f"   Listen: {url}")

        play = input(f"Do you want to play '{name}'? (y/n): ")
        if play.lower() == 'y':
            webbrowser.open(url)

# 🛠️ Step 3: Set Up Spotify API
client_id = "ffb4b601cfd944d68fdcfe8327cc0580"
client_secret = "495f5e54cf3f447facc7ec75a8769626"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
))

# 🚀 Step 4: Run the Program
user_input = input("How are you feeling today? ")
mood = get_mood_from_text(user_input)
print("Detected mood:", mood)
get_playlist_for_mood(mood)
