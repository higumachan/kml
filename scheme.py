import BeautifulSoup
from xml.etree.ElementTree import ElementTree


class DateScheme:
    def __init__(self, tag):
        self.ident = tag.find("identifier").attrib;
        self.date_scheme = tag.find("Scheme").text;

class TextScheme:
    def __init__(self, tag):
        self.ident = tag.find("identifier").attrib;

class SchemeReader:
    def __init__(self, file_name):
        f = open(file_name);
        """
        self.xml = f.read();
        self.parse();
        """
        self.root = ElementTree(file=f);
        self.parse();
        f.close();
    
    def parse(self):
        """
        bs = BeautifulSoup.BeautifulSoup(self.xml, "xml");
        print bs
        date_tag = bs.find("Date");
        print date_tag
        self.date = DateScheme(date_tag);
        text_tag = bs.find("Text");
        self.text = TextScheme(text_tag);
        """
        date_tag  = self.root.find("Date");
        self.date = DateScheme(date_tag);
        text_tag = self.root.find("Text");
        self.text = TextScheme(text_tag);


if __name__ == "__main__":
    SchemeReader("Scheme.xml");
