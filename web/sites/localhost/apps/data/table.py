
from zoom.mvc import View
from zoom.page import page
from zoom.tools import load_content
from zoom.browse import browse
from zoom.fields import *
from zoom.validators import required


class MyView(View):
    """Table"""

    def index(self):
  
        content = load_content('sample.md')
        return page(content)

def main(route, request):
    view = MyView(request.site)
    return view(*route, **request.data)

