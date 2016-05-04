#!/usr/bin/python

from flask import Flask, jsonify, render_template, request
import jinja2
import os
import spotipy
#from urllib.parse import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from apiclient.discovery import build
from apiclient.errors import HttpError
import json
from oauth2client.tools import argparser
import argparse
import sys
import pprint


app = Flask(__name__)
app.debug = True

spotify = spotipy.Spotify()

@app.route('/Youtify', methods=['POST','GET'])
def get_top_ten():
    mysearch = "Drake"
    if request.method == 'POST':
        rawsearch = request.form['searchstr']
        mysearch = rawsearch + " music video"

        spotify_results = spotify.search(q='artist:' + rawsearch, type='artist')
        items = spotify_results['artists']['items']
#        if len(items) > 0:
#            artist = items[0]
#            Artist_URL = artist['name'], artist['images'][0]['url']
#            return Artist_URL
#        top_track_list = spotify.artist_top_tracks(Artist_URL)
#        x = ""
#        for track in top_track_list['tracks'][:1]:
#            track_name = track['name']
#            x = x + "</br>" + track_name
#            print(x)


#            return track_name

#        if len(mysearch) > 1:
#            urn = mysearch[1]
#        else:
#            urn = 'spotify:artist:3TVXtAsR1Inumwj472S9r4'

#        sp = spotipy.Spotify()
#        response = sp.artist_top_tracks(urn)

#        for track in response['tracks']:
#            return(track['name'])

#        mysearch = track_name + "music video"

    argparser = argparse.ArgumentParser()
    print(mysearch)
    argparser.add_argument("--q", help="Search term", default=mysearch)
    argparser.add_argument("--max-results", help="Max results", default=1)
    args = argparser.parse_args()

    name = "Youtify"
    try:
        mysearchreturn = youtube_search(args)
    except HttpError as e:
        print("An HTTP error %d occured:\n%s" % (e.resp.status, e.content))
    if mysearchreturn == False:
      return render_template('Youtify.html', name=name)

    return render_template('Return.html', name=name, myvidid=json.dumps(mysearchreturn), myheight='320')

DEVELOPER_KEY = "AIzaSyARem1g5GfmB8LxUQz8V6r_HR2lo-gUNXg"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified query term.

    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        maxResults=options.max_results
    ).execute()

    videos = []
    channels = []
    playlists = []

    #print(search_response.get("items", [])[1])

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    myvid = None
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            if myvid == None:
                myvid = search_result["id"]["videoId"]
            videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                        search_result["id"]["videoId"]))
        elif search_result["id"]["kind"] == "youtube#channel":
            channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                        search_result["id"]["channelId"]))
        elif search_result["id"]["kind"] == "youtube#playlistl":
            playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                        search_result["id"]["playlistId"]))

    if myvid != None:
        return myvid
    else:
        return False

    print("Videos:\n", "\n".join(videos), "\n")

if __name__ == "__main__":
    app.run()


