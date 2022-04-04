from typing import Any, Optional


def response_format(data: Optional[Any], message: Optional[str] = '', is_error: bool = False):
    return {
        'error': is_error,
        'message': message,
        'data': data
    }
