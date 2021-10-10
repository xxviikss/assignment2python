to scrap all the related information  from Coinmarketcap.com about different cryptocurrencies 

# Requests

**Requests** is a simple, yet elegant, HTTP library.

```python
>>> import requests
>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
'{"type":"User"...'
>>> r.json()
{'disk_usage': 368627, 'private_gists': 484, ...}
```

Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your `PUT` & `POST` data — but nowadays, just use the `json` method!

Requests is one of the most downloaded Python package today, pulling in around `30M downloads / week`— according to GitHub, Requests is currently [depended upon](https://github.com/psf/requests/network/dependents?package_id=UGFja2FnZS01NzA4OTExNg%3D%3D) by `500,000+` repositories. You may certainly put your trust in this code.

[![Downloads](https://pepy.tech/badge/requests/month)](https://pepy.tech/project/requests)
[![Supported Versions](https://img.shields.io/pypi/pyversions/requests.svg)](https://pypi.org/project/requests)
[![Contributors](https://img.shields.io/github/contributors/psf/requests.svg)](https://github.com/psf/requests/graphs/contributors)

## Installing Requests and Supported Versions

Requests is available on PyPI:

```console
$ python -m pip install requests
```

Requests officially supports Python 2.7 & 3.6+.

## Supported Features & Best–Practices

Requests is ready for the demands of building robust and reliable HTTP–speaking applications, for the needs of today.

- Keep-Alive & Connection Pooling
- International Domains and URLs
- Sessions with Cookie Persistence
- Browser-style TLS/SSL Verification
- Basic & Digest Authentication
- Familiar `dict`–like Cookies
- Automatic Content Decompression and Decoding
- Multi-part File Uploads
- SOCKS Proxy Support
- Connection Timeouts
- Streaming Downloads
- Automatic honoring of `.netrc`
- Chunked HTTP Requests

## API Reference and User Guide available on [Read the Docs](https://requests.readthedocs.io)

[![Read the Docs](https://raw.githubusercontent.com/psf/requests/main/ext/ss.png)](https://requests.readthedocs.io)

## Cloning the repository

When cloning the Requests repository, you may need to add the `-c
fetch.fsck.badTimezone=ignore` flag to avoid an error about a bad commit (see
[this issue](https://github.com/psf/requests/issues/2690) for more background):

```shell
git clone -c fetch.fsck.badTimezone=ignore https://github.com/psf/requests.git
```

You can also apply this setting to your global Git config:

```shell
git config --global fetch.fsck.badTimezone ignore
```

---

[![Kenneth Reitz](https://raw.githubusercontent.com/psf/requests/main/ext/kr.png)](https://kennethreitz.org) [![Python Software Foundation](https://raw.githubusercontent.com/psf/requests/main/ext/psf.png)](https://www.python.org/psf)

# Beautifulsoup
## Installation

```  >>> from bs4 import BeautifulSoup
```
## Using
```  >>> soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
  >>> print soup.prettify()
<html>
   <body>
    <p>
     Some
     <b>
      bad
      <i>
       HTML
      </i>
     </b>
    </p>
   </body>
  </html>
  >>> soup.find(text="bad")
  u'bad'

  >>> soup.i
  <i>HTML</i>

  >>> soup = BeautifulSoup("<tag1>Some<tag2/>bad<tag3>XML", "xml")
  >>> print soup.prettify()
  <?xml version="1.0" encoding="utf-8">
  <tag1>
   Some
   <tag2 />
   bad
   <tag3>
    XML
   </tag3>
  </tag1>
```
= Full documentation =

The bs4/doc/ directory contains full documentation in Sphinx
format. Run "make html" in that directory to create HTML
documentation.

= Running the unit tests =

Beautiful Soup supports unit test discovery from the project root directory:

 ```$ nosetests```

 ```$ python -m unittest discover -s bs4 # Python 2.7 and up```

If you checked out the source tree, you should see a script in the
home directory called test-all-versions. This script will run the unit
tests under Python 2.7, then create a temporary Python 3 conversion of
the source and run the unit tests again under Python 3.

= Links =

Homepage: http://www.crummy.com/software/BeautifulSoup/bs4/
Documentation: http://www.crummy.com/software/BeautifulSoup/bs4/doc/
               http://readthedocs.org/docs/beautiful-soup-4/
Discussion group: http://groups.google.com/group/beautifulsoup/
Development: https://code.launchpad.net/beautifulsoup/
Bug tracker: https://bugs.launchpad.net/beautifulsoup/
