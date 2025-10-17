import csv
import time
books = []
FILENAME = 'myList.csv'



def displayBooks():
    while True:
        try:
            file = open(FILENAME, 'r')
            print('File found')
            reader = csv.DictReader(file)
            for line in reader:
                print(line)
                books.append(dict(line))
            print()
            file.close()
            break

        except FileNotFoundError:
            print('Books Not Found!')
            print('Creating new file')
            print('Please wait...')
            time.sleep(3)
            with open(FILENAME,"w",newline="") as csvfile:  # w for write
                headernames=["Title", "Author", "Description"]
                writer=csv.DictWriter(csvfile,headernames)
                writer.writeheader()
                # Default booklist
                writer.writerow({'Title':'The Rosie Project', 'Author':'Graeme Simsion', 'Description': 'A quirky romantic comedy'})
                writer.writerow({'Title':'Spiderman', 'Author':'Stan Lee', 'Description': 'A superhero story showing the importance of responsibility'})
                writer.writerow({'Title':'Invincible', 'Author':'Robert Kirkman', 'Description': 'A superhero story about a boy who got his powers from his alien dad'})
                writer.writerow({'Title':'The Chronicles of Narnia', 'Author':'C.S.Lewis', 'Description': 'Follows children who discover a magical land called Narnia'})




def addBooks():
    while True:
        try:
            n = int(input("Enter the number of entries: "))  # n represents number of entries
            if n <= 0:
                print('INVALID ENTRY!!! PLEASE ENTER A NUMBER BIGGER THAN 0.')
                continue

            for no in range(n):
                title = input("Enter Title: ")
                author = input("Enter Author Name: ")
                description = input("Enter Description: ")
                newBooks = {'Title': title, 'Author': author,'Description': description}  # creates newBooks dictionary
                books.append(newBooks)  # appends newBooks dictionary to previous books dictionary
                print('New book added.')

                # saves the new additions. writes new row
                with open(FILENAME,"a",newline="") as csvfile:  # a for append, see https://www.w3schools.com/python/python_file_write.asp
                    headernames=["Title", "Author", "Description"]
                    writer=csv.DictWriter(csvfile,headernames)
                    writer.writerow(newBooks)
            break

        except ValueError:
            print('Please enter a number')



def removeBooks():
    title = input('Enter the title of the book you want to remove: ')
    
    for book in books:
        if book['Title'].lower() == title.lower():
            books.remove(book)
            time.sleep(3)
            print('Book deleted successfully.')
            # writes the booklist without the removed book
            with open(FILENAME,"w",newline="") as csvfile:  #w for write
                headernames=["Title", "Author", "Description"]
                writer=csv.DictWriter(csvfile,headernames)
                writer.writeheader()
                for book in books:
                    writer.writerow(book)
            return

    print('Book not found.')  

            

#User's input
while True:
    print('Would you like to:')
    print('1. Display our current library')
    print('2. Add some books')
    print('3. Remove some books')
    print('4. Exit')
    choice = input('Enter your choice between 1-4: ')
    
    if choice == '1':
        displayBooks()
    elif choice == '2':
        addBooks()
    elif choice == '3':
        removeBooks()
    elif choice.lower() == '4':
        print('Exiting...')
        time.sleep(1)
        print('Thank you')
        break
    else:
        print('INVALID ENTRY!!! Please try again.')

    
