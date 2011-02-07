# -*- coding: utf-8 -*-

import os
import shutil
import tempfile
import logging
from glob import glob
from subprocess import call, STDOUT
import zc.buildout

class CreateUpdateJar(object):
    def __init__(self, buildout, name, options):
        self.name = name
        base = buildout['buildout']['directory']
        self.logger = logging.getLogger(self.name)

        self.basedir = os.path.join(base, options['basedir'])
        self.input = options.get('input', '')

        self.output = os.path.join(base, options['output'])
        # check if os.basedir(self.output) exists and is writable
        # check if self.output is not a directory

        self.mode = options.get('mode')
        if self.mode not in ['create', 'update']:
            raise zc.buildout.UserError('invalid mode. must be create or update')


    def install(self):
        os.chdir(self.basedir)
        filenames = []
        for item in self.input.split():
            filenames.extend(glob(item))

        tmpdir = tempfile.mkdtemp()
        jarfile = os.path.join(tmpdir, os.path.basename(self.output))
        args = {'jarfile': jarfile}

        if self.mode == 'create':
            args.update({'inputfiles': ' '.join(filenames)})
            cmd = "jar cf %(jarfile)s %(inputfiles)s"%args
        elif self.mode == 'update':
            shutil.copyfile(os.path.join(self.basedir, filenames[0]), jarfile)
            args.update({'inputfiles': ' '.join(filenames[1:])})
            cmd = "jar uf %(jarfile)s %(inputfiles)s"%args 

        self.logger.debug("running '%s'"%cmd)
        errors = tempfile.TemporaryFile()
        retcode = call(cmd.split(), cwd=self.basedir, stdout=errors, stderr=STDOUT)
        
        if retcode != 0:
            errors.seek(0)
            shutil.rmtree(tmpdir)
            raise Exception("error while creating jar: \n%s\n"%errors.read())
        else:
            shutil.copyfile(jarfile, self.output)
            self.logger.debug("saving to '%s'"%self.output)
            shutil.rmtree(tmpdir)
            return [self.output, self.output.replace('.war', '')]

    update = install
