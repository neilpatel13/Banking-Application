import jsons # https://jsons.readthedocs.io/en/latest/index.html
# using jsons instead of json for better nested object serialization
import math
# helper to serialize any class
class JsonSerializable(object):
    def toJson(self):
        return jsons.dumps(self)

    def __repr__(self):
        return self.toJson()

    def __str__(self):
        return self.toJson()

    def toJSON(self):
        return self.toJson()
    
class Pagination:
    def __init__(self, items, page=1, per_page=10):
        self.items = items
        self.page = page
        self.per_page = per_page

        if page > self.get_total_pages():
            page = self.get_total_pages()

    def get_items(self):
        return self.items[(self.page - 1) * self.per_page : self.page * self.per_page]

    def get_total_pages(self):
        return int(math.ceil(len(self.items) / self.per_page))

    def has_prev(self):
        return self.page > 1

    def has_next(self):
        return self.page < self.get_total_pages()

    @property
    def pages(self):
        return [i + 1 for i in range(self.get_total_pages())]
