
class ec_cntdic(object):

    def __init__(self):
        self.data = dict()

    def add(self, itm):
        if itm not in self.data.keys():
            self.data[itm] = 1
        else:
            self.data[itm] += 1

    def by_cnt(self, sort=True):
        if sort:
            return sorted([(self.data[key], key) for key in self.data.keys()], reverse=True)
        else:
            return [(self.data[key], key) for key in self.data.keys()]