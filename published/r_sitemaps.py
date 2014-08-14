from django.conf import settings
import os

def items():
    items = [
        dict(
            location='/r/histograms-tutorial/',
            lmfile=os.path.join(settings.TOP_DIR,'shelly','templates','api_docs','includes','user_guide','r','histograms-tutorial','body.html'),
            priority=0.5
        ),
        dict(
            location='/r/user-guide/',
            lmfile=os.path.join(settings.TOP_DIR,'shelly','templates','api_docs','includes','user_guide','r','user-guide','body.html'),
            priority=0.5
        ),
        dict(
            location='/r/line-shapes-tutorial/',
            lmfile=os.path.join(settings.TOP_DIR,'shelly','templates','api_docs','includes','user_guide','r','line-shapes-tutorial','body.html'),
            priority=0.5
        )
    ]
    return items
