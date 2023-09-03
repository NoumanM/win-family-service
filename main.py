from utils import *
import csv

def main(data):
    driver = get_chrome_driver()
    name = f'//td[@data-column-name="full_name" and text()= "{data["Name"]}"]'
    btn_click_with_action_chains(driver, name)
    btn_click_with_action_chains(driver, Elements.service_entry)
    time.sleep(5)
    select_by_text(driver, Elements.add_event_drop_down,data['Note Type'])




if __name__ == "__main__":
    data_list = get_data_from_Excel()
    for data in data_list:
        main(data)