import requests
from bs4 import BeautifulSoup


def wikipedia_search(topic , back = None):
    """
    this function is tack an topic(text) as an argument and return an
    article how descrip this topic from wikipedia
    """
    url = 'https://en.wikipedia.org/wiki'
    res = requests.get(f"{url}/{topic}")
    html_text = res.text
    soup = BeautifulSoup(html_text, "html.parser")
    citation = soup.find_all('p')
    text = ''
    if back != None:
        topic = back

    for i in citation:
        if  len(i.text) > 50 and topic.lower() in i.text.lower() :
            text += "s"
            print(i.text)
            break
        else :
            text += "m"
        

    if  text != 's':
        print("Please can you discripe exactly what you search about, Because no subject have this word alone")
        citation = soup.find_all('a')
        number_of_choices = 0
        list_of_choices = []
        for i in citation:           
            if  topic.lower() in i.text.lower() and len(i.text) > len(topic):
                number_of_choices += 1
                print(f"{number_of_choices}_{i.text}")
                list_of_choices.append(i.text)
                if number_of_choices == 5 :
                    break
        user_choices = int(input("Search >>>"))
        
        print(list_of_choices[user_choices - 1])
        wikipedia_search(list_of_choices[user_choices - 1] , topic)

def britannica_search(topic):
    url = f"https://www.britannica.com/search?query={topic}"
    res = requests.get(url)
    html_text = res.text
    soup = BeautifulSoup(html_text , "html.parser")
    li = soup.find_all('li', {'class': 'mb-45'})
    for i in li :
        print(i.findChildren("div" ,recursive = False )[0].text)
        break

def citizendium_search(topic , counter = 0):
    print(topic)
    """
    this function is tack an topic(text) as an argument and return an
    article how descrip this topic from citizendium
    """
    url = 'https://en.citizendium.org/wiki'
    res = requests.get(f"{url}/{topic}")
    html_text = res.text
    soup = BeautifulSoup(html_text, "html.parser")
    citation = soup.find_all('p')
    text = ''
    for i in citation:
        if  len(i.text) > 50 and topic.lower() in i.text.lower() :
            text += "s"
            print(i.text)
            break
        else :
            text += "m"
        

    if  text != 's':
        
        new_res = requests.get(f"https://en.citizendium.org/wiki/Special:Search/{topic}")
        new_soup = BeautifulSoup(new_res.text, "html.parser")
        citation = new_soup.find_all('div' , {"class" : "mw-search-result-heading"})
        print("Please can you discripe exactly what you search about, Because no subject have this word alone")
        
        number_of_choices = 0
        if counter !=0 :
            number_of_choices += counter
        counter += 5
        list_of_choices = []
        change_the_choices = 0
        for i in citation:
            if not('('  in i) :
               
                change_the_choices += 1
                if change_the_choices > number_of_choices  :
                    print(f"{change_the_choices-number_of_choices}_{i.text}") #.split('(')[0]
                    list_of_choices.append(i.text.split('(')[0])
                    
                if change_the_choices == counter :
                    break
        user_choices = int(input("Search >>>"))
        citizendium_search(list_of_choices[user_choices - 1] , counter)



def list_of_websites(topic_search):
    print(f"1.Article about {topic_search} from Wikipedia.\n2.Article about {topic_search} from Britannica.\n3.Article about {topic_search} from citizendium.")
    website = int(input("Search >>>"))
    if website == 1 :
        # if the user choose 1 the wikipedia function will start to give him an article from wikipedia site.
        wikipedia_search(topic_search)
    if website == 2 :
        # if the user choose 2 the britannica function will start to give him an article from britannica site.
        britannica_search(topic_search)
    if website == 3 :
        # if the user choose 1 the citizendium function will start to give him an article from citizendium site.
        citizendium_search(topic_search)