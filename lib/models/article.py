from lib.db.connection import get_connection

class Article:
    def __init__(self, title, author_id, magazine_id, id=None):
        self._id = id
        self._title = None
        self.title = title  # Use setter for validation
        self._author_id = author_id
        self._magazine_id = magazine_id
        if id is None:
            self.save()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title must be a non-empty string")
        self._title = value

    @property
    def author_id(self):
        return self._author_id

    @property
    def magazine_id(self):
        return self._magazine_id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self._id is None:
            cursor.execute(
                "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                (self.title, self.author_id, self.magazine_id)
            )
            self._id = cursor.lastrowid
            conn.commit()
        else:
            cursor.execute(
                "UPDATE articles SET title = ?, author_id = ?, magazine_id = ? WHERE id = ?",
                (self.title, self.author_id, self.magazine_id, self.id)
            )
            conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(row['title'], row['author_id'], row['magazine_id'], row['id']) if row else None