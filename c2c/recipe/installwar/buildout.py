# -*- coding: utf-8 -*-
# buildout recipe for c2c.recipe.installwar
#
import os
import shutil
import tempfile
from subprocess import call, STDOUT

class InstallWar(object):
    def __init__(self, buildout, name, options):
        self.name = name
        basedir = buildout['buildout']['directory']

        self.input = [os.path.join(basedir, f) for f in options['input'].split()]
        self.output = os.path.join(basedir, options['output'])
        # check if os.basedir(self.output) exists and is writable

    def install(self):
        warname = os.path.basename(self.output)
        tmpwar = os.path.join(tempfile.mkdtemp(), warname)
        errors = tempfile.TemporaryFile()
        retcode = call("jar -cf %s %s"%(tmpwar, ' '.join(self.input)).split(), 
                       cwd=dirname, stdout=errors, stderr=STDOUT)

        if retcode != 0:
            errors.seek(0)
            # raise

        shutil.copystat(tmpwar, self.output)
        shutil.rmtree(os.path.dirname(tmpwar))

        # returns the war and the directory name
        return [self.output, self.output.replace('.war', '')]

    update = install
