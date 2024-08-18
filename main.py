from library import Library

path = "./Library_8_18_2024.xml"

library = Library(path)

for song in library.parsexml():

    print(f'Song: {song.name}, Artist: {song.artist}')