import csv
import uuid


def write_csv(card_links, img_links, img_titles, filename):
    #Writes links into csv file
    with open(filename, mode='w', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["id", "card_link", "title", "img_url"])
        writer.writeheader()
        for i in range(len(card_links)):
            try:
                writer.writerow({"card_link":card_links[i], "img_url":img_links[i], "id":uuid.uuid1(), "title":img_titles[i]})
            except Exception as e:
                print(f"error at index: {str(i)} exception: {e}")
                continue


def write_csv_card_links(card_links, filename):
    #Writes links into csv file
    with open(filename, mode='w', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["card_link"])
        writer.writeheader()
        for i in range(len(card_links)):
            try:
                writer.writerow({"card_link":card_links[i]})
            except Exception as e:
                print(f"error at index: {str(i)} exception: {e}")
                continue


def write_number_of_items_done(num, filename):
    with open(filename, mode='w') as txtfile:
        txtfile.write(str(num))


def uuid_generator(list):
    uuid_list = []
    for i in range(len(list)):
        uuid_list[i] = uuid.uuid1()
    return uuid_list
    