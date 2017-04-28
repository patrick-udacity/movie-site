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
import webapp2
import datetime

t = datetime.datetime.now()
currentTime = str(t)
form="""
<html><title>Lession 2</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<body>
<form method="post">

    <H1>Current Server Date/Time:""" + currentTime + """</H1>
    <label style="font-weight: bold">What is your birthdate? <input type="date" name="bday" placeholder="MM/DD/YYYY"></label><br>
    <input type="submit">
</form>
</body></html>
"""
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

    def post(self):
        self.response.out.write("Thanks. That is a valid day.")

app = webapp2.WSGIApplication([('/', MainPage)],
    debug=True)
