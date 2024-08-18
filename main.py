from library import Library

path = "./Library_8_18_2024.xml"

library = Library(path)

library.parsexml_to_df()

def artist_count(library):
    # Argument is library object
    count = {}

    for song in library.metadata:

        if song.artist in count.keys():

            count[song.artist] += 1

        else:

            count[song.artist] = 1

    return count

# Export metadata to csv
import pandas as pd

metadata = library.metadata

df = pd.DataFrame(metadata)

df.to_csv("metadata.csv")