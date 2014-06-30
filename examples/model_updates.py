"""
This example demonstrates how updates to the application model's attributes are
reflected in the HTML view.
"""

#### Imports ####

from traits.api import HasTraits, Str
from jigna.api import Template, QtView

#### Domain model ####

class MOTD(HasTraits):
    message = Str

    def update_message(self, message):
        self.message = message

#### UI layer ####

body_html = """
    <div>
      Message of the day: {{motd.message}}
    </div>
"""

template = Template(body_html=body_html)

#### Entry point ####

def main():
    # Instantiate the domain model
    motd = MOTD(message="Explicit is better than implicit.")

    # Create a QtView to render the HTML template with the given context.
    view = QtView(template=template, context={'motd':motd})

    # Schedule an update to a model variable after 2.5 seconds. This update
    # will be reflected in the UI immediately.
    from pyface.timer.api import do_after
    do_after(2500, motd.update_message, "Flat is better than nested.")

    # Start the event loop
    view.start()

if __name__ == "__main__":
    main()

#### EOF ######################################################################