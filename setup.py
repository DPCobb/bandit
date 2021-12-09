from setuptools import setup

setup(
    name='bandit',
    version='1.0.0',
    py_modules=['bandit', 'parser'],
    install_requires=[
        'Click', 'pyautogui'
    ],
    entry_points={
        'console_scripts': [
            'bandit = bandit:main',
        ],
    },
)
