import datetime
# import yaml



store_group_details = {} 


    # global store_group_details
    # store_group_details.append(group['app'])
#=======================print sentense part=============================
# in this function contan all welcoming msg and satrt ask user to choose which app group want
def print_instruction():
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
#here user inter desire app group and save it in store_group_details
def get_app():
    input_group = input(">>> ")
    group_list = [{'type': "app_group1", 'app': ['vs code', 'notepad', 'google', ]},
              {'type': 'app_group2', 'app': ['slack', ' Discord', 'zoom', 'vs code', ]},
              {'type': 'app_group3', 'app': ['calculater', 'google']}]
    for group in group_list:
        if group['type'] == input_group:
            store_group_details[input_group]=group['app']
            return group['app']
    return None
#=======================get date part=============================
#here user inter desire date and save it in store_group_details
def get_date ():
    print ("Enter the date in format 'dd-mm-yyyy':")
    inputDate = input(">>> ")
    try:
        inputDate2 = datetime.datetime.strptime(inputDate,"%d-%m-%Y").date()  
        # now we have to store new date in list
        # print(str(inputDate2))
        store_group_details["Date"]= str(inputDate2)
                
    except:
        print ("enter date not match with the formela try it again or type quite ")
        # inputDate = input("Enter the date in format 'dd-mm-yy' : ")
        if inputDate == "quit":
            exit()
        else:
            get_date()
#=======================get time part=============================
#here user inter desire time and save it in store_group_details
def get_time():
    print ("Enter the time in format 'HH:MM':")
    inputTime = input(">>> ")
    try:
        inputTimes =datetime.datetime.strptime(inputTime, '%H:%M').time()
        # print('Time:', inputTime)
        # print('Date-time:', inputTime)
        store_group_details["Time"]= str(inputTimes)

        
    except:
        print ("time not match with the formela try it again or type quite ")
        # inputTime = input("Enter the time in format '%H:%M' : ")
        if inputTime == "quit":
            exit()
        else:
            get_time()


#=======================group app name part=============================
#here user inter desire app name and save it in store_group_details
def group_app_name ():
    print ("Please enter group_app name:")
    gname = input(">>> ")
    store_group_details["group name"]= gname
#=======================summary part=============================
#here will show summary for user and he can update the details
def summary_details(summary_group):
    if summary_group == "summary":
        if store_group_details:
            for k,v in store_group_details.items():
                print(k,'\n', v)
        print("did you want to update on this details [Y/N] ")        
        update_check = input(">>> ") 
        if update_check == "Y" or update_check == "y": #if user enter y here will call update_details() function
            update_details()
        elif update_check == "N" or update_check == "n":
                    print ("no")
    else:
        update_details()
#=======================update part=============================
def update_details():# here the user choose which feild he want to update
    print ("please select which field you want to change")
    input_details = input(">>> ")
    for item in store_group_details: #check if feild exist in decionary 
        if item == input_details:  # removed ['type']
            update_all_feature(input_details) # send input_details to update_all_feature() function
            break
    else: 
        print ("your input dose not exist? ")
        update_details()
        print ("your input dose not exist? ")


#=======================update all feature part===================
def update_all_feature(input_details):
    if input_details == "app_group1" or input_details == "app_group2" or input_details == "app_group3":
    # if the user enter one of this group  "app_group1" or input_details  or  "app_group3" he will call function update_group_app(input_details) and send input_details
        update_group_app(input_details)
    elif input_details == "Date":
        update_date_app(input_details)
    elif input_details == "Time":
        update_time_app(input_details)
    elif input_details == "group name":
        update_group_app_name(input_details)
#=======================complet function==========================
def complet_update_function(complet_update):
    if complet_update == 'Y' or complet_update == 'y':
        print ("your update store successfully")
        exit()
    else:
        update_details()
#=======================update_group_app==========================
def update_group_app(input_detais):
    #here programe show group_app_containt for user to choose from them 
    group_app_containt ="""
    app_group1 ==> [vs code, notepad, google]
    app_group2 ==> [slack,  Discord, zoom, vs code]
    app_group3 ==> [calculater, google]
    """
    print(group_app_containt)
    print ("Select group app name:")
    update_group_app = input(">>> ")

    # here store_group_details will update based on user input
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
        # print (store_group_details)
        del store_group_details [input_detais]
        # print (store_group_details)
        store_group_details[f'{update_group_app}'] = saved_group_app
        print (store_group_details)
        # complet update
    print ("did you finish update[Y/N]")
    complet_update = input (">>> ")
    complet_update_function(complet_update)
    

#=======================update_date_app==========================
def update_date_app(input_details):
    if input_details in store_group_details:
        # print (True)
        del store_group_details ["Date"]
        # print (store_group_details)
        get_date ()
        # print (store_group_details)
        # complet update
    print ("did you finish update[Y/N]")
    complet_update = input (">>> ")
    complet_update_function(complet_update)
    
#=======================update_time_app==========================
def update_time_app(input_details):
    if input_details in store_group_details:
        del store_group_details ['Time']
        # print (store_group_details)
        get_time()
        # print (store_group_details)
         # complet update
    print ("did you finish update?[Y/N]")
    complet_update = input (">>> ")
    complet_update_function(complet_update)
#=======================update_group_name==========================
def update_group_app_name(input_details):
    if input_details in store_group_details:
        del store_group_details ['group name']
        # print (store_group_details)
        group_app_name()
        for key,val in store_group_details.items():
            if isinstance(val, list):
                print(key, ":" ," ".join(val))
            else:
                print(key, ":" , val)
        # print ()
         # complet update
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
    summary_details (summary_group)

if __name__ == "__main__":
    main_senario()
#     print_instruction()
#     input_group = input(">>")
#     print(get_app( input_group)) #'app_group1'
#     # print(store_group_details,"store_group_details") # store_group_details 

#     # inputDate = input("Enter the date in format 'dd-mm-yy' : ")
#     get_date()
#     # print(store_group_details,"store_group_details") # store_group_details 
    
#     # inputTime = input("Enter the date in format 'HH:MM' : ")
#     get_time()
#     # print(store_group_details,"store_group_details")

#     # # gname = input("Please enter group_app name ")
#     group_app_name()
#     print(store_group_details,"store_group_details")

#     print("********************************************")
#     summary_group = str(input("if you want see app group detalis pleas enter summary: "))
#     summary_details (summary_group)
#     # print("")