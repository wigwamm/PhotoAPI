
import os

from django.conf import settings

import dropbox
import requests
from celery.decorators import task


@task
def upload_to_dropbox(url, image, **kwargs):

    
    client = dropbox.client.DropboxClient(settings.DROPBOX_TOKEN)

    path = os.path.join(settings.DROPBOX_FOLDER, 'test.jpg')
    r = requests.get(url)
    response = client.put_file(path, r.content)
    
    image.status = response
    image.save()

    return True
