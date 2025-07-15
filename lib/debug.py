from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from scripts.setup_db import setup_database

if __name__ == "__main__":
    setup_database()
    print("Database seeded. Use Author, Magazine, Article classes to interact.")
    # Example usage
    author = Author.find_by_name("Alice Smith")
    print(f"Author: {author.name}")
    print("Articles:", [a.title for a in author.articles()])
    print("Magazines:", [m.name for m in author.magazines()])