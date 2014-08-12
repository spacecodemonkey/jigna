from jigna.api import QtApp
from jigna.api import Template

from pyface.qt import QtWebKit, QtGui
from pyface.gui import GUI

import unittest

class TestQtApp(unittest.TestCase):

    def setUp(self):
        self.template = Template(body_html="")
        self.app = QtApp(template=self.template, context={})

    def test_widget_is_created(self):
        # Create a widget
        qwidget = self.app.create_widget()

        # Check if a qwebview widget was created
        self.assertIsNotNone(qwidget)
        self.assertIsInstance(qwidget, QtGui.QWidget)
        self.assertIsInstance(qwidget, QtWebKit.QWebView)

    def test_created_widget_loads_html(self):
        # Create a widget
        qwidget = self.app.create_widget()
        GUI.process_events()

        # Check if the widget has html loaded in it
        frame = qwidget.page().mainFrame()
        self.assertIsInstance(frame.toHtml(), basestring)
        self.assertGreater(len(frame.toHtml()), 0)

    def test_created_widget_can_access_jigna(self):
        # Create a widget and execute a js to determine whether jigna is
        # available in the Javascript console or not
        qwidget = self.app.create_widget()
        GUI.process_events()

        # Check if the widget was created
        jigna = self.app.execute_js("jigna");
        self.assertIsNotNone(jigna)

if __name__ == "__main__":
    unittest.main()