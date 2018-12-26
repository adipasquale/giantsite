import json
import urllib.request
import os
import sys


class Builder(object):

    def __init__(self, destination_dir="/tmp/www"):
        self.destination_dir = destination_dir

    def build(self):
        if not os.path.exists(self.destination_dir):
            os.makedirs(self.destination_dir)
        items = self.fetch_items()
        self.build_item_pages(items)
        self.build_index_page(items)
        print("done rebuilding inside %s !" % self.destination_dir)

    def item_page_path(self, item):
        return os.path.join(self.destination_dir, "item_%s.html" % item["id"])

    def fetch_items(self):
        api_url = "https://jsonplaceholder.typicode.com/photos"
        request = urllib.request.urlopen(api_url)
        items = json.loads(request.read())
        print("fetched %s items from API" % len(items))
        return items

    def build_item_pages(self, items):
        for item in items:
            with open(self.item_page_path(item), "w") as f:
                f.write("""
                    <html>
                    <head><title>Item %s</title></head>
                    <body>
                    <h1>%s</h1>
                    <img src="%s" />
                    </body>
                """ % (item["title"], item["title"], item["url"]))

    def build_index_page(self, items):
        index_path = os.path.join(self.destination_dir, "index.html")
        with open(index_path, "w") as f:
            links_html = "".join([
                "<li><a href='%s'>Item %s</a></li>" % (self.item_page_path(item), item["id"])
                for item in items
            ])
            f.write("""
                <html>
                <head><title>Index</title></head>
                <body>
                <h1>Index TEST 2</h1>
                <ul>
                    %s
                </ul>
                </body>
            """ % (links_html))

if __name__ == "__main__":
    Builder(sys.argv[1]).build()
