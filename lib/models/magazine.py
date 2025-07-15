from lib.db.connection import get_connection

class Magazine:
    def __init__(self, name, category, id=None):
        self._id = id
        self._name = None
        self._category = None
        self.name = name  #validation
        self.category = category
        if id is None:
            self.save()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self._id is None:
            cursor.execute(
                "INSERT INTO magazines (name, category) VALUES (?, ?)",
                (self.name, self.category)
            )
            self._id = cursor.lastrowid
            conn.commit()
        else:
            cursor.execute(
                "UPDATE magazines SET name = ?, category = ? WHERE id = ?",
                (self.name, self.category, self.id)
            )
            conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(row['name'], row['category'], row['id']) if row else None

    def articles(self):
        from lib.models.article import Article
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Article(row['title'], row['author_id'], row['magazine_id'], row['id']) for row in rows]

    def contributors(self):
        from lib.models.author import Author
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT DISTINCT a.* FROM authors a
            JOIN articles art ON a.id = art.author_id
            WHERE art.magazine_id = ?
            """,
            (self.id,)
        )
        rows = cursor.fetchall()
        conn.close()
        return [Author(row['name'], row['id']) for row in rows]

    def article_titles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM articles WHERE magazine_id = ?", (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [row['title'] for row in rows]

    def contributing_authors(self):
        from lib.models.author import Author
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT a.* FROM authors a
            JOIN articles art ON a.id = art.author_id
            WHERE art.magazine_id = ?
            GROUP BY a.id, a.name
            HAVING COUNT(art.id) > 2
            """,
            (self.id,)
        )
        rows = cursor.fetchall()
        conn.close()
        return [Author(row['name'], row['id']) for row in rows]

    @classmethod
    def top_publisher(cls):
        from lib.models.magazine import Magazine
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT m.*, COUNT(a.id) as article_count
            FROM magazines m
            LEFT JOIN articles a ON m.id = a.magazine_id
            GROUP BY m.id, m.name, m.category
            ORDER BY article_count DESC
            LIMIT 1
            """
        )
        row = cursor.fetchone()
        conn.close()
        return cls(row['name'], row['category'], row['id']) if row else None