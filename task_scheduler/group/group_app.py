import datetime
# import yaml



store_group_details = {} 


#=======================print sentense part=============================
# in this function contan all welcoming msg and satrt ask user to choose which app group want
def print_instruction():
    """
    this function to print welcome statment
    arqument non 
    output welcoming message
    """
    print("Anton say: select your group app you would open it:")
    print("*****************************************")
    print("Select From the folowing group app:")
    group_app_containt ="""
    app_group1 ==> [vs code, notepad, google]
    app_group2 ==> [slack,  Discord, zoom, vs code]
    app_group3 ==> [calculater, google]
      
    """
    print(group_app_containt)
    print("Anton says: pleas select group name as shown above📣📣")

#=======================get app part=============================

def get_app():
    """
    this function to inter desire app group and save it in store_group_details
    arqument take get_app input
    output: store select app to store_group_details dectionary
    """
    input_group = input(">>> ")
    group_list = [{'type': "app_group1", 'app': ['vs code', 'notepad', 'google', ]},
              {'type': 'app_group2', 'app': ['slack', ' Discord', 'zoom', 'vs code', ]},
              {'type': 'app_group3', 'app': ['calculater', 'google']}]
    for group in group_list:
        if group['type'] == input_group:
            store_group_details[input_group]=group['app']
            return group['app']
    else: #new
        print ("try again")
        get_app()
    return None
#=======================get date part=============================

def get_date ():
    """
    this function to inter desire date to open app group and save it in store_group_details
    arqument none
    output: store select ate to store_group_details dectionary
    """
    print ("Enter the date in format 'dd-mm-yyyy':")
    inputDate = input(">>> ")
    try:
        inputDate2 = datetime.datetime.strptime(inputDate,"%d-%m-%Y").date() 
        store_group_details["Date"]= str(inputDate2)
                
    except:
        print ("enter date not match with the formela try it again or type quite ")
        if inputDate == "quit":
            exit()
        else:
            get_date()
#=======================get time part=============================

def get_time():
    """
    this function to inter desire time to open app group and save it in store_group_details
    arqument none
    output: store select time to store_group_details dectionary
    """
    print ("Enter the time in format 'HH:MM':")
    inputTime = input(">>> ")
    try:
        inputTimes =datetime.datetime.strptime(inputTime, '%H:%M').time()
        store_group_details["Time"]= str(inputTimes)

        
    except:
        print ("time not match with the formela try it again or type quite ")
        if inputTime == "quit":
            exit()
        else:
            get_time()


#=======================group app name part=============================
#here user inter desire app name and save it in store_group_details
def group_app_name ():
    """
    this function to inter desire name to open app group and save it in store_group_details
    arqument none
    output: store select name to store_group_details dectionary
    """
    print ("Please enter group_app name:")
    gname = input(">>> ")
    if not gname:
         #new
        print ("try again")
        group_app_name()
    else:
        store_group_details["group name"]= gname
#=======================summary part=============================

def summary_details(summary_group):
    """
    this function to inter summary to start update on detalis
    arqument input "summary"
    action: print store_group_details for user
    """
    #  if store_group_details:
    if summary_group == "summary":
        for key,val in store_group_details.items():
            if isinstance(val, list):
                print(key, ":" ," ".join(val))
            else:
                print(key, ":" , val)
        print("did you want to update on this details [Y/N] ")        
        update_check = input(">>> ") 
        if update_check == "Y" or update_check == "y":
            update_details()
        elif update_check == "N" or update_check == "n":
                    print ("no")
    else:
        # update_details()
        exit ()
#=======================update part=============================
def update_details():
    """
    here the user choose which feild he want to update
    argument non
    action ask user to inter feild he want to update and the result send to update_all_feature
    """
    print ("please select which field you want to change")
    input_details = input(">>> ")
    for item in store_group_details:
        if item == input_details: 
            
            update_all_feature(input_details)
            break
    else: 
        print ("your input dose not exist? ")
        update_details()
        # print ("your input dose not exist? ")


#=======================update all feature part===================
def update_all_feature(input_details):
    """
    based on user input send to its function
    argument varuble
    send input to it function to update on details
    """

    if input_details == "app_group1" or input_details == "app_group2" or input_details == "app_group3":
        update_group_app(input_details)
    elif input_details == "Date":
        update_date_app(input_details)
    elif input_details == "Time":
        update_time_app(input_details)
    elif input_details == "group name":
        update_group_app_name(input_details)
#=======================complet function==========================
def complet_update_function(complet_update):
    """
    argument varuble
    based on user input if enter 'y' the programme print msg and exit from excution else he will go back to update_details
    """
    if complet_update == 'Y' or complet_update == 'y' or complet_update == 'N' or complet_update == 'n':
        if complet_update == 'Y' or complet_update == 'y':
            print ("your update store successfully")
            exit()
        elif complet_update == 'N' or complet_update == 'n':
            update_details()
    else:
        complet_update = input (">>> ")
        complet_update_function(complet_update)
#=======================update_group_app==========================
def update_group_app(input_detais):
    """
    this function to up date group app
    argument varuble
    ask user to select which app he want and delet prvious one and update with new one
    """
    group_app_containt ="""
    app_group1 ==> [vs code, notepad, google]
    app_group2 ==> [slack,  Discord, zoom, vs code]
    app_group3 ==> [calculater, google]
    """
    print(group_app_containt)
    print ("Select group app name:")
    update_group_app = input(">>> ")

    
    group_list = [{'type': "app_group1", 'app': ['vs code', 'notepad', 'google', ]},
              {'type': 'app_group2', 'app': ['slack', ' Discord', 'zoom', 'vs code', ]},
              {'type': 'app_group3', 'app': ['calculater', 'google']}]
    flag=False
    saved_group_app = None
    for group in group_list:
        if group['type'] == update_group_app:
            flag =True
            saved_group_app = group['app']
        # else :
        #     exit
            # print ("inside update function", update_group_app)
    if flag :
        del store_group_details [input_detais]
        store_group_details[f'{update_group_app}'] = saved_group_app
        for key,val in store_group_details.items():
            if isinstance(val, list):
                print(key, ":" ," ".join(val))
            else:
                print(key, ":" , val)
        
    print ("did you finish update[Y/N]")
    complet_update = input (">>> ")
    complet_update_function(complet_update)
    

#=======================update_date_app==========================
def update_date_app(input_details):
    """
    this function to up update date
    argument varuble
    ask user to select which date he want and delet prvious one and update with new one
    """
    if input_details in store_group_details:
        del store_group_details ["Date"]
        get_date ()
        
    print ("did you finish update[Y/N]")
    complet_update = input (">>> ")
    complet_update_function(complet_update)
    
#=======================update_time_app==========================
def update_time_app(input_details):
    """
    this function to up update time
    argument varuble
    ask user to select which time he want and delet prvious one and update with new one
    """
    if input_details in store_group_details:
        del store_group_details ['Time']
        get_time()
        
    print ("did you finish update?[Y/N]")
    complet_update = input (">>> ")
    complet_update_function(complet_update)
#=======================update_group_name==========================
def update_group_app_name(input_details):
    """
    this function to up update time
    argument varuble
    ask user to select which time he want and delet prvious one and update with new one
    """
    if input_details in store_group_details:
        del store_group_details ['group name']
        group_app_name()
        for key,val in store_group_details.items():
            if isinstance(val, list):
                print(key, ":" ," ".join(val))
            else:
                print(key, ":" , val)
    print ("did you finish update?[Y/N]")
    complet_update = input (">>> ")
    complet_update_function(complet_update)
#=======================end=======================================
def main_senario():
    print_instruction()
    get_app()
    get_date()
    get_time()
    group_app_name()
    print("********************************************")
    print ("if you want see app group detalis pleas enter summary: ")
    summary_group = str(input(">>> "))
    while not summary_group:
         #new
        print ("try again")
        summary_group = str(input(">>> "))
    else:
        summary_details (summary_group)

if __name__ == "__main__":
    main_senario()
