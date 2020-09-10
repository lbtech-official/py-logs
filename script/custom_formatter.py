import logging
from json_log_formatter import JSONFormatter


class CustomJSONFormatter(JSONFormatter):
    def __init__(self, app: str, *args, **kwargs):
        self.app = app
        super().__init__(*args, **kwargs)

    def json_record(self, message: str, extra: dict, record: logging.LogRecord) -> dict:
        extra['app'] = self.app
        extra['message'] = message

        # Include builtins
        extra['level'] = record.levelname
        extra['name'] = record.name
        extra['filename'] = record.filename
        extra['funcName'] = record.funcName

        if record.exc_info:
            extra['exc_info'] = self.formatException(record.exc_info)

        return extra
