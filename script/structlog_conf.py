import inspect
import logging
import logging.config
import threading
import os
import structlog


# Additional logging processors (auto params in every log line).

def add_app_name(logger, log_method, event_dict):
    """Application name"""
    event_dict['app'] = 'myApp'
    return event_dict


def add_standard_logger_params(logger, log_method, event_dict):
    """
    It's not that easy to add standart logging params.
    https://github.com/hynek/structlog/issues/253
    """
    record = event_dict.get("_record")
    if record:
        event_dict["funcName"] = record.funcName
        event_dict["thread"] = record.thread
        event_dict["pathname"] = record.pathname
        event_dict["lineno"] = record.lineno
    else:
        frame, _module_str = structlog._frames._find_first_app_frame_and_name(
            additional_ignores=[__name__]
        )
        frame_info = inspect.getframeinfo(frame)
        event_dict["funcName"] = frame_info.function
        event_dict["thread"] = threading.get_ident()
        event_dict["pathname"] = frame_info.filename
        event_dict["lineno"] = frame_info.lineno
    event_dict["process"] = os.getpid()
    return event_dict


timestamper = structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S")


# Logging config
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.processors.JSONRenderer(),
            # "format": '%(process)d %(asctime)s %(name)s %(levelname)s %(message)s',  # doesn't work properly with JSON
        },
        "colored": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.dev.ConsoleRenderer(colors=True),
        },
    },
    "handlers": {
        "dev": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "colored",
        },
        "prod": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "json",
        },
    },
    "loggers": {
        "": {
            "handlers": ["dev"],
            "level": "DEBUG",
            "propagate": True,
        },
    }
}

logging.config.dictConfig(LOGGING)


# Structlog config
structlog.configure(
    processors=[
        add_app_name,
        add_standard_logger_params,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        timestamper,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)


def get_logger(name):
    """Public logging factory"""
    return structlog.get_logger(__name__)
