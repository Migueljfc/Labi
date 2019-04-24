import cherrypy
import psutil

class Node(object):
    @cherrypy.expose
    def index(self):
        return "Eu sou o índice do Node (Node.index)"

    @cherrypy.expose
    def page(self):
        return "Eu sou um método do Node (Node.page)"
    
class Root(object):
    def __init__(self):
        self.node = Node()
        self.html = HTMLDocument()

    @cherrypy.expose
    def index(self):
        net = psutil.cpu_percent()
        return str(net)

    @cherrypy.expose
    def page(self):
        return "Eu sou um método do Root (Root.page)"

class HTMLDocument(object):
    @cherrypy.expose
    def index(self):
        f = open('index.html','r') 
        return f

if __name__ == "__main__":
    cherrypy.tree.mount(Root(),"/")
    cherrypy.server.start()