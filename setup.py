from setuptools import setup, find_packages

setup(
    name='demo_project',  # Replace with your project name
    version='0.1',  # Initial version
    packages=find_packages(),  # Automatically find packages in the project
    install_requires=[  # List dependencies here
        'numpy',  # Example dependency
        'requests',  # Another example
    ], # Specify the Python version compatibility
    author='Ashik',
    author_email='datas293@gmail.com',
    description='Another project to setup a structure',
    long_description=open('README.md').read(),  # Optional: Long description from README
    long_description_content_type='text/markdown',  # Specify README format (Markdown or reStructuredText)
    url='https://github.com/ashiknazar/demo_project.git',  # Your project's URL (e.g., GitHub)
    project_urls={  # Optional: Additional URLs like the issue tracker or documentation
        'Bug Tracker': 'https://github.com/ashiknazar/demo_project.git/issues',
    },
)
