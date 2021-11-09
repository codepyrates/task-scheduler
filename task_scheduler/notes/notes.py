import pandas as pd
import time


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

        self.notes = pd.read_csv('./task_scheduler/notes/notes.csv')

    def add_note(self, title, content):
        """ Function to add notes in the notes page """

        self.notes = self.notes.append(
            {"title": title, "content": content}, ignore_index=True)

    def view_notes(self):
        """ Function viewing notes saved in notes page """

        records = list(self.notes.to_records(index=True))
        for index, title, content in records:
            print(f"{index}. {title}\n  {content}")

    def delete_note(self, index):
        self.notes.drop(index, inplace=True)
        self.notes.reset_index(drop=True, inplace=True)

    def modify_note(self, index, newtitle, newcontent):
        """ Function modifying notes in notes page"""

        self.notes.iloc[index]['title'] = newtitle
        self.notes.iloc[index]['content'] = newcontent

    def save_note(self):
        self.notes.to_csv('./task_scheduler/notes/notes.csv',
                          header=True, index=False, mode='w')

    def start(self):
        while True:
            self.view_notes()
            print(
                'Options { a: add new note    d: delete note    m: modify note    q: quit }')

            choice = input("➤➤➤   ")

            if choice == "q":
                break

            elif choice == "a":
                print("Enter the title of the new note:")
                title = input("➤➤➤   ")
                print("Type the content of the new note:")
                content = input("➤➤➤   ")
                self.add_note(title, content)
                print('Note added successfully!')

            elif choice == "d":
                print("Enter the number of the note you want to delete:")
                num = input("➤➤➤   ")
                self.delete_note(int(num))
                print(f"Note number {num} has been deleted successfully!")

            elif choice == 'm':
                print("Enter the number of the note you want to modify:")
                index = int(input("➤➤➤   "))
                print("Enter the new title for the note:")
                newtitle = input(f"➤➤➤   ")
                print("Type the new content for the note:")
                newcontent = input(f"➤➤➤   ")
                self.modify_note(index, newtitle, newcontent)
                print(f"note number {index} has been modified successfully!")

            else:
                print("Please choose one of the available choices!")


if __name__ == "__main__":

    handler = NotesHandler()
    handler.start()
