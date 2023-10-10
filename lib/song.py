from config import CONN, CURSOR

class Song:

    def __init__(self, name, album) -> None:
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            );
        """
        CURSOR.execute(sql)
        CONN.commit() 

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()  
        return song

    def save(self):
        sql = f"""
            INSERT INTO songs (name, album)
            VALUES (?, ?);
        """
        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()  

    
        CURSOR.execute('SELECT id FROM songs WHERE name=? AND album=?', (self.name, self.album))
        row = CURSOR.fetchone()
        if row:
            self.id = row[0] 
        return self
