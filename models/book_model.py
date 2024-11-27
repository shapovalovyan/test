import json

class Book:

    
    def __init__(self):
        self.__id = 0
        self.databases = []



    def add(self):
        
        print(f"\n{'':-<10} {'':*>10} {'':->10}\n")
        print(f"{'': <7} Меню Добавление {'': >7}\n")
        print(f"{'':-<10} {'':*>10} {'':->10}\n")
        
        
        print('Для добавление в реестр необходимо ввести книгу')
        print('в формате "Название, Автор, Год" через запятую.\n')
        print('*Например: ', end='-> ')
        print('Война и Мир, Толстой Лев Николаевич, 1867.')


        text = input('Ввод: ')

        
        self.__id += 1

        text_clear = [i.strip() for i in text.split(',')]

    
        
        if len(text_clear) == 3:
            
            self.database_json = {
                
                'id': self.__id,
                'title': text_clear[0],
                'autor': text_clear[1],
                'year': int(text_clear[2]),
                'status': 'в наличии'
            },

            
            

            self.databases.extend(self.database_json)
            
            print(f'\nКнига "{text_clear[0]}" успешно записана в реестр.\n')



            with open('database.json', 'w', encoding='utf-8') as write_file:
                

                write_file.seek(0)
                write_file.write(json.dumps(self.databases,  ensure_ascii=False, indent=4))
                
        
        else:
            print('Извините, вы передали не верные данные. Повторите попытку.')




    def read(self):
        
        # print(f"\n{'':-<10} {'':*>10} {'':->10}\n")
        # print(f"{'': <7} Отображение списка книг {'': >7}\n")
        # print(f"{'':-<10} {'':*>10} {'':->10}\n")
        
            

        with open('database.json', 'r') as read_file:

            
            database = json.load(read_file)
            
            print(f"{' ':_<54}{' ':_>54}")

            print(f"{'|': <7}{'|': >7}{'|':>31}{'|':>29}{'|':>15}{'|':>19}")

            print(f"{'|': <6}id{'|': >6}"
                f"{' ':>12}title{'|':>14}"
                f"{' ':>11}autor{'|':>13}"
                f"{' ':>5}year{'|':>6}"
                f"{' ':>6}status{'|':>7}")

            print(f"{'|':_<7}{'|':_>7}{'|':_>31}{'|':_>29}{'|':_>15}{'|':_>19}")


            
            for book in database:

                
                print(f"{'|': <7}{'|': >7}{'|':>31}{'|':>29}{'|':>15}{'|':>19}")

                if len(book['title']) > 30:
                     
                        
                    print('|{txt:^12}|'.format(txt=book["id"])
                        + '{txt:.<30.27}|'.format(txt=book["title"])
                        + '{txt:*^28.26}|'.format(txt=book["autor"])
                        + '{txt:^14}|'.format(txt=book["year"])
                        + '{txt:^18}|'.format(txt=book["status"]))

                else:

                        
                    print('|{txt:^12}|'.format(txt=book["id"])
                        + '{txt:*^30}|'.format(txt=book["title"])
                        + '{txt:*^28}|'.format(txt=book["autor"])
                        + '{txt:^14}|'.format(txt=book["year"])
                        + '{txt:^18}|'.format(txt=book["status"]))


                print(f"{'|':_<7}{'|':_>7}{'|':_>31}{'|':_>29}{'|':_>15}{'|':_>19}")
                





    def search(self):
        


        print(f"\n{'':-<10} {'':*>10} {'':->10}\n")
        print(f"{'': <7} Поиск книг {'': >7}\n")
        print(f"{'':-<10} {'':*>10} {'':->10}\n")
        
            

        with open('database.json', 'r') as read_file:


            database = json.load(read_file)
            
            print(f"{' ':_<54}{' ':_>54}")

            print(f"{'|': <7}{'|': >7}{'|':>31}{'|':>29}{'|':>15}{'|':>19}")

            print(f"{'|': <6}id{'|': >6}"
                f"{' ':>12}title{'|':>14}"
                f"{' ':>11}autor{'|':>13}"
                f"{' ':>5}year{'|':>6}"
                f"{' ':>6}status{'|':>7}")

            print(f"{'|':_<7}{'|':_>7}{'|':_>31}{'|':_>29}{'|':_>15}{'|':_>19}")


            
            for book in database:



                
                print(f"{'|': <7}{'|': >7}{'|':>31}{'|':>29}{'|':>15}{'|':>19}")

                if len(book['title']) > 30:
                     
                        
                    print('|{txt:^12}|'.format(txt=book["id"])
                        + '{txt:.<30.27}|'.format(txt=book["title"])
                        + '{txt:*^28.26}|'.format(txt=book["autor"])
                        + '{txt:^14}|'.format(txt=book["year"])
                        + '{txt:^18}|'.format(txt=book["status"]))

                else:

                        
                    print('|{txt:^12}|'.format(txt=book["id"])
                        + '{txt:*^30}|'.format(txt=book["title"])
                        + '{txt:*^28}|'.format(txt=book["autor"])
                        + '{txt:^14}|'.format(txt=book["year"])
                        + '{txt:^18}|'.format(txt=book["status"]))


                print(f"{'|':_<7}{'|':_>7}{'|':_>31}{'|':_>29}{'|':_>15}{'|':_>19}")
                


    


    def delete(self):


        self.read()
            
        
        with open('database.json', 'r+', encoding='utf-8') as delete_file:


            delete_base_json = json.load(delete_file)
            


            user_input = int(input('удалить - '))

            book_id = user_input - 1
            
            

            self.databases.clear()

            for book in delete_base_json:
                
                

                if book['id'] == user_input:
                    
                    delete_base_json.pop(book_id)


                    self.databases.extend(delete_base_json)

                    
                    open('database.json', 'w').close()
                    
                    
                    delete_file.seek(0)
                    delete_file.write(json.dumps(self.databases,  ensure_ascii=False, indent=4))
                    delete_file.seek(0)


                


    def status(self):
        pass
