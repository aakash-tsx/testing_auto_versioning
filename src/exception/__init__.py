import sys
import logging


def get_error_details(error: Exception) -> str:
    """
    Extracts detailed error information including file name, line number, and the error message.

    :param error: The exception that occurred.
    :return: A formatted error message string.
    """
    exc_type, _, exc_tb = sys.exc_info()

    if exc_tb is None:
        return f"Exception: {error}"  # Handles cases where traceback is not available

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = (
        f"Error in script: [{file_name}] at line [{line_number}]: {str(error)}"
    )

    logging.error(error_message)  # Log error
    return error_message


class CustomException(Exception):
    """
    Custom exception class for handling errors in the application.
    """

    def __init__(self, error: Exception):
        """
        Initializes the CustomException with a detailed error message.

        :param error: The exception instance.
        """
        super().__init__(str(error))  # Base exception message
        self.error_message = get_error_details(error)

    def __str__(self) -> str:
        """
        Returns the formatted error message.
        """
        return self.error_message
