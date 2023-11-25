from setuptools import setup

setup(
    name="last_fm_collage_generator_bot",
    version="0.0.1",
    author="Miłosz Guglas",
    author_email="miloszweb@gmail.com",
    description="Generate LastFM collages using telegram bot",
    packages=['src'],
    install_requires=[
        'python-telegram-bot==20.6',
        'requests==2.27.0',
        'python-dotenv==0.19.0'
    ],
    entry_points={
        'console_scripts': ['run-bot=src.app:__main__']
    }
)
