from django.db import models

# Create your models here.
import tasks

class RepixlImage(models.Model):
    url = models.CharField(max_length=256)
    email_address = models.CharField(max_length=256)
    status = models.CharField(max_length=256)

    class Meta:
        pass

    def __unicode__(self):
        return self.url

    def upload_to_dropbox(self):
        #
        self.status = 'uploading to dropbox'
        self.save()
        
        tasks.upload_to_dropbox.delay(self.url, self)
        
