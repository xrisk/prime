import BaseHTTPServer
import sys, random, os, socket, urllib, json, urlparse, cgi



mimetable = {'.html':'text/html', '.css':'text/css'}

db = None
class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
  
  def do_GET(self):
      self.wfile.write('This page serves as a stupid wrapper, because Heroku has to have a web dyno running. #muchlogic')
  
    
    
def main():
  global db
  if 'PORT' in os.environ:
    HOST, PORT = socket.gethostname(), int(os.environ['PORT'])
  else:
    HOST, PORT = "localhost", random.choice(range(5000, 10000))
  httpd = BaseHTTPServer.HTTPServer(("", PORT), Handler)
  
  
  print "serving at port", PORT
  httpd.serve_forever()
  
main()