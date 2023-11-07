python
class MIDIWORX:
    def __init__(self, db_name):
        self.conn = self.create_db_connection(db_name)
        self.cur = self.conn.cursor()

    def create_db_connection(self, db_name):
        conn = None
        try:
            conn = sqlite3.connect(db_name)  # Creates SQLite database in memory if it doesn't exist
        except Exception as e:
            logging.error(f"Error creating DB connection: {str(e)}")
        return conn

    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS music_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                artist TEXT NOT NULL,
                song_name TEXT NOT NULL,
                popularity INTEGER NOT NULL,
                feature1 FLOAT, feature2 FLOAT, feature3 FLOAT,
                ...
                ...[other columns]...
                ...
                featureN FLOAT,
                UNIQUE(artist, song_name));
            """
        try:
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error creating Table: {str(e)}")

    def insert_music_data(self, music_batch):
        query = """
            INSERT OR IGNORE INTO music_data(
                artist, song_name, popularity, feature1, feature2, feature3, ..., featureN)
            VALUES(?,?,?,?,?,?,...,?);"""
        try:
            self.cur.executemany(query, music_batch)
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error inserting data: {str(e)}")

    # ... (rest of your code)

# Create an instance of MIDIWORX
app = MIDIWORX("music_data.db")

# THIS PART TO BE RAN ONLY ONCE BY ADMIN
# if table does not exist, create table and insert data
app.create_table()
music_batch = []  # replace with your actual data
app.insert_music_data(music_batch)

# Do other things
app.train_model()