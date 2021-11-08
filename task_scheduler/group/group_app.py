import datetime
# import yaml



store_group_details = {} 
#=======================print sentense part=============================
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
def get_app( app_type):
    group_list = [{'type': "app_group1", 'app': ['vs code', 'notepad', 'google', ]},
              {'type': 'app_group2', 'app': ['slack', ' Discord', 'zoom', 'vs code', ]},
              {'type': 'app_group3', 'app': ['calculater', 'google']}]
    for group in group_list:
        if group['type'] == app_type:
            store_group_details[app_type]=group['app']
            return group['app']
    return None



#=======================end=======================================

if __name__ == "__main__":
    
    print_instruction()
    input_group = input(">>")
    print(get_app( input_group)) #'app_group1'
    print(store_group_details,"store_group_details") # store_group_details 
