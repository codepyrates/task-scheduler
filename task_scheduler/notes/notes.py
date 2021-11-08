import csv
import pandas as pd


class Notes:

    def __init__(self, title, content):
        self.title = title
        self.content = content
    def update_title(self, new_title):
        self.title = new_title
    def update_content(self, new_content):
        self.content = new_content
    def __str__(self):
        return f"Title > {self.title} & Content > {self.content}"

class NotesHandler:

    def __init__(self):

        self.notes = pd.read_csv('./notes.csv')

    def add_note(self, title, content):
        self.notes = self.notes.append({"Title": title, "Content": content}, ignore_index=True)

    def view_notes(self):

        records = list(self.notes.to_records(index=True))
        for index, title, content in records:
            print(f"{index}. {title}\n  {content}")



if __name__ == "__main__":

    handler = NotesHandler()
    
    while True:

        choice = input("a: Add new note, v: View notes, d: Delete note, m: modify, q: quit,  >>> ")
        if choice == "q": break

        elif choice == "a":
            title = input("Title of the new note >>> ")
            content = input("Content of the new note >>> ")
            handler.add_note(title, content)
            print('Note added successfully!')

        elif choice == "v":
            handler.view_notes()
        
        
        else:
            print("Please choose one of the available choices")