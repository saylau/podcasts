import os
from uuid import uuid4


def upload_file(instance, filename):
    return os.path.join('podcasts/%s' % str(uuid4()), filename)
