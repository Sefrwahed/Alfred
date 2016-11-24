from wit import Wit
import json

# Local includes
import alfred.alfred_globals as ag
import alfred.logger as logger

_wit = Wit(access_token=ag.WIT_TOKEN)

class WitWrapper:
    def send(self, msg):
        self.response = _wit.message(msg)
        logger.info(self.response)

    def intent(self):
        return self.response["entities"]["intent"][0]["value"]
