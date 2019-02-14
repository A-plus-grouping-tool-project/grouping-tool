import logging
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django_lti_login.signals import lti_login_authenticated



@receiver(lti_login_authenticated)
def store_last_login(sender, **kwargs):
    """
    Example thing to do before user is actually authenticated, but does exists.
    Django sets user.last_login after this, so it's last time to use it.
    """
    request = kwargs.get('request', None)
    user = kwargs.get('user', None)
    if request and user:
        request.session['last_login'] = str(user.last_login)
        request.session.set_expiry(0)


@receiver(user_logged_in)
def store_course_info(sender, **kwargs):
    """
    Example things to do after user is fully authenticated.
    You can still raise PermissionDenied here.
    """
    request = kwargs.get('request', None)
    session = request.session
    user = kwargs.get('user', None)
    oauth = getattr(request, 'oauth', None)
    #is_staff is an attribute of user, and it returns true if the user is a teacher
    if user.is_staff:
        oauth.redirect_url = reverse('teacherView')
    else:
        oauth.redirect_url = reverse('mainPage')
    if request and user and oauth:
        course_lms = getattr(oauth, 'tool_consumer_instance_name', None) # Example LMS
        course_id = getattr(oauth, 'context_id', None) # lms.example.com/it-101/
        course_label = getattr(oauth, 'context_label', None) # IT-101
        course_name = getattr(oauth, 'context_title', None) # Basics on IT

        if course_id is None or course_label is None or course_name is None:
            # Invalid lti login due to missing information
            raise PermissionDenied("Not all required fields present in LTI login")

        #stores course information into session variable
        session['course_id'] = course_id
        session['course_label'] = course_label
        session['course_name'] = course_name
        session['course_lms'] = course_lms
