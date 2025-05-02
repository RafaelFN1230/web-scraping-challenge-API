from infrastructure.API.get_books import get_books
from interface.controller.DTOs.BookDTO import BookDTO, BookStoreDataDTO
from utils.logger import get_logger
logger = get_logger(__name__)
def get_books_use_case(base_url: str, token: str) -> BookStoreDataDTO:
    logger.info("Iniciando coleta de livros.")
    books_raw = get_books(base_url, token)
    
    logger.info("Convertendo livros para BookDTO.")

    books = [
            BookDTO(
                image="-",
                title=book.get("title"),
                author=book.get("author"),
                publisher=book.get("publisher")
            )
            for book in books_raw
        ]

    logger.info("Livros coletados com sucesso.")
    return books


