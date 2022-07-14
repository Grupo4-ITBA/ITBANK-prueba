import webbrowser 
from main import cliente 
class GetHtml:
    def __init__(self, cliente):
        self.cliente = cliente

    def create_HTML(self):
        with open('output.html', 'w') as html_file:
        # the html code which will go in the file GFG.html
          html_template = '<p>' 
          self.cliente.name 
          '</p>'
          
          # writing the code into the file
          html_file.write(html_template)
            
          # close the file
      
          
        webbrowser.open('GFG.html') 
