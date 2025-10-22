import logging

logging.basicConfig(
    filename="data.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    force=True
)

logger = logging.getLogger("app")


def write_info(text: str):
    logger.info(text)


def write_warning(text: str):
    logger.warning(text)


def write_error(text: str):
    logger.error(text)
