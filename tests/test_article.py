import pytest
from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine
from scripts.setup_db import setup_database

@pytest.fixture
def setup_db():
    setup_database()
    yield

def test_article_create(setup_db):
    author = Author("Test Author")
    mag = Magazine("Test Mag", "Tech")
    article = Article("Test Article", author.id, mag.id)
    assert article.id is not None
    assert article.title == "Test Article"