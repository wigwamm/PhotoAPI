from celery.decorators import task


@task
def upload_to_dropbox(url, image, **kwargs):

    image.status = 'uploaded';
    image.save()
    
    # we'll upload an image to DROPBOX.

    # session = HttpSession.objects.get(pk=session_id)
    # logger = make_session_request.get_logger(**kwargs)

    # logger.info("Starting request for session %s" % session.id)

    # # lots more code goes here...

    # session.save()
    return True
