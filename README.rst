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
    input = foo/bar/base.war
            foo/bar/*.png
            foo/bar/baz/config.yaml
            foo/bar/WEB-INF/
    output = /path/to/tomcat/webapps/foobar.war

'input' items are the files to be included in the final war, the result is then
save into 'output'.

