import logging

from ._get_type import getType
from openhivenpy.gateway.http import HTTP

logger = logging.getLogger(__name__)

__all__ = ['Feed']


class Feed:
    """`openhivenpy.types.Feed`
    
    Data Class for a users's Feed
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Represents the feed that is displayed on Hiven
    
    Attributes
    ~~~~~~~~~~
    
    """
    def __init__(self, data: dict, http: HTTP):
        self._http = http
