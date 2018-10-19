from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

import json

class ActionSendMail(Action):
        def name(self):
                return 'action_send_mail'

        def run(self, dispatcher, tracker, domain):
                
                dispatcher.utter_message("-----")
                return [SlotSet('email','abc@def.com')]
