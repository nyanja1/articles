from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    conn.close()

    # Seed authors
    author1 = Author("Alice Smith")
    author2 = Author("Bob Jones")
    
    # Seed magazines
    mag1 = Magazine("Tech Trends", "Technology")
    mag2 = Magazine("Health Weekly", "Health")
    
    # Seed articles
    author1.add_article(mag1, "AI Revolution")
    author1.add_article(mag2, "Healthy Living")
    author2.add_article(mag1, "Quantum Computing")
    author2.add_article(mag1, "Blockchain Basics")

if __name__ == "__main__":
    seed_database()