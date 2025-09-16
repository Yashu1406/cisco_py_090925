import logging
import json_log_formatter

formatter = json_log_formatter.JSONFormatter()

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger("hms_logger")
logger.addHandler(handler)
logger.setLevel(logging.INFO)