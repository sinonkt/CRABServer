"""
Important exceptions:
* StopHandler: raised in an action when we want a gentle exit.
    No notification about the error will be sent to the REST
* TaskWorkerException: raise in Actions when there is an error
    and we want to notify it to the REST (no stacktraces or
    other information will be added to the message).
    If in an Action a different exception is raised a lot of
    stacktrace and other info will be added.
* WorkerHandlerException: Used internally in the action handler
    to notify the worker about the type of error (add or not add
    the stacktrace to the REST error message?).
"""


class TaskWorkerException(Exception):
    """General exception to be returned in case of failures
       by the TaskWorker objects"""
    pass

class ConfigException(TaskWorkerException):
    """Returned in case there are issues with the input
       TaskWorker configuration"""
    exitcode = 4000

class StopHandler(TaskWorkerException):
    """Exception used in order to stop the handler from
       continuing to work the sequent actions.

       In other words, raised in actions to stop the Handler for further
       execution. Error handling is done in the action iself,
       and no notification will be sent to the REST.
    """
    exitcode = 6667

class PanDAException(TaskWorkerException):
    """Generic exception interacting with PanDA"""
    exitcode = 5000

class PanDAIdException(PanDAException):
    """Returned in case there are issues with the expected
       behaviour of PanDA id's (def, set)"""
    exitcode = 5001

class NoAvailableSite(PanDAException):
    """In case there is no site available to run the jobs
       use this exception"""
    exitcode = 5002

class WorkerHandlerException(TaskWorkerException):
    """Generic exception in case slave worker action
       crashes.

       Raised in Handler.py when we want the worker to
       propagate the error to the REST.
    """
    exitcode = 6666

