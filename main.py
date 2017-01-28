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
import webapp2
import cgi
import re


def validateUsername(username):
    user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    print user_re.match(username)
    return user_re.match(username)


def validatePassword(password):
    password_re = re.compile(r"^.{3,20}$")
    return  password_re.match(password)


def validateEmail(email):
    email_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")
    return email_re.match(email)

def renderForm(error):
    fopen = "<form action='.' method='post'>"
    unamein = "<label>Username: </label><input type='text' name='username'/><br>"
    pwordin = "<label>Password: </label><input type='text' name='password'/><br>"
    vpwordin = "<label>Verify Password: </label><input type='text' name='vpassword'/><br>"
    emailin = "<label>Email: </label><input type='text' name='email'/><br>"
    subin = "<input type='submit' value='Submit'>"
    fclose = "</form>"
    content = fopen + unamein + pwordin + vpwordin + emailin + subin + fclose
    return content


class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = renderForm("")
        self.response.write(content)



    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        vpassword = self.request.get('vpassword')
        email = self.request.get('email')

        error = ""

        if validateUsername(username) == None:
            error += "Username Invalid  "

        if validatePassword(password) == None:
            error += "Invalid Password  "
        elif password != vpassword:
            error += "Passwords do not match  "

        if validateEmail(email) == None:
            error += "Invalid Email Address  "



        self.response.write(error)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
