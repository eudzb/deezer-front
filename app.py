from flask import Flask, render_template, request, session, logging, url_for, redirect, flash
import requests, json, datetime, random, os
import logging
from werkzeug.utils import secure_filename
from time import *
from flask_cors import CORS, cross_origin

# Instancier notre application dont le nom est __main__
app = Flask(__name__)
CORS(app)
URL_API = "https://api.deezer.com"

@app.route('/')
@cross_origin() # allow all origins all methods.
def home():

    genres = requests.get(URL_API + "/genre")
    json_genres = genres.json()
    return json_genres

#Album
@app.route('/album')
@cross_origin() # allow all origins all methods.
def idAlbum():

    id = request.args.get('id')
    idAlbums = requests.get(URL_API + "/album/" + id)
    json_album = idAlbums.json()
    return json_album
 
@app.route('/topAlbum')
@cross_origin() # allow all origins all methods.
def topAlbum():

    albums = requests.get(URL_API + "/chart/0/albums?limit=10")
    json_albums = albums.json()
    return json_albums

#Artist
@app.route('/artist')
@cross_origin() # allow all origins all methods.
def idArtist():

    id = request.args.get('id')
    idArtist = requests.get(URL_API + "/artist/" + id)
    json_artist = idArtist.json()
    return json_artist
 
@app.route('/topArtist')
@cross_origin() # allow all origins all methods.
def topArtist():

    topArtists = requests.get(URL_API + "/chart/0/artists")
    json_artists = topArtists.json()
    return json_artists

@app.route('/artistRelated')
@cross_origin() # allow all origins all methods.
def artisrRelated():

    id = request.args.get('id')
    artistRelated = requests.get(URL_API + "/artist/" + id + "/related?limit=5")
    json_artist_related = artistRelated.json()
    return json_artist_related

@app.route('/artistTopTrack')
@cross_origin() # allow all origins all methods.
def artistTopTrack():

    id = request.args.get('id')
    artistTopTrack = requests.get(URL_API + "/artist/" + id + "/top")
    json_artist_top_track = artistTopTrack.json()
    return json_artist_top_track

@app.route('/artistAlbum')
@cross_origin() # allow all origins all methods.
def artistAlbum():

    id = request.args.get('id')
    artistAlbum = requests.get(URL_API + "/artist/" + id + "/albums")
    json_artist_album = artistAlbum.json()
    return json_artist_album

#Genre
@app.route('/genre')
@cross_origin() # allow all origins all methods.
def idGenre():

    id = request.args.get('id')
    idGenre = requests.get(URL_API + "/genre/" + id)
    json_genre = idGenre.json()
    return json_genre

@app.route('/genreArtist')
@cross_origin() # allow all origins all methods.
def genreArtist():

    id = request.args.get('id')
    genreArtist = requests.get(URL_API + "/genre/" + id + "/artists?limit=15")
    json_genre_artist = genreArtist.json()
    return json_genre_artist

@app.route('/genrePodcast')
@cross_origin() # allow all origins all methods.
def genrePodcast():

    id = request.args.get('id')
    genrePodcast = requests.get(URL_API + "/genre/" + id + "/podcasts?limit=15")
    json_genre_podcast = genrePodcast.json()
    return json_genre_podcast

@app.route('/genreRadios')
@cross_origin() # allow all origins all methods.
def genreRadios():

    id = request.args.get('id')
    genreRadios = requests.get(URL_API + "/genre/" + id + "/radios?limit=15")
    json_genre_radios = genreRadios.json()
    return json_genre_radios

#Search Albums
@app.route('/searchAlbums')
@cross_origin() # allow all origins all methods.
def searchAlbums():

    search = request.args.get('search')
    albums = requests.get(URL_API + "/search/album?q=" + search)
    json_albums = albums.json()
    return json_albums

#Search Artists
@app.route('/searchArtists')
@cross_origin() # allow all origins all methods.
def searchArtists():

    search = request.args.get('search')
    artists = requests.get(URL_API + "/search/artist?q=" + search)
    json_artists = artists.json()
    return json_artists

#Search Podcasts
@app.route('/searchPodcasts')
@cross_origin() # allow all origins all methods.
def searchPodcasts():

    search = request.args.get('search')
    podcasts = requests.get(URL_API + "/search/podcast?q=" + search)
    json_podcasts = podcasts.json()
    return json_podcasts

#Search Radios
@app.route('/searchRadios')
@cross_origin() # allow all origins all methods.
def searchRadios():

    search = request.args.get('search')
    radios = requests.get(URL_API + "/search/radio?q=" + search)
    json_radios = radios.json()
    return json_radios

#Search Tracks
@app.route('/searchTracks')
@cross_origin() # allow all origins all methods.
def searchTracks():

    search = request.args.get('search')
    tracks = requests.get(URL_API + "/search/track?q=" + search + "&limit=5")
    json_tracks = tracks.json()
    return json_tracks

if __name__=='__main__':
    app.run(host="0.0.0.0", debug=True)
