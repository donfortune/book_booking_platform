import pandas as pd
from pdf import create_pdf

data = pd.read_csv('articles.csv', dtype={'id': str})

class Articles:
    def __init__(self, articles_id):
        self.articles_id = articles_id
        self.name = data.loc[data['id'] == self.articles_id, "name"].squeeze()

    def in_stock(self):
        availability = data.loc[data['id'] == self.articles_id, "in stock"].squeeze()
        print(availability)
        if availability:
            return True
        else:
            return False

    def selected_stock(self):
        print("Selected stock:", self.name)

    def reduced_stock(self):
        current_stock = data.loc[data['id'] == self.articles_id, "in stock"].squeeze()
        new_stock = current_stock - 1
        data.loc[data['id'] == self.articles_id, "in stock"] = new_stock
        data.to_csv('articles.csv', index=False)  # Save updated data to the CSV file
        return new_stock


class Receipts:
    def print_receipts(self):
        create_pdf()
        print(f"{name} has successfully bought {articles.name}")

print(data)
articles_id = input('Enter the Id:')
articles = Articles(articles_id)
if articles.in_stock():
    articles.selected_stock()
    name = input('Enter your name:')
    reduced_stock = articles.reduced_stock()
    #print("Reduced stock:", reduced_stock)

receipts = Receipts()
receipts.print_receipts()
