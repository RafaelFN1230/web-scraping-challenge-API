from infrastructure.API.get_books import get_books
from interface.controller.DTOs.BookDTO import BookDTO, BookStoreDataDTO

def get_books_use_case(base_url: str, token: str) -> BookStoreDataDTO:
    books_raw = get_books(base_url, token)
    for book in books_raw:
        book["image"] = "https://via.placeholder.com/150"
    return [
            BookDTO(
                image="-",
                title=book.get("title"),
                author=book.get("author"),
                publisher=book.get("publisher")
            )
            for book in books_raw
        ]



