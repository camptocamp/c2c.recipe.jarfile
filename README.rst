example usage:
    [buildout]
    parts = warinstall

    [warinstall]
    recipe = c2c.recipe.installwar
    input = foo/bar/base.war
            foo/bar/*.png
            foo/bar/baz/config.yaml
            foo/bar/WEB-INF/
    output = /path/to/tomcat/webapps/final.war

If the first input argument is a war file, it will be updated with the next
files. If not, a new war file will be created.
