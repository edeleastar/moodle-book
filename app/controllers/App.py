from argparse import ArgumentParser
import settings
import jinja2
from Publisher import Publisher

class App:
  def __init__(self, path):
    self.publisher = Publisher()
   
    parser = ArgumentParser()
    parser.add_argument("-verbose", help="show details of generated files", action="store_true")
    args = parser.parse_args()
   
    settings.viewsPath      = path + '/views'
    settings.verbose        = args.verbose  
    settings.templateLoader = jinja2.FileSystemLoader( searchpath=settings.viewsPath )  
    settings.templateEnv    = jinja2.Environment( loader=settings.templateLoader, trim_blocks=True, lstrip_blocks=True, line_statement_prefix='#' )
   
    print ('Moodle-Books Version ' + settings.version + ' (-h for commands)')
   
  def publishBook(self, book):
    self.publisher.publishBook(book)   
 
  def publishLesson(self, book):
    self.publisher.publishLesson(book)   