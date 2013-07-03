# -*- coding:utf-8 -*-
from conference2013.config import PROJECTNAME
from plone.app.layout.navigation.interfaces import INavigationRoot
from Products.ATContentTypes.lib import constraintypes
from Products.CMFPlone.utils import _createObjectByType
from Products.Five.utilities.marker import mark

import logging

logger = logging.getLogger(PROJECTNAME)


REMOVE = [
    'events',
    'front-page',
    'Members',
    'news',
]


def remove_default_content(p):
    ''' Remove default content
    '''
    oIds = p.objectIds()
    to_remove = [oId for oId in REMOVE if oId in oIds]
    p.manage_delObjects(to_remove)
    logger.info('Default content removed')


def create_ploneconference(p):
    ''' Create Plone Conference folder
    '''
    oIds = p.objectIds()
    oId = 'ploneconf'
    if not oId in oIds:
        title = u'Plone Conference 2013'
        desc = u'Plone Conference 2013'
        _createObjectByType('Folder', p, id=oId,
                            title=title, description=desc)
    o = p[oId]
    o.setLanguage('en')
    # Set INavigationRoot
    mark(o, INavigationRoot)
    # Publish content
    p.portal_workflow.doActionFor(o, 'publish')
    logger.info('Plone Conference folder created')
    sub_folders = [
        ('the-event', 'The Event'),
        ('venue', 'Venue'),
        ('sponsors', 'Sponsors'),
        ('schedule', 'Schedule'),
        ('spread-the-word', 'Spread the Word'),
        ('contact', 'Contact'),
    ]
    for fId, title in sub_folders:
        _createObjectByType('Folder', o, id=fId,
                            title=title)
        folder = o[fId]
        p.portal_workflow.doActionFor(folder, 'publish')
        logger.info('Plone Conference: %s folder created' % title)


def create_pythonbrasil(p):
    ''' Create PythonBrasil folder
    '''
    oIds = p.objectIds()
    oId = 'pythonbrasil'
    if not oId in oIds:
        title = u'PythonBrasil [9]'
        desc = u'PythonBrasil [9]'
        _createObjectByType('Folder', p, id=oId,
                            title=title, description=desc)
    o = p[oId]
    o.setLanguage('pt-br')
    # Set INavigationRoot
    mark(o, INavigationRoot)
    # Publish content
    p.portal_workflow.doActionFor(o, 'publish')
    logger.info('PythonBrasil folder created')


def create_registrations(p):
    ''' Create Registrations structure
    '''
    oIds = p.objectIds()
    oId = 'register'
    if not oId in oIds:
        permission = 'apyb.conference: Add Registrations'
        p.manage_permission(permission, roles=['Manager', ], acquire=0)
        title = u'Register'
        desc = u'Register for both PloneConference 2013 and PythonBrasil [9]'
        _createObjectByType('registrations', p, id=oId,
                            title=title, description=desc)
        p.manage_permission(permission, roles=[], acquire=0)
    logger.info('Registrations structure created')


def create_sponsors(p):
    ''' Create Sponsors folder
    '''
    oIds = p.objectIds()
    oId = 'sponsors'
    if not oId in oIds:
        permission = 'apyb.conference: Add Sponsor'
        p.manage_permission(permission, roles=['Manager', 'Editor'], acquire=0)
        title = u'Sponsors'
        desc = u'Our sponsors'
        _createObjectByType('Folder', p, id=oId,
                            title=title, description=desc)
    o = p[oId]
    o.setConstrainTypesMode(constraintypes.ENABLED)
    o.setLocallyAllowedTypes(['sponsor'])
    o.setImmediatelyAddableTypes(['sponsor'])
    o.setLayout('folder_summary_view')
    o.setLanguage('en')
    # Publish content
    p.portal_workflow.doActionFor(o, 'publish')
    logger.info('Sponsors folder created')


def create_program(p):
    ''' Create Program
    '''
    oIds = p.objectIds()
    oId = 'program'
    if not oId in oIds:
        permission = 'apyb.conference: Add Program'
        p.manage_permission(permission,
                            roles=['Manager', 'Editor'],
                            acquire=0)
        title = u'Program'
        desc = u'Conference Program'
        _createObjectByType('program', p, id=oId,
                            title=title, description=desc)
        p.manage_permission(permission,
                            roles=[],
                            acquire=0)
    o = p[oId]
    permission = 'apyb.conference: Add Track'
    o.manage_permission(permission,
                        roles=['Manager', 'Editor'],
                        acquire=0)
    permission = 'apyb.conference: Add Speaker'
    o.manage_permission(permission,
                        roles=['Manager', 'Editor', 'Member'],
                        acquire=0)
    logger.info('Program created')


def setup_portal(context):
    ''' Setup portal content
    '''
    if context.readDataFile('initcontent.txt') is None:
        return
    site = context.getSite()
    # Remove default content
    remove_default_content(site)
    # Create PloneConf
    create_ploneconference(site)
    # Create PythonBrasil
    create_pythonbrasil(site)
    # Create Registrations
    create_registrations(site)
    # Create Sponsors
    create_sponsors(site)
    # Create Program
    create_program(site)
