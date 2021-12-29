# otel-python-django-test

Toy Django app instrumented with OTEL Python agent. Dev mode only. It's the start of the Django polls tutorial + parts of the OTEL django example.

## Local setup

1. Clone this repo and `cd <repo_path>/otel-site`.
2. Create and activate a virtual environment with Python 3.8.
3. `pip install -r requirements.txt`
4. If you want, make sure that worked with `python hello-otel.py`

5. `export DJANGO_SETTINGS_MODULE=otel-site.settings`
6. Run `otel-site` on http://localhost:8000 with: `python manage.py runserver --noreload`
7. In a separate Terminal (same dir, same virtual env), run the client with `python client.py`. This triggers OTEL trace export to stdout with a request to the Polls index at http://localhost:8000/polls

## References

* https://opentelemetry.io/docs/instrumentation/python/getting-started/
* https://opentelemetry-python.readthedocs.io/en/latest/examples/django/README.html