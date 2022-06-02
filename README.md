# plane

(name is WIP to avoid trademark issues temporarily)

A simple experimental Python wrapper for the Ravy API.

This is currently a work in progress state. Since this is a first experience as a developer working on an API wrapper, this might not utilize the best Python practices. If you see anything that needs to be changed, feel free to create a pull request!

This API is heavily inspired and is partially based upon the [ksoftapi Python wrapper](https://github.com/KSoft-Si/ksoftapi.py). Parts of the client and HTTP client were modified off of this, as well as the model interface designs.

TODO:

- [ ] Full API coverage
  - Add ban POST (admin.bans)
  - Edit website POST (admin.urls)
  - Avatars multipart/formdata POST (avatars)
- [ ] More flexibility
  - Use the url queries for `get_url()`
- [ ] Unit tests (Depends; I am most certainly not mocking an *entire* API you know, however some parts...)

DONE:

- [x] Basic HTTP requests functionality
- [x] Few API functionalities/routes
- [x] Docstrings (so far)
- [x] Public documentation
- [x] Abstract responses to objects
- [x] Client side validation for token and permissions
