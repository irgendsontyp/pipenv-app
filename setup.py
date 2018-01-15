from setuptools import setup

setup(
	name = "pipenv-app",
	version = "1.0.0",
	description = "Pipenv test app",
	install_requires = ["pipenv-dependency"],
	dependency_links = ["git+https://github.com/irgendsontyp/pipenv-dependency.git#egg=pipenv-dependency-1.0.0"],
	packages = ["pipenvapp"]
)
