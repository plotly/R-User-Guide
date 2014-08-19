from django.conf import settings
import os

def items():
    items = [
        dict(
            location='/r/user-guide/',
            lmfile=os.path.join(settings.TOP_DIR,'shelly','templates','api_docs','includes','user_guide','r','user-guide','body.html'),
            priority=0.5
        )
    ]
    return items
