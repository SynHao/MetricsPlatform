import json

from Sql.lib import fsmanager
from Sql.lib.django_util import render


# Create your views here.
def hue(request):
    apps_list = ['hive']
    other_apps = []

    return render('hue.mako', request, {})
