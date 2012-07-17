from scheme import SchemeReader
from parser import Parser
import urllib

scheme_reader = SchemeReader("Scheme.xml");
html = urllib.urlopen("http://higumachan725-aoj.blogspot.jp/2012/06/blog-post_29.html").read();
parser = Parser(scheme_reader, html);

print parser.text;
print parser.date;

