import csv
from interface.controller.DTOs.BookDTO import BookDTO

def generate_books_csv_use_case(books: list[BookDTO], filepath: str):
    with open(filepath, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Author", "Publisher", "Image"])
        for book in books:
            writer.writerow([book.title, book.author, book.publisher, book.image])
