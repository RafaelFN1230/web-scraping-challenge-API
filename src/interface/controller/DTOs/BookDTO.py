from dataclasses import dataclass

@dataclass
class BookDTO:
    image: str
    title: str
    author: str
    publisher: str

@dataclass
class BookStoreDataDTO:
    books: list[BookDTO]
