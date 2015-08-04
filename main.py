import BaseHTTPServer
import sys, random, os, socket, urllib, json, urlparse, cgi
from firebase import firebase


mimetable = {'.html':'text/html', '.css':'text/css'}

db = None
class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
  
  def do_GET(self):
      print self.path
      if self.path.find('/paste?') != -1:
        try:
          token = self.path[self.path.find('/paste?')+7:]
          resp = db.get('/data', token)
          self.send_response(200, 'Paste Found')
          self.send_header('Content-type', 'text/html')
          self.end_headers()
          h = open('web/code.html').read().format(cgi.escape(resp))
          self.wfile.write(h)
        except Exception, e:
          print e
          self.send_response(404, 'Paste not found')
          self.end_headers()
      else:
        path = self.path
        if path=='/':path="/index.html"
        path = 'web' + path
        try:
          resp = open(path).read()
          self.send_response(200, 'Paste Found')
          self.end_headers()
          self.wfile.write(resp)
        
        except Exception, e:
          print e
          self.send_response(404, 'Not Found')
          self.end_headers()
        
  
  def do_POST(self):    
    content = self.rfile.read(int(self.headers['Content-Length']))
    content = urlparse.parse_qs(content)
    if 'content' in content:
      resp = str(content['content'][0])
      result = db.post('/data', resp)
      self.send_response(303)
      self.send_header("Location", '/paste?'+result['name'])
      self.end_headers()
    
    
    
def main():
  global db
  if 'PORT' in os.environ:
    HOST, PORT = socket.gethostname(), int(os.environ['PORT'])
  else:
    HOST, PORT = "localhost", random.choice(range(5000, 10000))
  httpd = BaseHTTPServer.HTTPServer(("", PORT), Handler)
  auth = firebase.FirebaseAuthentication(os.environ['FIREBASE_SECRET'],'codesnip:db', admin=True)
  db = firebase.FirebaseApplication('https://codesnip.firebaseio.com', authentication=auth)
  print "serving at port", PORT
  httpd.serve_forever()
  
main()