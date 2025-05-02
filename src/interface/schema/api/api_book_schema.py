from dataclasses import dataclass

@dataclass
class BookSchema:
    isbn: str
    title: str
    subTitle: str
    author: str
    publish_date: str
    publisher: str
    pages: int
    description: str
    website: str