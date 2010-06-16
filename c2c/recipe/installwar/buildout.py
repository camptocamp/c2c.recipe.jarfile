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
        base = buildout['buildout']['directory']

        self.basedir = os.path.join(base, options['basedir'])
        # check if self.basedir exists
        self.input = options['input'].split()
        self.output = os.path.join(base, options['output'])
        # check if os.basedir(self.output) exists and is writable
        # check if self.output is not a directory

    def install(self):
        warname = os.path.basename(self.output)
        tmpwar = os.path.join(tempfile.mkdtemp(), warname)
        errors = tempfile.TemporaryFile()

        cmd = "jar -cf %s %s"%(tmpwar, ' '.join(self.input))
        retcode = call(cmd.split(), cwd=self.basedir, stdout=errors, stderr=STDOUT)

        if retcode != 0:
            errors.seek(0)
            # raise

        shutil.copy(tmpwar, self.output)
        shutil.rmtree(os.path.dirname(tmpwar))

        # returns the war and the directory name
        return [self.output, self.output.replace('.war', '')]

    update = install
