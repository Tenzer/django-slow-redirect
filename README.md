Install dependencies from `requirements.txt`.

Run uWSGI with `uwsgi --ini uwsgi.ini`.

Try making requests for http://127.0.0.1:8010/url and http://127.0.0.1:8011/url to compare.

Port 8010 is using the `http-socket` option and port 8011 is using `http11-socket`.
