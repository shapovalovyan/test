from .book_model import Book



class ProcessPolling:

    def __init__(self) -> None:
        self.book = Book()


    def main_menu(self):

        while True:


            print(f"\n{'':-<10} {'':*>10} {'':->10}\n")
            print(f"{'': <7} Основное меню {'': >7}\n")
            print(f"{'':-<10} {'':*>10} {'':->10}\n")

            print('Команды, меню:\n'
                '1 - Добавление книги.\n'
                '2 - Удаление книги.\n'
                '3 - Поиск книги.\n'
                '4 - Отображение всех книг.\n'
                '5 - Изменение статуса книги.\n')
            print('Введите номер команды, и попадете в соответствующее меню')
            print('*Пример: "Введите команду: -> 1"  \n')
            

            user_input = input('Введите команду: -> ')

            if user_input == '1':
                self.book.add()
            
            elif user_input == '2':
                self.book.delete()

            elif user_input == '3':
                self.book.search()

            elif user_input == '4':
                self.book.read()

            elif user_input == '5':
                self.book.status()

            else:
                print('Извините, я не знаю такую команду. Попробуйте снова.')



    def help(self):
        print('\nЯ помощник в пользовании.\n'
              'Наш сервис позволяет вам вносить данные о книгах и авторах простыми командами.\n'
              'Мы вносим книгу в реестр и после вам доступно '
              'добавлять/удалять/искать/отображать книгу и так же изменять статусы книг.\n')
        

        print('Для взаимодействия с сервисом требудется перейти в меню.')
        print('Для перехода в основное меню нажмите клавишу 1 \n')
        
        
        user_input = int(input('Ввод -> '))

    
        if isinstance(user_input, int):
                    
                    if user_input == 1:
                        self.main_menu()

                    if user_input != 1:
                        print('Извините, недопустимое знаечение. Попробуйте заново.')



        elif isinstance(user_input, (tuple, set, list, dict, str)):
            
                    print('Извините, недопустимое знаечение. Попробуйте ввести 0 для меню Help.')



    def start_polling(self):
        print()
        print(f"{'':+<10} {'': >3} {'':*>50} {'': >3} {'':*>10}\n")
        print(f"{'':<13} Электронная система управления библиотекой Effective Mobile!\n")
        print(f"{'':+<10} {'': >3} {'':*>50} {'': >3} {'':*>10}")

        print('\nНаш сервис предоставляет функционал:\n'
              '- Добавление книг.\n'
              '- Удаление книг.\n'
              '- Поиск книг.\n')
        
        print('Для перехода в основное меню, нажмите клавишу 1.')
        print('Или 0 для команды Help.\n')


        user_input = int(input('Введите команду 0 или 1: '))


        if isinstance(user_input, int):
            
            if user_input == 0:
                self.help()
                

            if user_input == 1:
                self.main_menu()
                

            if user_input > 1:
                print('Извините, недопустимое знаечение. Попробуйте ввести 0 для меню Help.')


        elif isinstance(user_input, (tuple, set, list, dict, str)):
    
            print('Извините, недопустимое знаечение. Попробуйте ввести снова.')
