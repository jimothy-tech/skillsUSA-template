import tkinter as tk
import argparse
from tests.test import Test


class Core:
    """Core functionality"""
    def proccess_data() -> None:
        pass


class Gui(tk.Tk):
    """Gui layer"""
    def __init__(self, core) -> None:
        super().__init__()
        #store core functionality
        self.core = core
        #config
        self.title("")
        self.geometry("800x600")
        #create a main frame for everything
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

    def create_widgets(self):
        pass


def main(gui=False) -> None:
    if gui:
        Gui(Core()).mainloop()
    else:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="",
        description=""
    )
    parser.add_argument("-t", "--test", action="store_true")
    parser.add_argument("-g", "--gui", action="store_true")
    args = parser.parse_args()

    if args.test:
        Test.main(argv=[''])
    else:
        main(args.gui)