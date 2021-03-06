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
<form method="post" action="/testform">

    <H1>Current Server Date/Time:""" + currentTime + """</H1>
    <label>Hello from Patrick to Udacity:<br><input name="q"><input type="submit"></label>
</form>
"""
class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/html'
        self.response.write(form)

class TestHandler(webapp2.RequestHandler):
    def post(self):
        q=self.request.get("q")
        self.response.out.write(q)

        #self.response.headers['Content-Type'] = 'text/html'
        #self.response.write(self.request)

app = webapp2.WSGIApplication([('/', MainPage),
    ('/testform',TestHandler)],
    debug=True)
