import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
  name='PyTimbr',
  version='1.0.0',
  author='timbr',
  author_email='contact@timbr.ai',
  description='Timbr Python connector',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/WPSemantix/timbr_python_connector',
  download_url = 'https://github.com/WPSemantix/timbr_python_connector/archive/refs/tags/v1.0.0.tar.gz',
  project_urls={
    "Bug Tracker": "https://github.com/WPSemantix/timbr_python_connector/issues"
  },
  license='MIT',
  packages=['PyTimbr'],
  install_requires=[
    'JayDeBeApi==1.2.3',
    'JPype1==1.3.0',
  ],
  package_data={
    'PyTimbr': ['jars/*'],
  },
  keywords = [
    'timbr',
    'timbr-python',
    'timbr-connector',
    'python-connector',
    'PyTimbr',
    'pytimbr',
    'py-timbr',
    'Py-Timbr',
  ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
