import datetime
import time
store_group_details = {}


def print_instruction():
    print("Welcome to App Grouping 🖥️")
    print("Please choose the group that suits you:")
    group_app_containt = """
1. VS Code, Terminal, Firefox
2. Slack, Discord, Zoom
3. Thundermail, Libreoffice
    """
    print(group_app_containt)


def get_app():
    input_group = input("➤➤➤   ")
    group_list = [{'type': "1", 'app': ['VS Code', 'Terminal', 'Firefox', ]},
                  {'type': '2', 'app': [
                      'Slack', 'Discord', 'Zoom', ]},
                  {'type': '3', 'app': ['Thundermail', 'Libreoffice']}]
    for group in group_list:
        if group['type'] == input_group:
            store_group_details[input_group] = group['app']
            return group['app']
    return None


def get_date():
    print("Enter the date in format 'DD-MM-YYYY':")
    inputDate = input("➤➤➤   ")
    try:
        inputDate2 = datetime.datetime.strptime(inputDate, "%d-%m-%Y").date()
        store_group_details["Date"] = str(inputDate2)
    except:
        print("Entered date does not match the provided format.")
        get_date()


def get_time():
    print("Enter the time in format 'HH:MM':")
    inputTime = input("➤➤➤   ")
    try:
        inputTimes = datetime.datetime.strptime(inputTime, '%H:%M').time()
        store_group_details["Time"] = str(inputTimes)
    except:
        print("Entered time does not match the provided format.")
        get_time()


def group_app_name():
    print("Enter the name of the app group you selected:")
    gname = input("➤➤➤   ")
    store_group_details["group name"] = gname


def summary_details(summary_group):
    if summary_group == "s":
        if store_group_details:
            for k, v in store_group_details.items():
                print(k, '\n', v)
        print("Would you like to update on this details [Y/N]?")
        update_check = input("➤➤➤   ")
        if update_check == "Y" or update_check == "y":
            update_details()
        elif update_check == "N" or update_check == "n":
            print("App group has been saved successfully!")
            time.sleep(0.5)
    else:
        update_details()


def update_details():
    print("Please select which field you want to change:")
    input_details = input("➤➤➤   ")
    for item in store_group_details:
        if item == input_details:
            update_all_feature(input_details)
            break
    else:
        print("your input dose not exist? ")
        update_details()
        print("your input dose not exist? ")


def update_all_feature(input_details):
    if input_details == "1" or input_details == "2" or input_details == "3":
        update_group_app(input_details)
    elif input_details == "Date":
        update_date_app(input_details)
    elif input_details == "Time":
        update_time_app(input_details)
    elif input_details == "Group Name":
        update_group_app_name(input_details)


def complet_update_function(complet_update):
    if complet_update == 'Y' or complet_update == 'y':
        print("Your update was saved successfully!")
        
        exit()
    else:
        update_details()


def update_group_app(input_detais):

    group_app_containt = """
1. VS Code, Terminal, Firefox
2. Slack,  Discord, Zoom
3. Thundermail, Libreoffice
    """
    print(group_app_containt)
    print("Select group app name:")
    update_group_app = input("➤➤➤   ")

    group_list = [{'type': "1", 'app': ['vs code', 'notepad', 'google', ]},
                  {'type': '2', 'app': [
                      'slack', ' Discord', 'zoom', 'vs code', ]},
                  {'type': '3', 'app': ['calculater', 'google']}]
    flag = False
    saved_group_app = None
    for group in group_list:
        if group['type'] == update_group_app:
            flag = True
            saved_group_app = group['app']
    if flag:

        del store_group_details[input_detais]
        store_group_details[f'{update_group_app}'] = saved_group_app
        print(store_group_details)
    print("did you finish update[Y/N]")
    complet_update = input("➤➤➤   ")
    complet_update_function(complet_update)


def update_date_app(input_details):
    if input_details in store_group_details:
        # print (True)
        del store_group_details["Date"]
        # print (store_group_details)
        get_date()
        # print (store_group_details)
        # complet update
    print("did you finish update[Y/N]")
    complet_update = input("➤➤➤   ")
    complet_update_function(complet_update)


def update_time_app(input_details):
    if input_details in store_group_details:
        del store_group_details['Time']
        # print (store_group_details)
        get_time()
        # print (store_group_details)
        # complet update
    print("did you finish update?[Y/N]")
    complet_update = input("➤➤➤   ")
    complet_update_function(complet_update)


def update_group_app_name(input_details):
    if input_details in store_group_details:
        del store_group_details['group name']
        # print (store_group_details)
        group_app_name()
        for key, val in store_group_details.items():
            if isinstance(val, list):
                print(key, ":", " ".join(val))
            else:
                print(key, ":", val)
        # print ()
         # complet update
    print("did you finish update?[Y/N]")
    complet_update = input("➤➤➤   ")
    complet_update_function(complet_update)


def main_scenario():
    print_instruction()
    get_app()
    get_date()
    get_time()
    group_app_name()
    print("If you want to view the app group's details, type 's':")
    summary_group = str(input("➤➤➤   "))
    summary_details(summary_group)
    return store_group_details


if __name__ == "__main__":
    main_scenario()
