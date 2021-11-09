from task_scheduler.topic_search.websites_to_search import list_of_websites
def search_main():
    # Start Search Option scenario
    print("Welcome to search, start by typing something to search for.")
    topic_search = input("Search >>>")
    # function that give the user a three website to choose on to search on him topic from it.
    list_of_websites(topic_search)

    # give the user some options    
    print("Options:   b: go back to article list    n: save as a note  q: quit")
    first_option = (input("Search >>>"))
    if first_option == 'b':
        # if the user choose b it will tack him back to the list of sites so search again.
        list_of_websites(topic_search)
    if first_option == 'n':
        # call note function to save the article in their. 
        "Note function"
        pass
    if first_option == 'q':
        # call main function to go back fo main when the user finish from Search topic.
        "Main function"
        print("Hello I’m Anton, I’m your assistant, to get started, just type the letter corresponding to the activity you want to do then hit enter.")
        print("Options:     s:  Search	    r:  Reminder    n:  Notes    a: App-Group    e: Entertainment   q: Quit")
        pass
    
if __name__ == "__main__":
    search_main()
