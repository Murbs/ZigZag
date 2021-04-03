import time
import traceback

spacing = 0
incrementSpacing = True
forward = ' \\\\\\\\\\'
back = '/////'

try:
    while True: 
        
        if incrementSpacing:
            print(' ' * spacing, end='')
            print(forward)
            time.sleep(0.1) 
            spacing = spacing + 1
            
            if spacing == 20:
                incrementSpacing = False

        else:
            print(' ' * spacing, end='')
            print(back)
            time.sleep(0.1)
            spacing = spacing - 1
            
            if spacing == 0:
                incrementSpacing = True
            
except Exception:
    print(traceback.format.exec())