=====================
c2c.recipe.jarfile
=====================

A buildout recipe to create or update jar archive file.

Requirements
------------
Requires zc.buildout and the 'jar' command.


Usage
-----
Create a buildout.cfg file which contains the following::

    [buildout]
    parts = updatewar

    [updatewar]
    recipe = c2c.recipe.jarfile
    basedir = foo/bar/
    input = base.war *.png baz/config.yaml WEB-INF/
    output = /path/to/tomcat/webapps/foobar.war
    mode = update

Where:

 * 'basedir' is the directory where the jar will be created.
 * 'input' items are the files to be included in the final jar, they must be
   relative to 'basedir'.
 * 'output' is the jar destination (eg. a tomcat webapps directory)
 * 'mode' [create|update] create a new archive using all the files in 'input'
   or create an updated version of the first item of 'input' using the rest of
   the files 

TODO:
 * jar cmd in config file
