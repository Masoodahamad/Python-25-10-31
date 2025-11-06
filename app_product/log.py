import logging

#setup
logging.basicConfig(filename='product_app_logs.log',
    level=logging.DEBUG,
    format = "%(asctime)s [%(levelname)s] %(message)s"
)