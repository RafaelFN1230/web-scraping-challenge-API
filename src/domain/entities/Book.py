class Book:
    def __init__(self, image: str, title: str, author: str, publisher: str):
        """
        Initialize a Book instance with image, title, author and publisher.

        Args:
            image (str): The image of the book.
            title (str): The title of the book.
            author (str): The author of the book.
            publisher (str): The publisher of the book.
        """
        self.image = image
        self.title = title
        self.author = author
        self.publisher = publisher
