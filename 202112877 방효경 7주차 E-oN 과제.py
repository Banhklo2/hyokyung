class library :
    def _init_(self, book, author, year, publisher, genre) :
        self.book = book
        self.author = author
        self.year = year
        self.publisher = publisher
        self.genre = genre
        
    def search(self) :
        data = input("도서를 검색하세요. : ")
        file.write(self.book)
        file.write(self.author)
        file.write(self.year)
        file.write(self.publisher)
        file.write(self.genre)
        while True :
            line = file.readline()
            if not line :
                break
            print(line)

    def modify(self) :
        data_s = input("수정하고 싶은 책의 이름을 입력하세요. : ")
        book_s = str(input("수정하고 싶은 분야를 [도서명, 저자, 출판연도, 출판사명, 장르] 중에서 골라 입력하시오. \n"))
        while True :
            sentence = d.book()
            if not book :
                break
            mylibrary = library.split(" ")
            if a == "도서명" :
                print(mylist[1])
            elif a == "저자" :
                print(mylist[2])
            elif a == "출판연도" :
                print(mylist[3])
            elif a == "출판사명" :
                print(mylist[4])
            elif a == "장르" :
                print(mylist[5])
            else :
                return(0)
        
    def delete(self) :
        data = input("삭제하고 싶은 책의 이름을 입력하세요. : ")

    def print_all(self) :
        print(on)

    def save(self) :
        save = input("파일을 저장하시겠습니까? : ")
        print("저장되었습니다.")

mylibrary = library()
