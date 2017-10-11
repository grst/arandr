from screenlayout.xrandr import XRandR
from .utils import todict
import pkg_resources


def test_state_get_hash():
    xr = XRandR()
    xr.load_from_x(pkg_resources.resource_string(__name__, 'files/xrandr_verbose01.txt'))
    assert xr.state.hash == (('LVDS1',
                              '00ffffffffffff004ca349410000000000150104901c11780a859599574f8f2621505400000001010101010101010101010101010101121b567250000c303020250024ae100000190c12567250000c303020250024ae1000001900000000000000000000000000000000000000000002000c42f20b3c6914111e6e00000000db'),
                             ('VGA1', None))
    xr.load_from_x(pkg_resources.resource_string(__name__, 'files/xrandr_verbose02.txt'))
    assert xr.state.hash == (('LVDS1',
                              '00ffffffffffff004ca349410000000000150104901c11780a859599574f8f2621505400000001010101010101010101010101010101121b567250000c303020250024ae100000190c12567250000c303020250024ae1000001900000000000000000000000000000000000000000002000c42f20b3c6914111e6e00000000db'),
                             ('VGA1',
                              '00ffffffffffff001e6d854b28360000041301036a261e78ea3231a3574c9d25115054a56b80314f454f614f81800101010101010101302a009851002a4030701300782d1100001e000000fd00384b1e530e000a202020202020000000fc004c313934320a20202020202020000000fc202020202020202020202020202000ea'))


def test_parse_raw_lines_01():
    screenline_expected = 'Screen 0: minimum 8 x 8, current 2390 x 768, maximum 32767 x 32767'
    items_expected = [
        {
            'headline': 'LVDS1 connected primary 1366x768+1024+0 (0x4a) normal (normal left inverted right x axis y axis) 280mm x 170mm',
            'EDID': '00ffffffffffff004ca349410000000000150104901c11780a859599574f8f2621505400000001010101010101010101010101010101121b567250000c303020250024ae100000190c12567250000c303020250024ae1000001900000000000000000000000000000000000000000002000c42f20b3c6914111e6e00000000db',
            'details': [
                [['1366x768', '(0x4a)', '69.300MHz', '-HSync', '-VSync', '*current', '+preferred'],
                 ' 1366', ' 768'],
                [['1366x768', '(0x122)', '46.200MHz', '-HSync', '-VSync'], ' 1366', ' 768'],
                [['1024x768', '(0x123)', '65.000MHz', '-HSync', '-VSync'], ' 1024', ' 768'],
                [['1024x576', '(0x124)', '46.995MHz', '-HSync', '+VSync'], ' 1024', ' 576'],
                [['960x540', '(0x125)', '40.784MHz', '-HSync', '+VSync'], ' 960', ' 540'],
                [['800x600', '(0x126)', '40.000MHz', '+HSync', '+VSync'], ' 800', ' 600'],
                [['800x600', '(0x127)', '36.000MHz', '+HSync', '+VSync'], ' 800', ' 600'],
                [['864x486', '(0x128)', '32.901MHz', '-HSync', '+VSync'], ' 864', ' 486'],
                [['640x480', '(0x129)', '25.175MHz', '-HSync', '-VSync'], ' 640', ' 480'],
                [['720x405', '(0x12a)', '22.176MHz', '-HSync', '+VSync'], ' 720', ' 405'],
                [['680x384', '(0x12b)', '19.677MHz', '-HSync', '+VSync'], ' 680', ' 384'],
                [['640x360', '(0x12c)', '17.187MHz', '-HSync', '+VSync'], ' 640', ' 360']]},
        {'headline': 'DP1 disconnected (normal left inverted right x axis y axis)', 'EDID': None,
         'details': []},
        {'headline': 'DP2 disconnected (normal left inverted right x axis y axis)', 'EDID': None,
         'details': []},
        {'headline': 'HDMI1 disconnected (normal left inverted right x axis y axis)', 'EDID': None,
         'details': []},
        {'headline': 'HDMI2 disconnected (normal left inverted right x axis y axis)', 'EDID': None,
         'details': []}, {
            'headline': 'VGA1 connected 1024x768+0+0 (0x123) normal (normal left inverted right x axis y axis) 0mm x 0mm',
            'EDID': None, 'details': [
                [['1024x768', '(0x123)', '65.000MHz', '-HSync', '-VSync', '*current'], ' 1024', ' 768'],
                [['800x600', '(0x126)', '40.000MHz', '+HSync', '+VSync'], ' 800', ' 600'],
                [['800x600', '(0x127)', '36.000MHz', '+HSync', '+VSync'], ' 800', ' 600'],
                [['848x480', '(0x131)', '33.750MHz', '+HSync', '+VSync'], ' 848', ' 480'],
                [['640x480', '(0x129)', '25.175MHz', '-HSync', '-VSync'], ' 640', ' 480']]},
        {'headline': 'VIRTUAL1 disconnected (normal left inverted right x axis y axis)', 'EDID': None,
         'details': []}, {'headline': '', 'EDID': None, 'details': []}
    ]
    xr = XRandR()
    screenline, items = xr._parse_raw_lines(pkg_resources.resource_string(__name__, 'files/xrandr_verbose01.txt'))
    assert screenline == screenline_expected
    assert items == items_expected


def test_parse_raw_lines_02():
    screenline_expected = 'Screen 0: minimum 8 x 8, current 2646 x 1024, maximum 32767 x 32767'
    items_expected = [
        {
            'headline': 'LVDS1 connected primary 1366x768+1280+0 (0x4a) normal (normal left inverted right x axis y axis) 280mm x 170mm',
            'EDID': '00ffffffffffff004ca349410000000000150104901c11780a859599574f8f2621505400000001010101010101010101010101010101121b567250000c303020250024ae100000190c12567250000c303020250024ae1000001900000000000000000000000000000000000000000002000c42f20b3c6914111e6e00000000db',
            'details': [
                [['1366x768', '(0x4a)', '69.300MHz', '-HSync', '-VSync', '*current', '+preferred'],
                 ' 1366', ' 768'],
                [['1366x768', '(0x122)', '46.200MHz', '-HSync', '-VSync'], ' 1366', ' 768'],
                [['1024x768', '(0x123)', '65.000MHz', '-HSync', '-VSync'], ' 1024', ' 768'],
                [['1024x576', '(0x124)', '46.995MHz', '-HSync', '+VSync'], ' 1024', ' 576'],
                [['960x540', '(0x125)', '40.784MHz', '-HSync', '+VSync'], ' 960', ' 540'],
                [['800x600', '(0x126)', '40.000MHz', '+HSync', '+VSync'], ' 800', ' 600'],
                [['800x600', '(0x127)', '36.000MHz', '+HSync', '+VSync'], ' 800', ' 600'],
                [['864x486', '(0x128)', '32.901MHz', '-HSync', '+VSync'], ' 864', ' 486'],
                [['640x480', '(0x129)', '25.175MHz', '-HSync', '-VSync'], ' 640', ' 480'],
                [['720x405', '(0x12a)', '22.176MHz', '-HSync', '+VSync'], ' 720', ' 405'],
                [['680x384', '(0x12b)', '19.677MHz', '-HSync', '+VSync'], ' 680', ' 384'],
                [['640x360', '(0x12c)', '17.187MHz', '-HSync', '+VSync'], ' 640', ' 360']]},
        {'headline': 'DP1 disconnected (normal left inverted right x axis y axis)', 'EDID': None,
         'details': []},
        {'headline': 'DP2 disconnected (normal left inverted right x axis y axis)', 'EDID': None,
         'details': []},
        {'headline': 'HDMI1 disconnected (normal left inverted right x axis y axis)', 'EDID': None,
         'details': []},
        {'headline': 'HDMI2 disconnected (normal left inverted right x axis y axis)', 'EDID': None,
         'details': []}, {
            'headline': 'VGA1 connected 1280x1024+0+0 (0x138) normal (normal left inverted right x axis y axis) 380mm x 300mm',
            'EDID': '00ffffffffffff001e6d854b28360000041301036a261e78ea3231a3574c9d25115054a56b80314f454f614f81800101010101010101302a009851002a4030701300782d1100001e000000fd00384b1e530e000a202020202020000000fc004c313934320a20202020202020000000fc202020202020202020202020202000ea',
            'details': [
                [['1280x1024', '(0x138)', '108.000MHz', '+HSync', '+VSync', '*current', '+preferred'],
                 ' 1280', ' 1024'],
                [['1280x1024', '(0x139)', '135.000MHz', '+HSync', '+VSync'], ' 1280', ' 1024'],
                [['1152x864', '(0x13a)', '108.000MHz', '+HSync', '+VSync'], ' 1152', ' 864'],
                [['1024x768', '(0x13b)', '78.750MHz', '+HSync', '+VSync'], ' 1024', ' 768'],
                [['1024x768', '(0x123)', '65.000MHz', '-HSync', '-VSync'], ' 1024', ' 768'],
                [['832x624', '(0x13c)', '57.284MHz', '-HSync', '-VSync'], ' 832', ' 624'],
                [['800x600', '(0x13d)', '49.500MHz', '+HSync', '+VSync'], ' 800', ' 600'],
                [['800x600', '(0x126)', '40.000MHz', '+HSync', '+VSync'], ' 800', ' 600'],
                [['640x480', '(0x13e)', '31.500MHz', '-HSync', '-VSync'], ' 640', ' 480'],
                [['640x480', '(0x129)', '25.175MHz', '-HSync', '-VSync'], ' 640', ' 480'],
                [['720x400', '(0x13f)', '28.320MHz', '-HSync', '+VSync'], ' 720', ' 400']]},
        {'headline': 'VIRTUAL1 disconnected (normal left inverted right x axis y axis)', 'EDID': None,
         'details': []}, {'headline': '', 'EDID': None, 'details': []}
    ]
    xr = XRandR()
    screenline, items = xr._parse_raw_lines(pkg_resources.resource_string(__name__, 'files/xrandr_verbose02.txt'))
    assert screenline == screenline_expected
    assert items == items_expected


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
                                            'rotations': [{}, {}, {}, {}],
                                            'EDID': '00ffffffffffff004ca349410000000000150104901c11780a859599574f8f2621505400000001010101010101010101010101010101121b567250000c303020250024ae100000190c12567250000c303020250024ae1000001900000000000000000000000000000000000000000002000c42f20b3c6914111e6e00000000db'},
                                  'VGA1': {'connected': True,
                                           'modes': [[1280, 1024],
                                                     [1152, 864],
                                                     [1024, 768],
                                                     [832, 624],
                                                     [800, 600],
                                                     [640, 480],
                                                     [720, 400]],
                                           'name': 'VGA1',
                                           'rotations': [{}, {}, {}, {}],
                                           'EDID': "00ffffffffffff001e6d854b28360000041301036a261e78ea3231a3574c9d25115054a56b80314f454f614f81800101010101010101302a009851002a4030701300782d1100001e000000fd00384b1e530e000a202020202020000000fc004c313934320a20202020202020000000fc202020202020202020202020202000ea"},
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
                                            'rotations': [{}, {}, {}, {}],
                                            'EDID': '00ffffffffffff004ca349410000000000150104901c11780a859599574f8f2621505400000001010101010101010101010101010101121b567250000c303020250024ae100000190c12567250000c303020250024ae1000001900000000000000000000000000000000000000000002000c42f20b3c6914111e6e00000000db'},
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
