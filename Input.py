from cherrypy import expose

class Adder:
    @expose
    def index(self):
        return '''<html>
                  <body>
                  <form action="add">
                      <input name="a" /> + <input name="b"> = 
                      <input type="submit" />
                  </form>
                  </body>
                  </html>'''

    @expose
    def add(self, a, b):
        return str(int(a) + int(b))


if __name__ == "__main__":
    from cherrypy import quickstart
    quickstart(Adder())
