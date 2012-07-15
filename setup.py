import distutils.core

distutils.core.setup(
    name="pyomxplayer",
    packages = ["."],
    requires = ['pexpect (>= 2.4)'],
    )
