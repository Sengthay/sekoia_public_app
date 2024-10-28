from testrequest_modules import TestrequestModule

from testrequest_modules.trigger_new_entries import NewEntriesTrigger
from testrequest_modules.action_request import Request


if __name__ == "__main__":
    module = TestrequestModule()
    module.register(NewEntriesTrigger, "NewEntriesTrigger")
    module.register(Request, "Request")
    module.run()
