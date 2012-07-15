pyomxplayer
===========
Python wrapper module around `OMXPlayer <https://github.com/huceke/omxplayer>`_
for the Raspberry Pi.

Unlike `other implementations <https://github.com/KenT2/pyomxplayer>`_, this
module does not rely on any external scripts and FIFOs, but uses the
`pexpect module <http://pypi.python.org/pypi/pexpect/2.4>`_ for communication
with the OMXPlayer process.

CPU overhead is rather low (~3% for the Python process on my development RPi)
and the object-oriented design makes it easy to re-use in other projects.

Installation:
-------------
::

    git clone https://github.com/jbaiter/pyomxplayer.git
    python pyomxplayer/setup.py install

Example:
--------
::

    >>> from pyomxplayer import OMXPlayer
    >>> from pprint import pprint
    >>> omx = OMXPlayer('/tmp/video.mp4')
    >>> pprint(omx.__dict__)
    {'_position_thread': <Thread(Thread-5, started 1089234032)>,
    '_process': <pexpect.spawn object at 0x1a435d0>,
    'audio': {'bps': 16,
            'channels': 2,
            'decoder': 'mp3',
            'rate': 48000,
            'streams': 1},
    'chapters': 0,
    'current_audio_stream': 1,
    'current_volume': 0.0,
    'paused': True,
    'position': 0.0,
    'subtitles': 0,
    'subtitles_visible': False,
    'video': {'decoder': 'omx-mpeg4',
            'dimensions': (640, 272),
            'fps': 23.976025,
            'profile': 15,
            'streams': 1}}
    >>> omx.toggle_pause()
    >>> omx.position
    9.43
    >>> omx.stop()
