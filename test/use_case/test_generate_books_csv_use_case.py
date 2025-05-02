import pytest
import os
from unittest.mock import patch
import csv
from interface.controller.DTOs.BookDTO import BookDTO
from use_case.generate_csv_use_case import generate_books_csv_use_case

@pytest.fixture
def book_dto_list():
    """
    Fixture providing a list of BookDTO instances for testing the generate_books_csv_use_case
    function.

    The returned list contains two BookDTO instances with different title, author, publisher
    and image attributes. The list is meant to be used as input for the
    generate_books_csv_use_case function.

    Yields:
        A list of two BookDTO instances.
    """
    return [
        BookDTO(title="Book 1", author="Author 1", publisher="Publisher 1", image="image1.jpg"),
        BookDTO(title="Book 2", author="Author 2", publisher="Publisher 2", image="image2.jpg")
    ]

def test_generate_books_csv_use_case(book_dto_list):
    """
    Test the generate_books_csv_use_case function to ensure it creates a CSV file correctly.

    This test verifies that the CSV file is created with the correct header and that each
    row corresponds accurately to the book details provided in the book_dto_list. It checks
    for the existence of the file, validates the header, and confirms that the number of rows
    and their content match the expected values.

    Args:
        book_dto_list: A pytest fixture providing a list of BookDTO objects to be used for 
        generating the CSV file.

    Asserts:
        The CSV file is created and exists at the specified filepath.
        The CSV header matches the expected format ["Title", "Author", "Publisher", "Image"].
        The number of rows in the CSV matches the number of books in book_dto_list.
        Each row's content matches the corresponding BookDTO object's attributes.
    """

    filepath = "test_books.csv"

    generate_books_csv_use_case(book_dto_list, filepath)
    assert os.path.exists(filepath), f"Arquivo {filepath} não foi criado."

    with open(filepath, mode='r', encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        assert header == ["Title", "Author", "Publisher", "Image"], "Cabeçalho incorreto no CSV."

        rows = list(reader)
        assert len(rows) == len(book_dto_list), "Número de linhas no CSV não corresponde ao número de livros."
        for i, row in enumerate(rows):
            assert row[0] == book_dto_list[i].title, f"Erro no título do livro na linha {i+1}."
            assert row[1] == book_dto_list[i].author, f"Erro no autor do livro na linha {i+1}."
            assert row[2] == book_dto_list[i].publisher, f"Erro na editora do livro na linha {i+1}."
            assert row[3] == book_dto_list[i].image, f"Erro na imagem do livro na linha {i+1}."

    os.remove(filepath)