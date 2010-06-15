example usage:
    [buildout]
    parts = warinstall

    [warinstall]
    recipe = c2c.recipe.installwar
    input = foo/bar/base.war
            foo/bar/baz/*.png
            foo/bar/baz/config.yaml
    dest = /path/to/tomcat/webapps/final.war
