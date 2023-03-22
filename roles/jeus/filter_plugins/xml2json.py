import xmltodict, json


class FilterModule(object):
    def filters(self):
        return {
            'xml2json': self.xml2json,
        }

    def xml2json(self, value):
        converted_xml = json.dumps(xmltodict.parse(value))
        print(converted_xml)
        return converted_xml
