import os, sys
from modules import menu

if __name__ == '__main__':
    try:
        if os.geteuid() == 0:
            if len(sys.argv) > 1:
                target_address = sys.argv[1]

                while True:
                    menu.menu_handler(target_address)

            else:
                raise ValueError("Usage: python ./nlyzer.py [IP Address | IP Address range]")
    
        else:
            raise PermissionError('You must be root to run this script.')

    except PermissionError as p_error:
        print(p_error)
    
    except ValueError as v_error:
        print(v_error)