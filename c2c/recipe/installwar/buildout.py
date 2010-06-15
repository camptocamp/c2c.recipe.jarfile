# -*- coding: utf-8 -*-
# buildout recipe for c2c.recipe.installwar
#

class InstallWar(object):
    def __init__(self, buildout, name, options):
        basedir = buildout['buildout']['directory']

    def install(self):
        pass

    def update(self):
        pass
    update = install
