import csv
from interface.controller.DTOs.BookDTO import BookDTO
from utils.logger import get_logger

logger = get_logger(__name__)

def generate_books_csv_use_case(books: list[BookDTO], filepath: str):
    """
    Generates a CSV file containing book information.

    This function takes a list of BookDTO objects and writes their details 
    into a CSV file at the specified filepath. Each row in the CSV file 
    corresponds to a book, containing its title, author, publisher, and image.

    Args:
        books (list[BookDTO]): A list of BookDTO objects containing book details.
        filepath (str): The path where the CSV file will be created.

    Raises:
        IOError: If the file cannot be opened or written to.
    """

    logger.info("Iniciando a criação do CSV.")
    with open(filepath, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Author", "Publisher", "Image"])
        for book in books:
            writer.writerow([book.title, book.author, book.publisher, book.image])
    
    logger.info(f"Arquivo CSV criado com sucesso (path: {filepath}).")
