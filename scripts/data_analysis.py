from library import Library

class Analysis:

    def __init__(self, metadata):
        self.metadata = metadata

    def composition_of_library(self):
        
        comp = {}
        total = 0

        for song in self.metadata:

            album_artist = song['album_artist']

            if album_artist not in comp:
                comp[album_artist] = 1
            
            else:
                comp[album_artist] += 1

            total += 1
        
        for artist,songs in comp.items():

            print(f'{artist}: {round(((songs/total) * 100), 2)}%')

lib = Library("../Library.xml")
lib.parsexml()
metadata = lib.metadata

analytics = Analysis(metadata)
'''
for data in analytics.metadata:

    print(data['artist'])

print(len(analytics.metadata))
'''
analytics.composition_of_library()