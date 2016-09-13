# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#!/usr/bin/env python
#@PydevCodeAnalysisIgnore

from __builtin__ import setattr

import endpoints
from protorpc import remote
from protorpc import message_types
from models import HelloForm
from models import  SEAFARERS_REQUEST
from models import  SEAFARERS_RESPONSE

EMAIL_SCOPE = endpoints.EMAIL_SCOPE
API_EXPLORER_CLIENT_ID = endpoints.API_EXPLORER_CLIENT_ID
WEB_CLIENT_ID = '209444890233-mks99bqshn12ttu7slvrgbnoh1dbocpk.apps.googleusercontent.com'
@endpoints.api(name='seafarers', version='v1', 
    allowed_client_ids=[WEB_CLIENT_ID, API_EXPLORER_CLIENT_ID],
    scopes=[EMAIL_SCOPE])
class SeafarersApi(remote.Service):
    """Conference API v0.1"""
    def _sayHello(self, request=None):
        hello = HelloForm()
        setattr(hello, 'hello', 'Ahoj')
        return hello
    @endpoints.method(message_types.VoidMessage, HelloForm,
                      path='hello', http_method='GET', name='sayHello')
    def sayHello(self, request):
        return self._sayHello(request)
    
    def _getAbolition(self, request):
        response_message = 'Ahoj ' +  str(getattr(request, 'first_name')) + ' '  + str(getattr(request, 'last_name'))
        response = SEAFARERS_RESPONSE()
        setattr(response, 'message', response_message)
        return response
    
    @endpoints.method(SEAFARERS_REQUEST, SEAFARERS_RESPONSE, name='getAbolition', path='getabolition', http_method='POST')
    def getAbolition(self, request):
        return self._getAbolition(request)
        

api = endpoints.api_server([SeafarersApi]) # register API
