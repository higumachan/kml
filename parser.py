import BeautifulSoup
import datetime
import re

class Parser:
    def __init__(self, scheme, html):
        self.parse(scheme, html);
    
    def parse(self, scheme, html):
        bs = BeautifulSoup.BeautifulSoup(html);
        self.text = self.parse_text(scheme.text, bs);
        self.date = self.parse_date(scheme.date, bs);
    
    def parse_text(self, scheme, bs):
        id = scheme.ident["id"];
        #cl = scheme.ident["class"];

        id_search = re.compile(id);
        #cl_search = re.compile(cl);

        result = bs.find(attrs={"id": id_search}).text;

        return result;
    
    def parse_date(self, scheme, bs):
        attrs = {};
        if (scheme.ident.has_key("id")):
            id = scheme.ident["id"];
            attrs["id"] = re.compile(id);
        if (scheme.ident.has_key("class")):
            cl = scheme.ident["class"];
            attrs["class"] = re.compile(cl);

        date_str = bs.find(attrs=attrs).text;
        date_str = date_str[:len(scheme.date_scheme) + 1];
        result = datetime.datetime.strptime(date_str.encode("utf-8"), scheme.date_scheme.encode("utf-8"));

        return (result);


