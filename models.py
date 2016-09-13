#!/usr/bin/env python

from protorpc import messages

class HelloForm(messages.Message):
    hello = messages.StringField(1)
    
class SEAFARERS_REQUEST(messages.Message):
    first_name = messages.StringField(1)
    last_name = messages.StringField(2)
    
class SEAFARERS_RESPONSE(messages.Message):
    message = messages.StringField(1)
