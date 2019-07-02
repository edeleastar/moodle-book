from markdown import markdown
from utils.FileUtils import  read_data_from_file
from os import remove
import settings

def parse_markdown(md_location):
  content = read_data_from_file(md_location)
  html = generate_html(content)
  if settings.verbose:
    print ('parsing ' + md_location)
  return html

def generate_html(content):
  html = markdown(content, extensions=['fenced_code', 'tables'], output_format='html5')
  return html

def parse_markdown_without_header(md_location):
  with open(md_location, 'r') as fin:
    data = fin.read().splitlines(True)
  with open('temp.md', 'w') as fout:
    fout.writelines(data[1:])
    fout.close()
  withoutHeadder  = parse_markdown('temp.md')
  remove ('temp.md')
  return withoutHeadder