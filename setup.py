from setuptools import setup, find_packages


setup(name='petstore-api',
      version='1.0',
      description="petstore API testing",
      author='Manoj Sahu',
      author_email='manojs@hexaware.com',
      url='https://petstore.swagger.io/',
      packages=find_packages(),
      install_requires=[
          "pytest==5.4.2",
          "pytest-html==2.1.1",
          "requests==2.23.0",
      ]
      )
