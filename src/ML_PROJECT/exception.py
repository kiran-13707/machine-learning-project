import sys

def getErrorDetails(error, error_Details: sys):
    _, _, tb_obj=error_Details.exc_info()
    Line_no=tb_obj.tb_lineno
    File_name=tb_obj.tb_frame.f_code.co_filename

    Error_msg=f"Error occurred in File name :- {File_name}, Error occurred in Line number :- {Line_no}, error message :- {error} "
    return Error_msg

class customeException(Exception):
    def __init__(self, error, error_msg : sys):
        super().__init__(error_msg)
        self.error_msg = getErrorDetails(error, error_msg)

    def __str__(self):
        return self.error_msg


