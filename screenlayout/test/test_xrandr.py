from screenlayout.xrandr import XRandR
from .test_utils import todict
import pkg_resources


def test_parse_state_02():
    state_expected = {'outputs': {'DP1': {'connected': False,
                                          'modes': [],
                                          'name': 'DP1',
                                          'rotations': [{}, {}, {}, {}]},
                                  'DP2': {'connected': False,
                                          'modes': [],
                                          'name': 'DP2',
                                          'rotations': [{}, {}, {}, {}]},
                                  'HDMI1': {'connected': False,
                                            'modes': [],
                                            'name': 'HDMI1',
                                            'rotations': [{}, {}, {}, {}]},
                                  'HDMI2': {'connected': False,
                                            'modes': [],
                                            'name': 'HDMI2',
                                            'rotations': [{}, {}, {}, {}]},
                                  'LVDS1': {'connected': True,
                                            'modes': [[1366, 768],
                                                      [1024, 768],
                                                      [1024, 576],
                                                      [960, 540],
                                                      [800, 600],
                                                      [864, 486],
                                                      [640, 480],
                                                      [720, 405],
                                                      [680, 384],
                                                      [640, 360]],
                                            'name': 'LVDS1',
                                            'rotations': [{}, {}, {}, {}]},
                                  'VGA1': {'connected': True,
                                           'modes': [[1280, 1024],
                                                     [1152, 864],
                                                     [1024, 768],
                                                     [832, 624],
                                                     [800, 600],
                                                     [640, 480],
                                                     [720, 400]],
                                           'name': 'VGA1',
                                           'rotations': [{}, {}, {}, {}]},
                                  'VIRTUAL1': {'connected': False,
                                               'modes': [],
                                               'name': 'VIRTUAL1',
                                               'rotations': [{}, {}, {}, {}]}},
                      'virtual': {'max': [32767, 32767], 'min': [8, 8]}}
    xr = XRandR()
    xr.load_from_x(pkg_resources.resource_string(__name__, 'files/xrandr_verbose02.txt'))
    assert todict(xr.state) == state_expected


def test_parse_config_02():
    config_expected = {'outputs': {'DP1': {'active': False, 'primary': False},
                                   'DP2': {'active': False, 'primary': False},
                                   'HDMI1': {'active': False, 'primary': False},
                                   'HDMI2': {'active': False, 'primary': False},
                                   'LVDS1': {'active': True,
                                             'mode': [1366, 768],
                                             'position': [1280, 0],
                                             'primary': True,
                                             'rotation': {}},
                                   'VGA1': {'active': True,
                                            'mode': [1280, 1024],
                                            'position': [0, 0],
                                            'primary': False,
                                            'rotation': {}},
                                   'VIRTUAL1': {'active': False, 'primary': False}},
                       'virtual': [2646, 1024]}
    xr = XRandR()
    xr.load_from_x(pkg_resources.resource_string(__name__, 'files/xrandr_verbose02.txt'))
    assert todict(xr.configuration) == config_expected


def test_parse_state_01():
    state_expected = {'outputs': {'DP1': {'connected': False,
                                          'modes': [],
                                          'name': 'DP1',
                                          'rotations': [{}, {}, {}, {}]},
                                  'DP2': {'connected': False,
                                          'modes': [],
                                          'name': 'DP2',
                                          'rotations': [{}, {}, {}, {}]},
                                  'HDMI1': {'connected': False,
                                            'modes': [],
                                            'name': 'HDMI1',
                                            'rotations': [{}, {}, {}, {}]},
                                  'HDMI2': {'connected': False,
                                            'modes': [],
                                            'name': 'HDMI2',
                                            'rotations': [{}, {}, {}, {}]},
                                  'LVDS1': {'connected': True,
                                            'modes': [[1366, 768],
                                                      [1024, 768],
                                                      [1024, 576],
                                                      [960, 540],
                                                      [800, 600],
                                                      [864, 486],
                                                      [640, 480],
                                                      [720, 405],
                                                      [680, 384],
                                                      [640, 360]],
                                            'name': 'LVDS1',
                                            'rotations': [{}, {}, {}, {}]},
                                  'VGA1': {'connected': True,
                                           'modes': [[1024, 768], [800, 600], [848, 480], [640, 480]],
                                           'name': 'VGA1',
                                           'rotations': [{}, {}, {}, {}]},
                                  'VIRTUAL1': {'connected': False,
                                               'modes': [],
                                               'name': 'VIRTUAL1',
                                               'rotations': [{}, {}, {}, {}]}},
                      'virtual': {'max': [32767, 32767], 'min': [8, 8]}}
    xr = XRandR()
    xr.load_from_x(pkg_resources.resource_string(__name__, 'files/xrandr_verbose01.txt'))
    assert todict(xr.state) == state_expected


def test_parse_config_01():
    config_expected = {'outputs': {'DP1': {'active': False, 'primary': False},
                                   'DP2': {'active': False, 'primary': False},
                                   'HDMI1': {'active': False, 'primary': False},
                                   'HDMI2': {'active': False, 'primary': False},
                                   'LVDS1': {'active': True,
                                             'mode': [1366, 768],
                                             'position': [1024, 0],
                                             'primary': True,
                                             'rotation': {}},
                                   'VGA1': {'active': True,
                                            'mode': [1024, 768],
                                            'position': [0, 0],
                                            'primary': False,
                                            'rotation': {}},
                                   'VIRTUAL1': {'active': False, 'primary': False}},
                       'virtual': [2390, 768]}
    xr = XRandR()
    xr.load_from_x(pkg_resources.resource_string(__name__, 'files/xrandr_verbose01.txt'))
    assert todict(xr.configuration) == config_expected
