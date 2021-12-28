# otel-python-django-test

Toy Django app instrumented with OTEL Python agent. Dev mode only. It's the start of the Django polls tutorial + parts of the OTEL django example.

## Local setup

1. Clone this repo and `cd <repo_path>/otel-site`.
2. Create and activate a virtual environment with Python 3.8.
3. Install a lot of things:

```
pip install Django
pip install opentelemetry-api
pip install opentelemetry-sdk
pip install opentelemetry-instrumentation
pip install opentelemetry-instrumentation-django
```

4. Run on localhost:8000 with: `python manage.py runserver --noreload`
5. In a separate Terminal in the same dir, trigger the client with `python client.py hello` to output some spans.
6. ...


## References

* https://opentelemetry.io/docs/instrumentation/python/getting-started/
* https://opentelemetry-python.readthedocs.io/en/latest/examples/django/README.html