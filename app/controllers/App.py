from argparse import ArgumentParser
import settings
import jinja2
from Publisher import Publisher

class App:
  def __init__(self, path):
    self.publisher = Publisher()
   
    parser = ArgumentParser()
    parser.add_argument("-verbose",      help="show details of generated files", action="store_true")
    parser.add_argument("-pagetitles",   help="Page titles based on file names, not on first headder in document. eg. '1.02.md' would have title '02'", action="store_true")
    parser.add_argument("-outputfolder", help="output folder for generated files")
    parser.add_argument("-bootstrap",    help="use bootstrap theme", action="store_true")
        
    args = parser.parse_args()
   
    settings.viewsPath      = path + '/views'
    settings.verbose        = args.verbose  
    settings.pagetitles     = args.pagetitles
    settings.bootstrap      = args.bootstrap
    
    if args.outputfolder:
      settings.outputfolder   = args.outputfolder
    settings.templateLoader = jinja2.FileSystemLoader( searchpath=settings.viewsPath )  
    settings.templateEnv    = jinja2.Environment( loader=settings.templateLoader, trim_blocks=True, lstrip_blocks=True, line_statement_prefix='#' )
   
    print ('Moodle-Books Version ' + settings.version + ' (-h for commands)')
   
  def publishBook(self, book):
    self.publisher.publishBook(book)   
 
  def publishLab(self, book):
    self.publisher.publishLab(book)   

  def publishTopic(self, topic):
    self.publisher.publishTopic(topic)   

  def publishCourse(self, course):
    self.publisher.publishCourse(course)   
        
        