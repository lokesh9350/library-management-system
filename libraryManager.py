def menu():
    print("\n"*2)
    print("1.Add book")
    print("2.View book")
    # print("3.Search book")
    # print("4.Delete book")
    print("3.Exit")

def add_book(ids,name,author):
    bid=input("Enter book id:")
    bname=input("Enter book name:")
    bauthor=input("Enter book author:")

    ids.append(bid)
    name.append(bname)
    author.append(bauthor)

    print("book added successfully")

def view_book(ids,name,author):
    if len(ids)==0:
        print("No book available")
        return
    print("="*8 + "Books" + "="*8)
    for i in range(len(ids)):
        print("Book ",i+1,"ID :",ids[i])
        print("Book ",i+1,"Name :",name[i])
        print("Book ",i+1,"Author:",author[i])

def main():
    ids=[]
    name=[]
    author=[]
    
    while True:
        menu()
        ch=int(input("Enter Choice :"))
        if ch==1:
            add_book(ids,name,author)
        elif ch==2:
            view_book(ids,name,author)
        elif ch==3:
            print("Thank you")
            break
        
        else:
            print("Invalid Choice")
    
                             
    

        
       

   # while True:
        # menu()
        # ch=int(input("Enter Choice :"))

        # if ch==1:
        #     add_book(ids,name,author)
        # elif ch==2:
        #     view_book(ids,name,author)
        # elif ch==3:
        #     print("Thank you")
        #     break
        # else:
        #     print("Invalid Choice")
       

#
# def main():
#     menu()

if __name__=="__main__":
    main()
