import xmltodict, json

class FilterModule(object):

    def filters(self):
        return {
            'xml2json': self.xml2json,
        }

    def xml2json(self, value):
        return json.dumps(xmltodict.parse(value))
