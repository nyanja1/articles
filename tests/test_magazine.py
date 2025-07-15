import pytest
from lib.models.magazine import Magazine
from lib.models.author import Author
from scripts.setup_db import setup_database

@pytest.fixture
def setup_db():
    setup_database()
    yield

def test_magazine_create(setup_db):
    mag = Magazine("Test Mag", "Tech")
    assert mag.id is not None
    assert mag.name == "Test Mag"
    assert mag.category == "Tech"

def test_magazine_contributors(setup_db):
    mag = Magazine.find_by_id(1)
    contributors = mag.contributors()
    assert len(contributors) >= 2