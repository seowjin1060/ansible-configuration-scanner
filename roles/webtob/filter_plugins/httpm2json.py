import json


class FilterModule(object):
    def filters(self):
        return {
            'httpm2json': self.httpm2json,
        }

    def httpm2json(self, value):
        #file = open(value, 'r')
        res = {}
        line = ""
        is_key = False
        key = ""
        for letter in value:
            if '*' in letter:
                is_key = True
                continue
            if letter == '\n':
                if is_key:
                    res[key] = []
                    is_key = False
                else:
                    if line == "":
                        continue
                    else:
                        line=line.replace(' ','')
                        res[key].append(line)
                        line =""
            else:
                if is_key:
                    key += letter
                else:
                    line += letter
        return res