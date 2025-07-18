import logging

from django.http import HttpResponse
from opentelemetry import trace
import requests


logger = logging.getLogger(__name__)


def index(request):
    logger.warning("Welcome to polls index")
    return HttpResponse("Hello, world. You're at the polls index.")


def reentry(request):
    """A silly little view that requests the same app by http"""
    logger.warning("Received request for /reentry with headers:")
    logger.warning("%s", request.headers)
    requests.get("http://0.0.0.0:8000/polls/")
    logger.warning("Made a request to polls index.")
    return HttpResponse("Done")
