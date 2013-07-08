# -*- coding:utf-8 -*-
from Acquisition import aq_inner
from apyb.conference.content.program import IProgram
from apyb.conference.content.program import View as BaseView
from five import grok
from plone.memoize.view import memoize
from conference2013.interfaces import IConference2013
from zope.component import queryUtility
from zope.schema.interfaces import IVocabularyFactory
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

grok.templatedir('templates')


class View(BaseView):
    grok.context(IProgram)
    grok.layer(IConference2013)
    grok.require('zope2.View')

    tracks_listing = ViewPageTemplateFile('templates/tracks_listing.pt')

    def update(self):
        super(View, self).update()
        context = aq_inner(self.context)
        self._path = '/'.join(context.getPhysicalPath())
        self.state = self._multi_adapter(u'plone_context_state')
        self.tools = self._multi_adapter(u'plone_tools')
        self.portal = self._multi_adapter(u'plone_portal_state')
        self.helper = self._multi_adapter(u'helper')
        voc_factory = queryUtility(IVocabularyFactory,
                                   'apyb.conference.rooms')
        self.rooms = voc_factory(self.context)
        self._ct = self.tools.catalog()
        self._mt = self.tools.membership()
        self.is_anonymous = self.portal.anonymous()
        self.member = self.portal.member()
        self.stats = self.helper.program_stats()
        if not self.show_border:
            self.request['disable_border'] = True

    @memoize
    def tracks(self):
        ''' Return a list of tracks in here '''
        helper = self.helper
        results = helper.tracks(sort_on='getObjPositionInParent')
        return results

    @memoize
    def pc_tracks(self):
        ''' Return a list of Plone Tracks '''
        all_tracks = self.tracks()
        results = [b for b in all_tracks if '/pc/' in b.getPath()]
        return self.tracks_listing(tracks=results)

    @memoize
    def pb_tracks(self):
        ''' Return a list of PythonBrasil Tracks '''
        all_tracks = self.tracks()
        results = [b for b in all_tracks if '/pb/' in b.getPath()]
        return self.tracks_listing(tracks=results)

    @memoize
    def general_tracks(self):
        ''' Return a list of General Tracks '''
        all_tracks = self.tracks()
        results = [b for b in all_tracks
                   if '/program/' + b.getId in b.getPath()]
        return self.tracks_listing(tracks=results)
