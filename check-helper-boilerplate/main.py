#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import os
import webapp2
import jinja2
import logging
from google.appengine.ext import ndb
import json

JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# This handler receives the post request when the user hits the submit button.
class ReceiptHandler(webapp2.RequestHandler):
    def post(self):
        # We handle a post request because the form method
        # is "POST". We handle it in this handler because the "action" field
        # specifies that it should go to the /register_check handler.
        tax_rate = float(self.request.get('tax_rate'))
        service_rate = float(self.request.get('service_rate'))
        # Compute the subtotal.
        # ...

        # Tax and service.
        # ...

        # The reply is ready. We must send it back. We did not need to Compute
        # it in the backend, since we could do it all in JS. We do it this way
        # to demonstrate the AJAX paradigm.
        # Prepare the dictionary to send back.
        # ...

        # Replace the placeholders in the receipt template with the values
        # computed here.
        template = JINJA_ENV.get_template('templates/receipt.html')
        self.response.write( "Here shall be the answer" )

# This is the handler that receives the initial get request, and sends the html
# page.
class MainHandler(webapp2.RequestHandler):
    def get(self):
        # All we need to do is really just displaying the page once.
        # From now on everything will be client-side, at least for now.
        template = JINJA_ENV.get_template('templates/check_helper.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/register_check', ReceiptHandler),
], debug=True)
