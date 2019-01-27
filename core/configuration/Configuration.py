from core.util.error_factory.ConfigErrors import ConfigAttributeDoesNotExist
import json
# BASE CLASS FOR CONFIGURATION OBJECTS

class Configuration():

    def __init__(self,file,requiredAttributes,defaultAttributes):
        self._required_attributes=requiredAttributes
        self._defaults=defaultAttributes
        self.config_file=file

        self.default_output_header="-----------------"
        self.dev_mode_enabled=True


    def initialize_config(self):
        self._read_config(self.config_file)

    def _read_config(self,file):
        self._initialize_object(json.load
                                (open(file)))
        self._check_defaults()

    def _initialize_object(self,json):

        for config_item in json.keys():
            if self._attribute_exists(json,config_item):
                 setattr(self,config_item,json[config_item])

            elif self._is_default(config_item):
                setattr(self,config_item,self._grab_default(config_item))

            elif self._is_attribute_required(config_item):
                raise ConfigAttributeDoesNotExist(config_item)

    def _check_defaults(self):
        for default in self._defaults.keys():
            if hasattr(self,default) and getattr(self,default) is not None:
                continue
            else:
                setattr(self,default,self._defaults[default])

    def _attribute_exists(self,obj,key):
        if key in obj.keys():
            return True
        else:
            return False

    def _is_attribute_required(self,key):
        if key in self._required_attributes:
            return True

    def _is_default(self,key):
        if key in self._defaults.keys():
            return True
        else:
            return False

    def _grab_default(self,key):
        return self._defaults[key]

