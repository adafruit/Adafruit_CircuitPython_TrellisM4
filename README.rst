Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-trellism4/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/trellism4/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_TrellisM4/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_TrellisM4/actions/
    :alt: Build Status

This high level library provides objects that represent Trellis M4 hardware.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
--------------------

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-trellism4/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-trellism4

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-trellism4

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-trellism4

Usage Example
=============

This example prints out the coordinates of a button each time it is pressed and released:

.. code-block:: python

     import time
     import adafruit_trellism4

     trellis = adafruit_trellism4.TrellisM4Express()

     current_press = set()
     while True:
         pressed = set(trellis.pressed_keys)
         for press in pressed - current_press:
             print("Pressed:", press)
         for release in current_press - pressed:
             print("Released:", release)
         time.sleep(0.08)
         current_press = pressed

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_TrellisM4/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
