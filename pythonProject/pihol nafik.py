import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs_pihol nafik_1.log",
                    filemode='a',
                    format="we have pisun: %(asctime)s%(levelname)s - %(message)s")


try:
    print(10/0)
except Exception:
    logging.exception("exception")
