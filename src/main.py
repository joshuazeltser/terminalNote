import sys
import os
import fileutils


class TerminalNote:

    def __init__(self):
        self.file_name = os.getenv("TERMINAL_NOTE_FILE", "terminal_note")
        self.file_type = os.getenv("TERMINAL_NOTE_TYPE", "txt")
        if len(sys.argv) == 2:
            self.command = sys.argv[1]

    def select_command(self):
        if self.command == "--help":
            print("Welcome to TerminalNote!")
            print("The easy place to store notes while you code.")
        #   TODO: Write help page
        elif self.command == "--setup":
            print("Please enter filename to store notes:")
            file_name = input("filename")
            file_type = input("filetype")
            os.environ["TERMINAL_NOTE_FILE"] = file_name
            os.environ["TERMINAL_NOTE_TYPE"] = file_type
        elif self.command == "--export":
            print("This option allows for the export of the notes to a specified format")
            print("Please select from the following options:")
            export_filename = input("exported filename")
            export_destination = input("exported file type (.txt, .csv, .docx, custom")
            print("Coming soon!")
            # TODO: Implement this functionality
        elif self.command == '--clear':
            fileutils.clear_file(self.file_name, self.file_type)
        else:
            text = ' '.join(sys.argv[1:])
            fileutils.append_to_file(text, self.file_name, self.file_type)
            print("Note saved!")


def main():
    terminal_note = TerminalNote()
    terminal_note.select_command()


if __name__ == '__main__':
    main()
