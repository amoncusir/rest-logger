# REST Logger #

Python project that expose an endpoint for make HTTP
petitions.

The endpoint is dynamic and can accept custom HTTP status if it set in petition using path argument, named `status`.
By default the response status is `200` (OK).

For run project in your machine, you need have install in you environment `python3` and execute these commands:

``` bash
$ make init & make start
``` 

The endpoint can accept the HTTP methods: (`GET`, `POST`,`PUT`, `DELETE`, `PATCH`)
For change HTTP status in response use `status` path argument, like: `/my/fictitious/path?status=404`.
This call return a `404` code.

By default the server run in port `3000` and can be customize in `endpoint.py` file.

This project is soo basic and simple. 

Using flask as HTTP server.
