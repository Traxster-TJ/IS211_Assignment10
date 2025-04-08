-- Create the artists table
CREATE TABLE artists (
    artist_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

-- Create the albums table with a foreign key reference to artists
CREATE TABLE albums (
    album_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    artist_id INTEGER NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);

-- Create the songs table with a foreign key reference to albums
CREATE TABLE songs (
    song_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    album_id INTEGER NOT NULL,
    track_number INTEGER NOT NULL,
    length_seconds INTEGER NOT NULL,
    FOREIGN KEY (album_id) REFERENCES albums(album_id)
);
