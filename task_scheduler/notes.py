import time
import csv
import pandas as pd

class Note:
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
        self.notes = self.notes.append({"title": title, "content": content}, ignore_index=True)
    def delete_note(self, index):
        self.notes.drop(index, inplace=True)
        self.notes.reset_index(drop=True,inplace=True)
    def view_notes(self):
        records = list(self.notes.to_records(index=True))
        for index, title, content in records:
            print(f"{index}. {title}\n  {content}")
    def modify_note(self, index, newtitle, newcontent):
        self.notes.iloc[index]['title'] = newtitle
        self.notes.iloc[index]['content'] = newcontent
    def save_to_server(self):
        self.notes.to_csv('./notes.csv', header=True, index = False, mode='w')

if __name__ == "__main__":
    
    nh = NotesHandler()
    while True:
        choice = input("q: quit, a: add, v: view, d: delete, f: dataframe, m: modify, s: server me >>> ")
        if choice == "q": break
        elif choice == "a":
            title = input("title of the new note >>> ")
            content = input("content of the new note >>> ")
            nh.add_note(title, content)
            print('Note added successfully!')
        elif choice == "v":
            nh.view_notes()
        elif choice == "d":
            num = input("enter the number of the note you want to delete >>> ")
            nh.delete_note(int(num))
            print(f"note number {num} has been deleted successfully!")
        elif choice == "f":
            print(nh.notes)
        elif choice == 'm':
            index = int(input("enter the index of the note >>>"))
            newtitle = input(f"enter the new title >>>")
            newcontent = input(f"enter the new content >>>")
            nh.modify_note(index, newtitle, newcontent)
            print(f"note number {index} has been modified successfully!" )
        elif choice == "s":
            nh.save_to_server()
            print("uploading ...")
            time.sleep(2)
            print("notes have been successfully uploaded to the server!")
        else:
            print("c'mon man be real!")