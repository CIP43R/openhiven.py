import logging
import sys

import openhivenpy.Exception as errs
from openhivenpy.Gateway.http import HTTPClient
from ._get_type import getType

logger = logging.getLogger(__name__)

class Context():
    """`openhivenpy.Types.Context` 
    
    Data Class for a Command or Event Context
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    The class inherits all the avaible data from Hiven(attr -> read-only)!
    
    Returned with events, commands and HivenClient.on_ready()
    
    """
    def __init__(self, data: dict, http_client: HTTPClient):
        self._http_client = http_client