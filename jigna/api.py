from template import Template
from core.concurrent import Future
from qt_app import QtApp

# Wrapping the WebApp import so that you can use jigna even if you don't have
# tornado install
try:
    from web_app import WebApp
except ImportError:
    pass