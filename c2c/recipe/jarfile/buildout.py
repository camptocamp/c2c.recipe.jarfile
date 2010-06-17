# -*- coding: utf-8 -*-

import os
import shutil
import tempfile
from glob import glob
from subprocess import call, STDOUT

class CreateUpdateJar(object):
    def __init__(self, buildout, name, options):
        self.name = name
        base = buildout['buildout']['directory']

        self.basedir = os.path.join(base, options['basedir'])

        self.input = []
        os.chdir(self.basedir)
        for item in options['input'].split():
            self.input.extend(glob(item))

        self.output = os.path.join(base, options['output'])
        # check if os.basedir(self.output) exists and is writable
        # check if self.output is not a directory

        self.mode = options.get('mode')
        # assert self.mode in ['create', 'update']

    def install(self):
        tmpdir = tempfile.mkdtemp()
        jarfile = os.path.join(tmpdir, os.path.basename(self.output))
        args = {'jarfile': jarfile}

        if self.mode == 'create':
            args.update({'inputfiles': ' '.join(self.input)})
            cmd = "jar cf %(jarfile)s %(inputfiles)s"%args
        elif self.mode == 'update':
            shutil.copy(os.path.join(self.basedir, self.input[0]), jarfile)
            args.update({'inputfiles': ' '.join(self.input[1:])})
            cmd = "jar uf %(jarfile)s %(inputfiles)s"%args 
        else:
            raise 'unknow mode'

        errors = tempfile.TemporaryFile()
        retcode = call(cmd.split(), cwd=self.basedir, stdout=errors, stderr=STDOUT)
        
        if retcode != 0:
            errors.seek(0)
            raise 'error while creating jar'
        else:
            shutil.copy(jarfile, self.output)
            shutil.rmtree(tmpdir)
            return [self.output, self.output.replace('.war', '')]

    update = install
