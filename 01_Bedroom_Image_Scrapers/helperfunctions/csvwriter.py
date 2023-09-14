import csv
import uuid

def write_csv(card_links, img_links, img_titles, filename):
    #Writes links into csv file
    with open(filename, mode='w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["id", "card_link", "title", "img_url"])
        writer.writeheader()
        for i in range(len(card_links)):
            try:
                writer.writerow({"card_link":card_links[i], "img_url":img_links[i], "id":uuid.uuid1(), "title":img_titles[i]})
            except:
                print("error at index: "+str(i))
                continue