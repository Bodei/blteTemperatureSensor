import py3nextion_lib as nxlib # simple python3 library to use nextion device
import nextionApp as nxApp # initialization of the components
from time import sleep

ser = nxlib.ser
EndCom = "\xff\xff\xff"             # 3 last bits to end serial communication
look_touch = 1  # in seconds

while True:
    try:
        touch=ser.read_until(EndCom)

        if hex(touch[0]) == '0x65':
            nxlib.nx_setText(ser,nxApp.ID_temp[0],nxApp.ID_temp[1],'Pressed')
            pageID_touch = touch[1]
            compID_touch = touch[2]
            event_touch = touch[3]
            print("page= {}, component= {}, event= {}".format(pageID_touch,compID_touch,event_touch))

    except:
        pass

    finally:
        nxlib.nx_setText(ser,nxApp.ID_temp[0],nxApp.ID_temp[1],'')
        sleep(look_touch)
