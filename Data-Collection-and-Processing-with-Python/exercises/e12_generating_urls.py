import requests

# The HTTP protocol contains some restrictions regarding what characters can be used as part of a URL.
# For example, a URL cannot contain any spaces, / or : characters. For this reason, there are special combinations of
# characters designated as replacements for these forbidden characters.
# More specifically:
# a space is encoded as +
# " is encoded as %22
# : is encoded as %3A
# ...and so on.

# Fortunately, when we want to pass information as a URL parameter value, we don’t have to remember all the
# substitutions that are required to encode special characters. Instead, that capability is built into the requests
# module.

# The get function in the requests module takes an optional parameter called params. If a value is specified for that
# parameter, it should be a dictionary. The keys and values in that dictionary are used to append something to the URL
# that is requested from the remote site.

d = {'q': '"violins and guitars"', 'tbm': 'isch'}
results = requests.get("https://google.com/search", params=d)
print(results.url)  # https://www.google.com/search?q=%22violins+and+guitars%22&tbm=isch
# Because dictionary keys are unordered in python, the final url might sometimes have the encoded key-value pairs in a
# completely random order. Fortunately, most websites that accept URL parameters in this form will accept the key-value
# pairs in any order.

# Let's see another example:
kval_pairs = {'rel_rhy': 'funny'}
page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
# Let's print the first 50 characters:
print(page.text[:50])  # [{"word":"money","score":4415,"numSyllables":2},{"
# We print the url that was fetched:
print(page.url)  # https://api.datamuse.com/words?rel_rhy=funny

# Unfortunately, if the call to requests.get produces an error, we won’t get a Response object, so we’ll need some
# other way to see what URL was produced. The function defined below takes the same parameters as requests.get and
# returns the URL as a string, without trying to fetch it.

def requestURL(baseurl, params = {}):
    # This function accepts a URL path and a params diction as inputs.
    # It calls requests.get() with those inputs,
    # and returns the full URL of the data you want to get.
    req = requests.Request(method = 'GET', url = baseurl, params = params)
    prepped = req.prepare()
    return prepped.url

# print(requestURL(some_base_url, some_params_dictionary))