import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from scripts.setup_db import setup_database

@pytest.fixture
def setup_db():
    setup_database()
    yield

def test_author_create(setup_db):
    author = Author("Test Author")
    assert author.id is not None
    assert author.name == "Test Author"

def test_author_articles(setup_db):
    author = Author.find_by_name("Alice Smith")
    articles = author.articles()
    assert len(articles) >= 2
    assert any(article.title == "AI Revolution" for article in articles)

def test_author_magazines(setup_db):
    author = Author.find_by_name("Alice Smith")
    magazines = author.magazines()
    assert len(magazines) >= 2
    assert any(mag.name == "Tech Trends" for mag in magazines)