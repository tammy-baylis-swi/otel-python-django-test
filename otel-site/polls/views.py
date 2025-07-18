import logging

from django.http import HttpResponse
from opentelemetry import trace
import requests


logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def reentry(request):
    """A silly little view that requests the same app by http"""
    requests.get("http://0.0.0.0:8000/polls/")
    logger.info("Made a request to polls index.")
    return HttpResponse("Done")
