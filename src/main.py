from interface.controller.main_controller import MainController
from utils.logger import get_logger

logger = get_logger(__name__)

def main():
    logger.info("Iniciando aplicação.")
    base_url = "https://demoqa.com"
    controller = MainController(base_url=base_url)
    try:
        controller.execute(csv_path="output/books_api.csv")
    except Exception as e:
        logger.error(f"Erro: {e}", exc_info=True)
    logger.info("Processo finalizado com sucesso.")

if __name__ == "__main__":
    main()