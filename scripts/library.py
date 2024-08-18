import xml.etree.ElementTree as ET
import pandas as pd

class Library:

    def __init__(self, xmlfile_path):
        self.tree = ET.parse(xmlfile_path)
        self.metadata = None
    
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

                song_obj = {
                    "trackID": metadata.get('Track ID'),
                    "name": metadata.get('Name'),
                    "artist": metadata.get('Artist'),
                    "album_artist": metadata.get('Album Artist'),
                    "composer": metadata.get('Composer'),
                    "album": metadata.get('Album'),
                    "genre": metadata.get('Genre'),
                    "kind": metadata.get('Kind'),
                    "size": metadata.get('Size'),
                    "total_time": metadata.get('Total Time'),
                    "disc_num": metadata.get('Disc Number'),
                    "disc_count": metadata.get('Disc Count'),
                    "track_num": metadata.get('Track Number'),
                    "track_count": metadata.get('Track Count'),
                    "year": metadata.get('Year'),
                    "date_modified": metadata.get('Date Modified'),
                    "date_added": metadata.get('Date Added'),
                    "bit_rate": metadata.get('Bit Rate'),
                    "sample_rate": metadata.get('Sample Rate'),
                    "play_count": metadata.get('Play Count'),
                    "play_date": metadata.get('Play Date'),
                    "play_date_utc": metadata.get('Play Date UTC'),
                    "release_date": metadata.get('Release Date'),
                    "artwork_count": metadata.get('Artwork Count'),
                    "sort_artist": metadata.get('Sort Artist'),
                    "sort_name": metadata.get('Sort Name'),
                    "persistent_ID": metadata.get('Persistent ID'),
                    "track_type": metadata.get('Track Type'),
                    "matched": metadata.get('Matched', False),
                }

                master_list.append(song_obj)

        self.metadata = master_list

    def export_csv(self):

        if not self.metadata:
            self.parsexml()
        
        df = pd.DataFrame(self.metadata)

        df.to_csv("../metadata.csv")

        print(f'Successfully exported {len(self.metadata)} songs to csv')