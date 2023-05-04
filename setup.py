from distutils.core import setup

with open("README.md", "r") as f:
    readme = f.read()

setup(name='tortuemobile',
      version='0.5.2',
      description='Un module pour les tortues dans les cahiers Jupyter.',
      long_description = readme,
      long_description_content_type = "text/markdown",
      author='David Hay',
      author_email='misterhay@gmail.com',
      url='https://github.com/callysto/tortuemobile',
      packages=['tortuemobile'],
      package_data={'tortuemobile': ['tortuemobilejs/*.js']},
      classifiers=[
          'Framework :: IPython',
          'Intended Audience :: Education',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Artistic Software',
          'Topic :: Education',
      ],
      install_requires=['IPython', 'ipywidgets>=7.0.0'],
)
