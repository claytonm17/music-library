import pandas as pd

class Analysis:

    def __init__(self):
        self.data = pd.read_csv("../metadata.csv")

    def composition_of_library(self):
        
        comp = {}
        total = 0

        for artist in self.data["album_artist"]:

            if artist not in comp.keys():
                comp[artist] = 1
            
            else:
                comp[artist] += 1

            total += 1
        
        for artist,songs in comp.items():

            print(f'{artist}: {round(((songs/total) * 100), 2)}%')

    def find_missing_artist(self):

        for artist in self.data["album_artist"]:

            if artist == "NaN":

                print(artist)


analytics = Analysis()
#print(analytics.composition_of_library())
print(analytics.find_missing_artist())