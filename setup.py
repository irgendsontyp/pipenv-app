from setuptools import setup

setup(
	name = "pipenv-app",
	version = "1.0.0",
	description = "Pipenv test app",
	install_requires = ["pipenv-dependency"],
	packages = ["pipenvapp"]
)
