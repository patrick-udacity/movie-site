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
import cgi
import datetime
import re #Regular Expression library.
#ref: http://stackoverflow.com/questions/37757691/python-regex-date

#This function will valiate an input date. Date should use the format mm/dd/yyyy
def yield_valid_dates(dateStr):
    #Prepopulate with return value with a failure notice.
    #This accounts for gibberish or a badly formed date in the input field.
    resultList = [False,("Exception. Invalid date entered: %s", dateStr),"Error"]
    try:     
        for match in re.finditer(r"\d{1,2}/\d{1,2}/\d{4}", dateStr):
            #Return the result as a three unit list [BOOLEAN,"mm/dd/yyy","Monthname"]

            try:
                date = datetime.datetime.strptime(match.group(0), "%m/%d/%Y")
                strMonth = date.strftime("%B")
                #print strMonth
                
                #Return the result as a three unit list [BOOLEAN,"mm/dd/yyy","Monthname"]
                resultList = [True,match.group(0),strMonth]

            except ValueError:
                # date couldn't be parsed by datetime... invalid date
                #return list with only the error.
                resultList = [False,"Exception. Invalid date entered!","Error"]
                
    finally:
        return resultList



t = datetime.datetime.now()
currentTime = str(t)
form="""
<html><title>Lession 2</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<body>
<form method="post">

    <H1>Current Server Date/Time:""" + currentTime + """</H1>
    <label style="font-weight: bold">What is your birthdate? <input type="text" name="inputDate" placeholder="MM/DD/YYYY" value="%(inputDate)s"></label><br>
    <input type="submit">
    <div style="color:red">%(error)s</div>
</form>
</body></html>
"""
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.write_form()

    #This funciton will send the form to the browser.
    def write_form(self,error="",inputDate=""):
        self.response.out.write(form %{"error":error,"inputDate":inputDate})

    


    def post(self):
        #user_inputDate = self.request.get('inputDate')
        #user_inputDate = self.request.get(user_inputDate)

        def escape_html(inputString):
            return cgi.escape(inputString,quote=True)

        user_inputDate = escape_html(self.request.get('inputDate'))
        if (user_inputDate):
            checkedDate = yield_valid_dates(user_inputDate)
            if(checkedDate[0]==True):
                strOut = "Thanks. " + checkedDate[1] +" is a valid date."
                self.response.out.write(strOut)
            else:
                #user_inputDate=self.request.get('inputDate')
                self.write_form("Invalid date provided.",user_inputDate )
                #strOut = "Whoops: " + checkedDate[1] + " is not a valid date."
                #self.response.out.write(strOut)
        else:
            self.write_form("Invalid date provided.")

app = webapp2.WSGIApplication([('/', MainPage)],
    debug=True)
