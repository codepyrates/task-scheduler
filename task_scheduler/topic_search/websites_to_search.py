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