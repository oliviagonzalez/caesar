import webapp2
import cgi
from caesar import encrypt

form="""
<form method="post">
    <label>
        Rotate text by:
        <input type="text" name="rotation" value=%(rotation)s>
    </label>
    <br>
    <input type="textarea" name="text" value=%(text)s>
    <br>
    <br>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def write_form(self, rotation="", text=""):
        self.response.out.write(form% {'text': cgi.escape(text),
                                       'rotation': cgi.escape(rotation)})

    def get(self):
        self.write_form()

    def post(self):
        #what the user actually entered
        user_text = self.request.get('text')
        user_rot = self.request.get('rotation')

        #escape
        text = cgi.escape(user_text)
        rot = cgi.escape(user_rot)

        #rot13 encryption
        if user_text:
            encryption = encrypt(text, rot)
            self.write_form(rot, encryption)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
