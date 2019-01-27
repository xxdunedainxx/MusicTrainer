from core.configuration.ServiceConfig.ServiceConfig import ServiceConfig

class IService():

    def __init__(self, serviceConfig: ServiceConfig=None):
        pass

    def _validate_config(self,config: ServiceConfig):
        pass

    def _setup_service_logger(self):
        pass

    def service_output(self):
        pass

    def dispose(self):
        pass

    def credential(self):
        pass