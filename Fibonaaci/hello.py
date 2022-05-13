import webapp2

class MainPage(webapp2.RequestHandler):
     def get(self):
          def recur_fibonaaci(n):
               if n<=1:
                    return n
               else:
                    return recur_fibonaaci(n-1) + recur_fibonaaci(n-2)
     
          Maxterms=10;
          for i in range(1,Maxterms+1):
               self.response.write(recur_fibonaaci(i))
               self.response.write('<br/>')
          
app = webapp2.WSGIApplication([('/',MainPage)],debug=True)