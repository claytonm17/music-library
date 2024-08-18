class Song:
    
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