import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        for i in range(1,11):
            self.response.write("4 x {} = {}".format(i,4*i))
            self.response.write('</br>')
            
        

app = webapp2.WSGIApplication([('/',MainPage)],debug=True)