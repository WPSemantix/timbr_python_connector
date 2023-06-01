import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
  name='timbr',
  version='1.0.0',
  author='timbr',
  author_email='contact@timbr.ai',
  description='Timbr Python connector',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/WPSemantix/timbr_python_connector',
  project_urls={
    "Bug Tracker": "https://github.com/WPSemantix/timbr_python_connector/issues"
  },
  license='MIT',
  packages=['timbr'],
  install_requires=[
    'JayDeBeApi==1.2.3',
    'JPype1==1.3.0',
  ],
  package_data={
    'timbr': ['jars/*'],
  },
)
