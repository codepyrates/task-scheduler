from websites_to_search import wikipedia_search , britannica_search

# Start Search Option scenario
print("Welcome to search, start by typing something to search for.")
topic_search = input("Search >>>")
print(f"1.Article about {topic_search} from Wikipedia.\n2.Article about {topic_search} from Britannica.\n3.Article about {topic_search} from citizendium.")
website = int(input("Search >>>"))
if website == 1 :
    # if the user choose 1 the wikipedia function will start to give him an article from wikipedia site.
    wikipedia_search(topic_search)
    pass
    
if website == 2 :
    # if the user choose 2 the britannica function will start to give him an article from britannica site.
    britannica_search(topic_search)
    pass
    
if website == 3 :
    # if the user choose 1 the citizendium function will start to give him an article from citizendium site.
    # citizendium_search(topic_search)
    pass
# give the user some options    
print("Options:   b: go back to article list    n: save as a note  q: quit")
first_option = (input("Search >>>"))
if first_option == 'b':
    # if the user choose b it will tack him back to the list of sites so search again.
    # list_of_websites(topic_search) 
    pass
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