# otel-python-django-test

Django app that's auto-instrumented with OTEL Python default distro. Dev mode only; exports telemetry to console.

## Local setup

1. Create and activate a virtual environment with Python >= 3.9.
2. `pip install -r requirements.txt`
3. `export DJANGO_SETTINGS_MODULE=otel-site.settings`
4. `cd <repo>/otel-site`
5. You may need to `python manage.py migrate` the first time.
6. `export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true`
7. `opentelemetry-bootstrap --action=install`
8. `opentelemetry-instrument --traces_exporter console --metrics_exporter console --logs_exporter console python manage.py runserver --noreload`

## Generate spans, metrics, logs

```
curl -v http://localhost:8000
curl -v http://localhost:8000/polls
curl -v http://localhost:8000/polls/reentry
```

## Distributed trace script

In a separate Terminal (same dir, same virtual env, same dependencies), run a request client with `python client.py`. This triggers distributed OTel trace export to stdout by including OTel context in request to Django (http://localhost:8000/polls).

## References

* https://opentelemetry.io/docs/instrumentation/python/getting-started/
* https://opentelemetry-python.readthedocs.io/en/latest/examples/django/README.html