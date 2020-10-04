import json

class SearchByTag:

    def __init__(self, data_file, query_tag):
        with open(data_file) as data_file:
            self._data = json.load(data_file)
        self.query = query_tag
        self.i = 0

    def search(self):
        for i in range((self.i)+1, len(self._data["items"])):
            if self.query in self._data["items"][i]["tags"]:
                self.i = i
                yield self._data["items"][i]

    def first(self):
        for i in range(self.i, len(self._data["items"])):
            if self.query in self._data["items"][i]["tags"]:
                self.i = i
                yield self._data["items"][i]
                #return self._data["items"][i]



search = SearchByTag("python/movies.json", "crime")

print search._data["items"]
print search._data["items"][0]
print search._data["items"][0]["tags"]
print len(search._data["items"])

first_result = search.first()
#print first_result
print next(first_result)

next_result = search.search()
print next(next_result)
print next(next_result)
