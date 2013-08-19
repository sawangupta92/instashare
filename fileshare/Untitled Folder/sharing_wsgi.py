# mysite_uwsgi.ini file
site.addsitedir(os.path.join('/home/sawan/Desktop','instashare/fileshare'))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), '../../../'))
sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), '../../'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'fileshare.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
[uwsgi]

# Django-related settings
# the base directory (full path)
chdir           = '/home/sawan/Desktop/instashare/fileshare'
# Django's wsgi file
module          = sharing.wsgi
# the virtualenv (full path)
# home            = /path/to/virtualenv

# process-related settings
# master
master          = true
# maximum number of worker processes
processes       = 10
# the socket (use the full path to be safe
socket          = '/home/sawan/Desktop/instashare/fileshare/mysite.sock'
# ... with appropriate permissions - may be needed
# chmod-socket    = 664
# clear environment on exit
vacuum          = true