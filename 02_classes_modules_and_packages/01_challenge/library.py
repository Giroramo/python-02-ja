# ここにコードを書いてください
class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, title, author):
        # 本を辞書形式で追加
        self.__books.append({"title": title, "author": author})

    def remove_book(self, title):
        # タイトルに一致する本を削除
        self.__books = [book for book in self.__books if book["title"] != title]

    def retrieve_books(self):
        # 現在の本のコレクションを返す
        return self.__books


my_library = Library()
my_library.add_book("1984", "George Orwell")
my_library.add_book("To Kill a Mockingbird", "Harper Lee")
for book in my_library.retrieve_books():
    print(book)
my_library.remove_book("1984")
for book in my_library.retrieve_books():
    print(book)