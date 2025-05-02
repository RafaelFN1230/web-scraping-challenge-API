from interface.controller.main_controller import MainController

if __name__ == "__main__":
    base_url = "https://demoqa.com"
    controller = MainController(base_url=base_url)
    controller.execute(csv_path="output/books_api.csv")
