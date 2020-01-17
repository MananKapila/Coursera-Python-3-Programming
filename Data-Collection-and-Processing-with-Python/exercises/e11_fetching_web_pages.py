# The web works with a metaphor of “pages”. When we put a URL into a browser, we see a “page” of content.
# We don’t need to use a browser to fetch the contents of a page, though. In Python, there’s a module available, called
# requests. We can use the get function in the requests module to fetch the contents of a page.

# For illustration purposes, we could try visiting https://api.datamuse.com/words?rel_rhy=funny in our browser.
# It returns data in JSON format, not in HTML. Our browser would display the results (information about some words that
# rhyme with “funny”) but it wouldn’t look like a normal web page.
# Now we will try running the code below to fetch the same text string in our python program. If we try changing
# “funny” to some other word, both in the browser, and in the code below, we will see that, either way, we are
# retrieving the same thing, the datamuse API’s response to our request for words that rhyme with some word that we are
# sending as a query parameter.

import json

import requests

# This sends an http GET request to an URL and fetches the response. The returned response is an instance of a class
# called Response that is defined in the requests module.
page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(type(page))  # <class 'requests.models.Response'>
# We're going to print the first 150 characters of the response. The .text attribute contains the contents of the file
# or other information available from the url (or sometimes an error message).
print(page.text[:150])
# Now we're going to print the URL that was fetched (stored in the url attribute). We will see later that requests.get
# function takes an optional second parameter that is used to add some characters to the end of the base URL (which is
# the first parameter). The .url attribute displays the full URL that was generated from the input parameters. It can be
# helpful for debugging purposes; we can print out the URL, paste it into a browser, and see exactly what was returned.
# In this case, however, when we only passed one parameter to the get function, the generated URL is identical to the
# one we passed.
print(page.url)
print("------")
# The .json() method converts the text into a python list or dictionary, by passing the contents of the .text attribute
# to the jsons.loads function.
x = page.json()
print(type(x))  # <class 'list'>
print("---first item in the list---")
print(x[0])  # {'word': 'money', 'score': 4415, 'numSyllables': 2}
print("---the whole list, pretty printed---")
print(json.dumps(x, indent=2))  # pretty print the results
# The Response class also contains the status code of the received HTTP response.
print(page.status_code)  # 200

# When a server thinks that it is sending back what was requested, it sends the code 200.
# When the requested page doesn’t exist, it sends back code 404, which is sometimes described as “File Not Found”.
# When the page has moved to a different location, it sends back code 301 and a different URL where the client is
# supposed to retrieve from. The get function of the request module is so smart that when it gets a 301, it looks at
# the new URL and fetches it. For example, github redirects all requests using http to the corresponding page using
# https (the secure http protocol). Thus, when we ask for http://github.com/presnick/runestone, github sends back a
# 301 code and the URL https://github.com/presnick/runestone. The requests.get function then fetches the other URL.
# It reports a status of 200 and the updated URL. We have to do further inquire to find out that a redirection occurred
# (see below).

# The .headers attribute has as its value a dictionary consisting of keys and values.
print(page.headers.keys())  # KeysView({'Cache-Control': 'no-transform, max-age=86400', ...})
# We notice that one of the headers is ‘Content-type’. Some possible values are text/html; charset-utf-8 and
# application/json; charset=utf-8.

# The .history attribute contains a list of previous responses, if there were redirects.
print(page.history)  # []
# In this case, there were no redirects involved in fulfilling our request.
