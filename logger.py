import logging

def setup_logger():

    logging.basicConfig(
        filename="test_execution.log",
        filemode="w",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger()