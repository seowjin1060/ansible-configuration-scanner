import json

class FilterModule(object):

    def filters(self):
        return {
            'httpm2json': self.httpm2json,
        }

    def httpm2json(self, value):
        file = open(value, 'r')
        res = {}
        for line in file:
            if '*' in line:
                key = line.replace('*','')
                res['key'] = []
            else:
                line = line.rstrip('\n')
                res['key'].append(line)
        return res