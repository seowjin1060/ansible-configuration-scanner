

class FilterModule(object):

    def filters(self):
        return {
            'xml2json': self.httpm2json,
        }

    def httpm2json(self, value):
        return