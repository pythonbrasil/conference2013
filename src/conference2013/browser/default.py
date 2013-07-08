# -*- coding:utf-8 -*-
from conference2013.interfaces import IConference2013
from five import grok
from Products.CMFPlone.interfaces import IPloneSiteRoot


class DefaultPageView(grok.View):
    grok.context(IPloneSiteRoot)
    grok.layer(IConference2013)
    grok.require('zope2.View')
    grok.name('front-page')

    def get_hostname(self, request):
        if "HTTP_X_FORWARDED_HOST" in request.environ:
            # Virtual host
            host = request.environ["HTTP_X_FORWARDED_HOST"]
        elif "HTTP_HOST" in request.environ:
            # Direct client request
            host = request.environ["HTTP_HOST"]
        else:
            host = ''
        return host

    def render(self):
        request = self.request
        hostname = self.get_hostname(request)
        if 'ploneconf' in hostname:
            path = 'ploneconf'
        else:
            path = 'pythonbrasil'
        context = self.context
        portal_state = context.restrictedTraverse('@@plone_portal_state')
        return request.RESPONSE.redirect(
            portal_state.portal_url() + '/' + path
        )
