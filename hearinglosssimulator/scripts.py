"""
Basic command line for HearingLossSimulator
"""




import sys
import os
import argparse



comand_list =[
    'audiodevice',
    'wifidevice',
    
]
txt_command_list = ', '.join(comand_list)


def open_audiodevice_mainwindow():
    
    from hearinglosssimulator.gui.audiodevice_mainwindow import AudioDeviceMainWindow
    import pyqtgraph as pg
    
    app = pg.mkQApp()
    win = AudioDeviceMainWindow()
    win.show()
    app.exec_()


def open_wifidevice_mainwindow():
    from hearinglosssimulator.gui.wifidevice_mainwindow import WifiDeviceMainWindow
    import pyqtgraph as pg
    
    app = pg.mkQApp()
    win = WifiDeviceMainWindow()
    win.show()
    app.exec_()
    
def hls():
    argv = sys.argv[1:]

    parser = argparse.ArgumentParser(description='hearinglosssimulator')
    parser.add_argument('command', help='command in [{}]'.format(txt_command_list), default='audiodevice', nargs='?')
    
    parser.add_argument('-i', '--input', help='working directory', default=None)
    parser.add_argument('-o', '--output', type=int, help='channel group index', default=None)
    parser.add_argument('-p', '--parameters', help='JSON parameter file', default=None)
    
    
    args = parser.parse_args(argv)
    #~ print(sys.argv)
    #~ print(args)
    #~ print(args.command)
    
    command = args.command
    if not command in comand_list:
        print('command should be in [{}]'.format(txt_command_list))
        exit()
    
    if command=='audiodevice':
        open_audiodevice_mainwindow()
    
    elif command=='wifidevice':
        open_hls_wifi()



if __name__=='__main__':
    open_audiodevice_mainwindow()
    #~ open_wifidevice_mainwindow()





    
