
# Articles Code Challenge

A Python application modeling the relationships between Authors, Articles, and Magazines using raw SQL and SQLite. This project implements an object-relational design fulfilling the requirements of the Object Relations Code Challenge.

---

## Overview

This project models Authors, Articles, and Magazines with the following relationships:

- An Author can write many Articles.
- A Magazine can publish many Articles.
- Articles belong to one Author and one Magazine.
- Author and Magazine have a many-to-many relationship through Articles.

Implemented with Python classes using raw SQL queries, transaction handling, and comprehensive tests. Optimized for macOS High Sierra compatibility.

---

## Features

- **Database Schema**: Tables for authors, magazines, and articles with foreign key constraints.
- **Model Classes**:
  - **Author**: Save, find by ID/name, list articles, magazines, topic areas, and add articles.
  - **Article**: Save and find by ID with title validation.
  - **Magazine**: Save, find by ID, list articles, contributors, article titles, and authors with >2 articles; includes `top_publisher` class method.
- **SQL Queries**: Efficient, parameterized queries to prevent SQL injection.
- **Transaction Handling**: Atomic operations for adding authors and articles.
- **Testing**: Comprehensive pytest coverage for all models and relationships.
- **Version Control**: Git repository with incremental, descriptive commits.

---

## Project Structure

```

code-challenge/
├── lib/
│   ├── models/
│   │   ├── **init**.py
│   │   ├── author.py
│   │   ├── article.py
│   │   └── magazine.py
│   ├── db/
│   │   ├── **init**.py
│   │   ├── connection.py
│   │   ├── schema.sql
│   │   └── seed.py
│   ├── controllers/
│   │   └── **init**.py
│   ├── debug.py
│   └── **init**.py
├── tests/
│   ├── **init**.py
│   ├── test\_author.py
│   ├── test\_article.py
│   └── test\_magazine.py
├── scripts/
│   ├── setup\_db.py
│   └── run\_queries.py
├── README.md
└── .gitignore

````

---

## Setup Instructions

### Prerequisites

- Python 3.6+ (compatible with macOS High Sierra)
- pip
- Git

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/articles-challenge.git
   cd articles-challenge
````

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install pytest
   ```

4. Initialize the database:

   ```bash
   python scripts/setup_db.py
   ```

5. (Optional) Seed the database:

   ```bash
   python lib/db/seed.py
   ```

6. Run tests:

   ```bash
   pytest
   ```

7. Start interactive debugging:

   ```bash
   python lib/debug.py
   ```

---

## Usage Example

```python
from lib.models.author import Author
from lib.models.magazine import Magazine

author = Author("Alice Smith")
mag = Magazine("Tech Trends", "Technology")
author.add_article(mag, "AI Revolution")

print([a.title for a in author.articles()])
print([m.name for m in mag.contributors()])
print(Magazine.top_publisher().name)
```


## Dev
Elvis Amonde
