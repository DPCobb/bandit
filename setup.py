from setuptools import setup

setup(
    name='bandit',
    version='0.1.1',
    py_modules=['bandit'],
    install_requires=[
        'Click', 'pyautogui'
    ],
    entry_points={
        'console_scripts': [
            'bandit = bandit:main',
        ],
    },
)
