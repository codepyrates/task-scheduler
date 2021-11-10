from task_scheduler.topic_search.websites_to_search import list_of_websites
def search_main():
    # Start Search Option scenario
    print("Welcome to search, start by typing something to search for.")
    topic_search = input("Search >>>")
    # function that give the user a three website to choose on to search on him topic from it.
    result = ""
    result = list_of_websites(topic_search)

    # give the user some options   
    
    while True: 
        print("Options:   b: go back to article list    n: save as a note    s: search again    q: quit")
        first_option = (input("Search >>>"))
        if first_option == 'b':
            # if the user choose b it will tack him back to the list of sites so search again.
            result = list_of_websites(topic_search)
           
        if first_option == "s":
            search_main()
        if first_option == 'n':
            # call note function to save the article in their. 
            "Note function"
            #print(result)
            return result
        if first_option == 'q':
            # call main function to go back fo main when the user finish from Search topic.
            return
    
if __name__ == "__main__":
    search_main()
