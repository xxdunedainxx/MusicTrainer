from core.configuration import Configuration


default_attributes={
    "log_file" : "./log/dump.log",
    "log_level" : "ALL",
    "logging_enabled" : True
}
required_attributes=[]

class ServiceConfig(Configuration):

    def __init__(self,file,requiredAttributes=[],defaultAttributes=default_attributes):
        self.svc_name="Default Service Config"
        self.svc_description="Some service description"
        self.svc_version="1.0"
        self.svc_namespace="google_transfer1_0.core.service"
        self.authors=["zach.mcfadden"]
        self.last_update="11/29/2018"

        super().__init__(file,requiredAttributes,defaultAttributes)
