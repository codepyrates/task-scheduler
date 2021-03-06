import requests
from bs4 import BeautifulSoup


def wikipedia_search(topic = 'cat' , back = None):
    """[search about topic from wikipedia site]

    Args:
        topic (str, optional): [topic]. Defaults to 'cat'.
        back ([type], optional): [to save base topic name]. Defaults to None.

    Returns:
        [str]: [article related with your topic]
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
            print(i.text.strip('\n'))
            # return result from wikipedia
            return i.text.strip('\n')
        else :
            text += "m"
        

    if  text == 'm':
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
        user_choices = input("> ")
        user_choices = int(user_choices)
        
        print(list_of_choices[user_choices - 1])
        wikipedia_search(list_of_choices[user_choices - 1] , topic)

def britannica_search(topic ='animal' ):
    """[search about topic from britannica site]

    Args:
        topic (str, optional): [topic]. Defaults to 'animal'.

    Returns:
        [str]: [article that related with your topic]
    """
    url = f"https://www.britannica.com/search?query={topic}"
    res = requests.get(url)
    html_text = res.text
    soup = BeautifulSoup(html_text , "html.parser")
    li = soup.find_all('li', {'class': 'mb-45'})
    for i in li :
        print(i.findChildren("div" ,recursive = False )[0].text)
        # return result from britannica
        return i.findChildren("div" ,recursive = False )[0].text
        

def citizendium_search(topic = "fish" , counter = 0):
    """[search about topic from citizendium]

    Args:
        topic (str, optional): [topic]. Defaults to "fish".
        counter (int, optional): [counter to help for search]. Defaults to 0.

    Returns:
        [str]: [article that related with your topic]
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
            print(i.text.strip('\n'))
            # return result from citicendium
            return i.text.strip('\n')
        else :
            text += "m"
        

    if  text == 'm':
        
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
        user_choices = int(input("> "))
        citizendium_search(list_of_choices[user_choices - 1] , counter)


def list_of_websites(topic_search = 'dog'):
    """[give a list of websites to search from its]

    Args:
        topic_search (str, optional): [topic]. Defaults to 'dog'.

    Returns:
        [str]: [article related with your topic and your site]
    """
    
    print(f"1.Article about {topic_search} from Wikipedia.\n2.Article about {topic_search} from Britannica.\n3.Article about {topic_search} from citizendium.")
    prompt = input("> ").lower()
    # website = '2'
    if prompt == '1' :
        # if the user choose 1 the wikipedia function will start to give him an article from wikipedia site.
        
        val = wikipedia_search(topic_search)
        return val
    if prompt == '2' :
        # if the user choose 2 the britannica function will start to give him an article from britannica site.
        val = britannica_search(topic_search)
        return val
    if prompt == '3' :
        # if the user choose 1 the citizendium function will start to give him an article from citizendium site.
        val =  citizendium_search(topic_search)
        return val
    


if __name__ == "__main__":
    
    list_of_websites("joker")