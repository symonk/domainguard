import typing
from dataclasses import dataclass
import whois


@dataclass(frozen=True)
class WhoIsResponse:
    """WhoIsResponse encapsulates meta data for a domain"""
    creation_date: str
    expiration_date: str
    updated_date: str
    domain: str
    nameservers: typing.List[str]
    

class WhoisService:
    
    def __init__(self) -> typing.NoReturn:
        ...

    def whois(self, domain: str) -> typing.Dict[typing.Any, typing.Any]:
        return whois.whois(domain)