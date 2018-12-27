# Giant static website builder

A very simple script fetches 5000 photos from the [JSONPlaceholder Fake API](https://jsonplaceholder.typicode.com/), and builds a static website with an index and one page per photo.

This repository is used in this blog post: [Build and deploy huge static websites with Caddy](https://blog.dipasquale.fr/en/2018/12/27/build-and-deploy-huge-static-websites-with-caddy/)

## Run

The script has no external dependency, **you just need to run it with Python 3** :

```sh
python3 build.py /tmp/www
```
