
"""
basic index
"""

import zoom
from zoom.browse import browse



class MyView(zoom.View):
    """Index View"""

    def index(self):
        """Index page"""
        return zoom.page('Index', title='Index')



    def chart(self):
        """Chart page"""

        content = 'Hello!'
        return zoom.page(
            content.format(app=zoom.system.request.app),
            title='Zoom Chart',
        )


main = zoom.dispatch(MyView)
