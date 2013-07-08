# -*- coding:utf-8 -*-
from conference2013.config import PROJECTNAME
from plone.app.upgrade.utils import loadMigrationProfile

import logging


def apply_profile(context):
    ''' Apply upgrade profile '''
    logger = logging.getLogger(PROJECTNAME)
    profile = 'profile-conference2013.upgrades.v2000:default'
    loadMigrationProfile(context, profile)
    logger.info('Loaded upgrade profile to version 2000')
