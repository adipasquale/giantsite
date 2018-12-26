import json
import urllib.request
import os
import sys

ITEM_PAGE_TEMPLATE = """
    <html>
    <head>
        <title>Page %s</title>
        <link rel="stylesheet" href="https://unpkg.com/tachyons@4.10.0/css/tachyons.min.css"/>
    </head>
    <body>
        <article class="mw5 center bg-white br3 pa3 pa4-ns mv3 ba b--black-10">
            <div class="tc">
                <img src="%s" class="br-100 h4 w4 dib ba b--black-05 pa2" title="Photo of a kitty staring at you">
                <h1 class="f3 mb2">%s</h1>
                <h2 class="f5 fw4 gray mt0">Some text...</h2>
            </div>
        </article>
    </body>
"""

INDEX_PAGE_TEMPLATE = """
    <html>
    <head>
        <title>Index</title>
        <link rel="stylesheet" href="https://unpkg.com/tachyons@4.10.0/css/tachyons.min.css"/>
    </head>
    <body>
    <h1 class="f4 bold center mw5">List of pages</h1>
    <ul class="list pl0 ml0 center mw5 ba b--light-silver br3">
        %s
    </ul>
    </body>
"""

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
                f.write(ITEM_PAGE_TEMPLATE % (item["title"], item["url"], item["title"]))

    def build_index_page(self, items):
        index_path = os.path.join(self.destination_dir, "index.html")
        with open(index_path, "w") as f:
            links_html = "".join([
                "<li class='ph3 pv2 bb b--light-silver'><a href='%s'>Page %s</a></li>" %
                (self.item_page_path(item), item["id"])
                for item in items
            ])
            f.write(INDEX_PAGE_TEMPLATE % (links_html))

if __name__ == "__main__":
    Builder(sys.argv[1]).build()
