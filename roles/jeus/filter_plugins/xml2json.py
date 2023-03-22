import xmltodict, json

class FilterModule(object):
    def filters(self):
        return {
            'xml2json': self.xml2json,
        }

    def xml2json(self, value):
        print(value)
        converted_xml = json.dumps(xmltodict.parse(value))
        return converted_xml
