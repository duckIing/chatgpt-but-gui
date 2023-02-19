import appdirs
import os
from gui01_convert_ico.png_bytes import *


def set_icon():
    temp_path = appdirs.user_data_dir(roaming=True)
    icon_byte_path = os.path.join(temp_path, 'con_title.png')
    with open(icon_byte_path, 'wb') as f:
        f.write(con)
    return icon_byte_path


try:
    icon_path = set_icon()

    try:
        if not os.path.exists(icon_path):
            os.makedirs(icon_path)
    except Exception as e:
        pass

except Exception as e:
    icon_path = ''
