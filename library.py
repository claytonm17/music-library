import xml.etree.ElementTree as ET

path = "./Library_8_18_2024.xml"

class Song:

    # All values given from itunes
    def __init__(
            self,
            key = None,
            trackID = None,
            name = None,
            artist = None,
            album_artist = None,
            composer = None,
            album = None,
            genre = None,
            kind = None,
            size = None,
            total_time = None,
            disc_num = None,
            disc_count = None,
            track_num = None,
            track_count = None,
            year = None,
            date_modified = None,
            date_added = None,
            bit_rate = None,
            sample_rate = None,
            play_count = None,
            play_date = None,
            play_date_utc = None,
            release_date = None,
            artwork_count = None,
            sort_artist = None,
            sort_name = None,
            persistent_ID = None,
            track_type = None,
            matched = False,
            ):
        self.key = key,
        self.trackID = trackID
        self.name = name
        self.artist = artist
        self.album_artist = album_artist
        self.composer = composer
        self.album = album
        self.genre = genre
        self.kind = kind
        self.size = size
        self.total_time = total_time
        self.disc_num = disc_num
        self.disc_count = disc_count
        self.track_num = track_num
        self.track_count = track_count
        self.year = year
        self.date_modified = date_modified
        self.date_added = date_added
        self.bit_rate = bit_rate
        self.sample_rate = sample_rate
        self.play_count = play_count
        self.play_date = play_date
        self.play_date_utc = play_date_utc
        self.release_date = release_date
        self.artwork_count = artwork_count
        self.sort_artist = sort_artist
        self.sort_name = sort_name
        self.persistent_ID = persistent_ID
        self.track_type = track_type
        self.matched = matched

class Library:

    def __init__(self, xmlfile_path):
        self.tree = ET.parse(xmlfile_path)

    def parsexml(self):
        root = self.tree.getroot()
        songs = root.find("./dict/dict")

        master_list = []
        
        for song in songs:
            if song.tag == "dict":
                metadata = {}
                current_key = None
                for item in song:
                    if item.tag == "key":
                        current_key = item.text
                    else:
                        if current_key:
                            if item.tag == "integer":
                                metadata[current_key] = int(item.text)
                            elif item.tag == "string":
                                metadata[current_key] = item.text
                            elif item.tag == "date":
                                metadata[current_key] = item.text
                            elif item.tag == "true":
                                metadata[current_key] = True
                            elif item.tag == "false":
                                metadata[current_key] = False

                song_obj = Song(
                    key = metadata.get('Track ID'),
                    trackID = metadata.get('Track ID'),
                    name = metadata.get('Name'),
                    artist = metadata.get('Artist'),
                    album_artist = metadata.get('Album Artist'),
                    composer = metadata.get('Composer'),
                    album = metadata.get('Album'),
                    genre = metadata.get('Genre'),
                    kind = metadata.get('Kind'),
                    size = metadata.get('Size'),
                    total_time = metadata.get('Total Time'),
                    disc_num = metadata.get('Disc Number'),
                    disc_count = metadata.get('Disc Count'),
                    track_num = metadata.get('Track Number'),
                    track_count = metadata.get('Track Count'),
                    year = metadata.get('Year'),
                    date_modified = metadata.get('Date Modified'),
                    date_added = metadata.get('Date Added'),
                    bit_rate = metadata.get('Bit Rate'),
                    sample_rate = metadata.get('Sample Rate'),
                    play_count = metadata.get('Play Count'),
                    play_date = metadata.get('Play Date'),
                    play_date_utc = metadata.get('Play Date UTC'),
                    release_date = metadata.get('Release Date'),
                    artwork_count = metadata.get('Artwork Count'),
                    sort_artist = metadata.get('Sort Artist'),
                    sort_name = metadata.get('Sort Name'),
                    persistent_ID = metadata.get('Persistent ID'),
                    track_type = metadata.get('Track Type'),
                    matched = metadata.get('Matched', False)
                )

                master_list.append(song_obj)

        return master_list
                

library = Library(path)

for song in library.parsexml():

    print(f'Song: {song.name}, Artist: {song.artist}')