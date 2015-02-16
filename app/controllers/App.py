from argparse import ArgumentParser
import settings
import jinja2
from Publisher import Publisher

class App:
  def __init__(self, path):
    self.publisher = Publisher()
   
    parser = ArgumentParser()
    parser.add_argument("-verbose",      help="show details of generated files", action="store_true")
    parser.add_argument("-outputfolder", help="output folder for generated files")
    args = parser.parse_args()
   
    settings.viewsPath      = path + '/views'
    settings.verbose        = args.verbose
    
    if args.outputfolder:
      settings.outputfolder   = args.outputfolder
    settings.templateLoader = jinja2.FileSystemLoader( searchpath=settings.viewsPath )  
    settings.templateEnv    = jinja2.Environment( loader=settings.templateLoader, trim_blocks=True, lstrip_blocks=True, line_statement_prefix='#' )
   
    print ('Tutor Version ' + settings.version + ' (-h for commands)')
   
  def publishBook(self, book):
    self.publisher.publishBook(book)   
 
  def publishLab(self, book):
    self.publisher.publishLab(book)   

  def publishTopic(self, topic):
    self.publisher.publishTopic(topic)   

  def publishCourse(self, course):
    self.publisher.publishCourse(course)   

        