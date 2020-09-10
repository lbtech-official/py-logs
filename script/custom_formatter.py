import logging
from json_log_formatter import JSONFormatter


class CustomJSONFormatter(JSONFormatter):
    def json_record(self, message: str, extra: dict, record: logging.LogRecord) -> dict:
        extra['message'] = message

        # Include builtins
        extra['level'] = record.levelname
        extra['name'] = record.name
        extra['filename'] = record.filename
        extra['funcName'] = record.funcName

        if record.exc_info:
            extra['exc_info'] = self.formatException(record.exc_info)

        return extra
