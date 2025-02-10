import cmd
from colorama import init, Fore, Style

init()

class MyShell(cmd.Cmd):
    intro = Fore.GREEN + "Welcome to MyShell Type 'help' to list commands." + Style.RESET_ALL
    prompt = Fore.CYAN + "myshell> " + Style.RESET_ALL

    def do_greet(self, arg):
        """Say Hello"""
        print(Fore.YELLOW + "Hello, welcome to MyShell!" + Style.RESET_ALL)

    def do_exit(self, arg):
        """Exit the shell"""
        print(Fore.RED + "Exiting MyShell..." + Style.RESET_ALL)
        return True

if __name__ == '__main__':
    MyShell().cmdloop()
