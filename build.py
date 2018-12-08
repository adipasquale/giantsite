import json
import urllib.request
import os

BUILD_PATH = "/tmp/huge_static_website"

if not os.path.exists(BUILD_PATH):
    os.makedirs(BUILD_PATH)

def path_for(item):
    return os.path.join(BUILD_PATH, "item_%s.html" % item["id"])


api_url = "https://jsonplaceholder.typicode.com/photos"
request = urllib.request.urlopen(api_url)
items = json.loads(request.read())
print("fetched %s items from API" % len(items))

for item in items:
    with open(path_for(item), "w") as f:
        f.write("""
            <html>
            <head><title>Item %s</title></head>
            <body>
            <h1>%s</h1>
            <img src="%s" />
            </body>
        """ % (item["title"], item["title"], item["url"]))

index_path = os.path.join(BUILD_PATH, "index.html")
with open(index_path, "w") as f:
    links_html = "".join([
        "<li><a href='%s'>Item %s</a></li>" % (path_for(item), item["id"])
        for item in items
    ])
    f.write("""
        <html>
        <head><title>Index</title></head>
        <body>
        <h1>Index</h1>
        <ul>
            %s
        </ul>
        </body>
    """ % (links_html))

print("done rebuilding ! you can open %s" % (index_path))