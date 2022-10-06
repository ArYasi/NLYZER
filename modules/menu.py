from rich.prompt import Prompt
from enum import Enum
from modes import scan

class MENU(str, Enum):
    SCAN = 'SCAN'
    ENUMERATE = 'ENUMERATE'
    RESULTS = 'RESULTS'
    EXIT = 'EXIT'

def menu_handler(target_address):
    menu_choice = Prompt.ask("Select a menu: ", show_choices=True, show_default=True, choices=list(MENU))

    match menu_choice:
        case MENU.SCAN:
            scan.scan_handler(target_address)
        
        case MENU.ENUMERATE:
            pass
        
        case MENU.RESULTS:
            pass
        
        case MENU.EXIT:
            exit(0)