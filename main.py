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

def renderForm(error_list, username, email):
    fopen = "<form action='.' method='post'>"
    unamein = "<label>Username: </label><input type='text' name='username' value='"+username+"'/>"
    if error_list[0] == True:
        unamein += "  Username Invalid"
    pwordin = "<br><label>Password: </label><input type='text' name='password'/>"
    if error_list[1] == True:
        pwordin += "  Invalid Password"
    vpwordin = "<br><label>Verify Password: </label><input type='text' name='vpassword'/>"
    if error_list[2] == True:
        vpwordin += "  Passwords do not match"
    emailin = "<br><label>Email: </label><input type='text' name='email' value='"+email+"'/>"
    if error_list[3] == True:
        emailin += "  Invalid Email Address"
    subin = "<br><input type='submit' value='Submit'>"
    fclose = "</form>"
    content = fopen + unamein + pwordin + vpwordin + emailin + subin + fclose
    return content


class MainHandler(webapp2.RequestHandler):
    def get(self):
        error_list = [False, False, False, False]
        username = ''
        email = ''
        content = renderForm(error_list, username, email)
        self.response.write(content)



    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        vpassword = self.request.get('vpassword')
        email = self.request.get('email')


        error_list = [False, False, False, False]

        if validateUsername(username) == None:
            error_list[0] = True
            username = ""
        else:
            error_list[0] = False
            #incl_user = True
            #username = cgi.escape(username)

        if validatePassword(password) == None:
            error_list[1] = True
        else:
            error_list[1] = False

        if password != vpassword:
            error_list[2] = True
        else:
            error_list[2] = False


        if validateEmail(email) == None:
            error_list[3] = True
            email = ""
        else:
            error_list[3] = False
            #incl_email = True
            #email = cgi.escape(email)

        if not any(error_list):
            content = 'Success!'
        else:
            content = renderForm(error_list, username, email)


        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
