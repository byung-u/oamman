from django.conf import settings
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from django.db.models import Count
from collections import OrderedDict
from datetime import datetime

from base.models import Banner


def default(request):
    title = None
    url = request.path
    if settings.FORCE_SCRIPT_NAME:
        url = url[len(settings.FORCE_SCRIPT_NAME):]
    base_content = FlatPage.objects.filter(url=url).first()

    submenu = None
    menu = OrderedDict([
        ('issue', {
            'title': _('Issue'),
            'icon': 'calendar',
            'submenu': OrderedDict([
                ('issue_add', {'title': _('Issue add')}),
                ('issue_list', {'title': _('Issue list')}),
                ('issue_modi', {'title': _('Issue modify')}),
            ]),
        }),
        ('project', {
            'title': _('Project'),
            'icon': 'edit',
            'submenu': OrderedDict([
                ('project_add', {'title': _('Project add')}),
                ('project_issue', {'title': _('Project issue')}),
                ('project_list', {'title': _('Project list')}),
                ('project_modi', {'title': _('Project modify')}),
            ]),
        }),
    ])

    rp = request.path[len(settings.FORCE_SCRIPT_NAME):]

    for k, v in menu.items():
        path = '/{}/'.format(k)

        if rp.startswith(path):
            v['active'] = True
            title = v['title']

            if 'submenu' in v:
                submenu = v['submenu']

                for sk, sv in v['submenu'].items():
                    sv['path'] = '{}{}/'.format(path, sk)
                    subpath = sv['path'][:-2]

                    if rp.startswith(subpath):
                        sv['active'] = True
                        title = sv['title']

    now = datetime.now()
    banners = Banner.objects.filter(begin__lte=now, end__gte=now)

    c = {
        'menu': menu,
        'submenu': submenu,
        'banners': banners,
        'title': title,
        'domain': settings.DOMAIN,
        'base_content': base_content.content if base_content else '',
    }
    return c

'''
def profile(request):
    speaker = None
    programs = None

    if request.user.is_authenticated():
        speaker = Speaker.objects.filter(email=request.user.email).first()
        if speaker:
            programs = speaker.program_set.all()

    return {
        'my_speaker': speaker,
        'my_programs': programs,
    }
'''
