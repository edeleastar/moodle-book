from markdown import markdown
from FileUtils import  read_data_from_file
import settings

def parse_markdown(md_location):
  content = read_data_from_file(md_location)
  html = generate_html(content)
  if settings.verbose:
    print ('parsing ' + md_location)
  return html

def generate_html(content):
  html = markdown(content, ['fenced_code', 'tables'], output_format='html5')
  return html