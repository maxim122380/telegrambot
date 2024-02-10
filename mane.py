import sqlite3

class Database:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("base.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
    
    def get_users(self, id):
        self.cursor.execute(f"SELECT user_name FROM users WHERE id={id}")
        return self.cursor.fetchone()[0]
    
    def regitser(self, name):
        self.cursor.execute(f"INSERT INTO users VALUES (?)", (name,))
        self.conn.commit()
        return True
    
db = Database()
print(db.regitser(""))