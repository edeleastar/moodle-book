from markdown import markdown, Extension
from markdown.postprocessors import Postprocessor
from FileUtils import  read_data_from_file

def parse_markdown(md_location):
  content = read_data_from_file(md_location)
  html = generate_html(content)
  return html

def generate_html(content):
  html = markdown(content, ['fenced_code'], output_format='html5')
  return html