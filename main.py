class WebPage:
    def __init__(self, title, content, publish_date):
        self.title = title
        self.content = content
        self.publish_date = publish_date

    def display_details(self):
        print("Заголовок:", self.title)
        print("Вміст:", self.content)
        print("Дата публікації:", self.publish_date)


class WebSite:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.pages = {}

    def add_page(self, title, content, publish_date):
        new_page = WebPage(title, content, publish_date)
        self.pages[title] = new_page

    def remove_page(self, title):
        if title in self.pages:
            del self.pages[title]
            print("Сторінка '{}' видалена з сайту '{}'.".format(title, self.name))
        else:
            print("Сторінка '{}' не знайдена на сайті '{}'.".format(title, self.name))

    def display_info(self):
        print("Назва сайту:", self.name)
        print("URL:", self.url)
        print("Список сторінок:")
        if self.pages:
            for title, page in self.pages.items():
                print("-" * 20)
                page.display_details()
        else:
            print("На цьому сайті немає сторінок.")


websites = {}

while True:
    print("\nМеню:")
    print("1. Створити новий сайт.")
    print("2. Додати сторінку до сайту.")
    print("3. Видалити сторінку з сайту.")
    print("4. Показати інформацію про сайт.")
    print("5. Вийти")

    choice = int(input("Оберіть опцію: "))

    if choice == 1:
        name = input("Введіть назву сайту: ")
        url = input("Введіть URL сайту: ")
        websites[name] = WebSite(name, url)
        print("Сайт '{}' створено успішно.".format(name))
    elif choice == 2:
        if not websites:
            print("Немає створених сайтів. Спочатку створіть сайт.")
            continue
        website_name = input("Введіть назву сайту для додавання сторінки: ")
        if website_name in websites:
            title = input("Введіть заголовок сторінки: ")
            content = input("Введіть вміст сторінки: ")
            publish_date = input("Введіть дату публікації сторінки: ")
            websites[website_name].add_page(title, content, publish_date)
            print("Сторінка додана на сайт '{}' успішно.".format(website_name))
        else:
            print("Сайт '{}' не знайдено.".format(website_name))
    elif choice == 3:
        if not websites:
            print("Немає створених сайтів. Спочатку створіть сайт.")
            continue
        website_name = input("Введіть назву сайту для видалення сторінки: ")
        if website_name in websites:
            title = input("Введіть заголовок сторінки для видалення: ")
            websites[website_name].remove_page(title)
        else:
            print("Сайт '{}' не знайдено.".format(website_name))
    elif choice == 4:
        if not websites:
            print("Немає створених сайтів.")
            continue
        website_name = input("Введіть назву сайту для відображення інформації: ")
        if website_name in websites:
            websites[website_name].display_info()
        else:
            print("Сайт '{}' не знайдено.".format(website_name))
    elif choice == 5:
        print("Вихід...")
        break
    else:
        print("Неправильний вибір. Оберіть число від 1 до 5.")
