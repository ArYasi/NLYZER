from rich.prompt import Prompt
from rich.console import Console
import subprocess

def scan_handler(target_address):
    scan_choice = Prompt.Confirm.ask('Do you want to use a custom scan?')

    with Console().status("[bold red]Scanning target machine(s)...", spinner='aesthetic') as status:
        subprocess.check_output(f'nmap -sS {target_address} -oX ./results.xml', shell=True)
