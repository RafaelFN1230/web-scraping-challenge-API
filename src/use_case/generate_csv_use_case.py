import csv
from interface.controller.DTOs.BookDTO import BookDTO
from utils.logger import get_logger
logger = get_logger(__name__)
def generate_books_csv_use_case(books: list[BookDTO], filepath: str):
    logger.info("Iniciando a criação do CSV.")
    with open(filepath, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Author", "Publisher", "Image"])
        for book in books:
            writer.writerow([book.title, book.author, book.publisher, book.image])
    
    logger.info(f"Arquivo CSV criado com sucesso (path: {filepath}).")
