from distutils.core import setup
setup(
  name = 'simpleselector',
  packages = ['simpleselector'],
  version = '1.2',
  license='MIT',
  description = 'simpleselector allows you to make selection menus in Python',
  author = 'B Game Studios',                  
  author_email = 'bgamestudios@mail.com',      
  url = 'https://bgamestudios.tk', 
  download_url = 'https://github.com/SuperBoyne/simpleselect/archive/1.2.tar.gz',
  keywords = ['Select', 'Menu', 'Simple', 'Python', 'Selection'],
  install_requires=[          
          'keyboard',
          'colorama',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
