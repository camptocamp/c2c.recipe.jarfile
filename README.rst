=====================
c2c.recipe.installwar
=====================

Usage
-----

Create a buildout.cfg file which contains the following::

    [buildout]
    parts = warinstall

    [warinstall]
    recipe = c2c.recipe.installwar
    basedir = foo/bar/
    input = base.war *.png baz/config.yaml WEB-INF/
    output = /path/to/tomcat/webapps/foobar.war


 * 'basedir' is the directory where the war will be created
 * 'input' items are the files to be included in the final war, they must be relative to 'basedir'
 * 'output' is the war destination (eg. a tomcat webapps)
