import logging

from main import args


formatter = logging.Formatter(' %(name)s :: %(asctime)s :: %(levelname)-8s :: %(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename=args.log_path)
file_handler.setFormatter(formatter)


stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)




