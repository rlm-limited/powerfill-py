



class OCPPTagAlreadyExistsError(Exception):
    pass

class OCPPTagDoesNotExistError(Exception):
    pass


class ChargeBoxDoesNotExistError(Exception):
    pass

class ChargeBoxConnectorDoesNotExistError(Exception):
    pass

class ChargeBoxConnectorNotAvailableError(Exception):
    pass

class InvalidWebRequestReturnCode(Exception):
    pass

class HTTPConnectionError(Exception):
    pass

class RequestTimeoutError(Exception):
    pass

class UnableToFindTransactionError(Exception):
    pass

class RemoteStartFailedError(Exception):
    pass

class RemoteStopFailedError(Exception):
    pass