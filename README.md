# shrinkurlnow

This project will turn a long url into a short one using Django Python.
It uses postgresql as the database and is a little unrefined as it is not intended for production at this time.
Read through the comments to follow the logic:
It uses templates for the webpage with a form to post the data.
The URI file handles the conversion of a short URL to a long one.
The post request inserts a URL pair of the short URL and Long URL into the Database for later retrieval.

Project is working with latest Django 5.1.4, Released Dec 4, 2024
Docker files included for a container setup.

