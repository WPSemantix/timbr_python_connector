import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
  name='pytimbr',
  version='1.0.7',
  author='timbr',
  author_email='contact@timbr.ai',
  description='Timbr Python connector',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/WPSemantix/timbr_python_connector',
  download_url = 'https://github.com/WPSemantix/timbr_python_connector/archive/refs/tags/v1.0.7.tar.gz',
  project_urls={
    "Bug Tracker": "https://github.com/WPSemantix/timbr_python_connector/issues"
  },
  license='MIT',
  packages=['pytimbr'],
  install_requires=[
    'JPype1==1.5.1',
    'pandas==1.3.5',
    'numpy==1.26.4',
  ],
  package_data={
    'pytimbr': ['jars/*'],
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
