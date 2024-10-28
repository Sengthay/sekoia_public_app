from sekoia_automation.module import Module
from testrequest_modules.models import TestrequestModuleConfiguration


class TestrequestModule(Module):
    configuration: TestrequestModuleConfiguration
