class ConfigAttributeDoesNotExist(Exception):
    def __init__(self,Attribute):
        Exception.__init__(self,f"{Attribute} is required!!")

class ConfigurationMethodNotImplemented(Exception):
    def __init__(self,method):
        Exception.__init__(self,f"{method} method must be implemented!")
