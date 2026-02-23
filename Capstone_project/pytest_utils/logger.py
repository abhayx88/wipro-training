import logging


LOGGER = logging.getLogger("pytest_steps")


def log_step(message: str) -> None:
    LOGGER.info(message)
