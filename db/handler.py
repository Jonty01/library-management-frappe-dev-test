import mysql.connector
import requests
from flask import *
import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="bookList"
)

class BookDb:
    def __init__(self):
        pass
    def insert_into_books(self, book_id, title, authors, avg_rating, isbn, isbn13, language_code, num_pages, rating_count, textrev_count, publ_date, publisher, count):
        cursor = db.cursor()
        sql = f"""INSERT INTO books VALUES ({book_id}, "{title}", '{authors}', {avg_rating}, '{isbn}', '{isbn13}', '{language_code}', {num_pages}, {rating_count}, {textrev_count}, '{publ_date}', "{publisher}", {count})"""
        cursor.execute(sql)
        db.commit()
        # print(cursor.rowcount, "record inserted.")
        # url = requests.get('https://frappe.io/api/method/frappe-library?page=2&title=and')
        # book_data = url.json()
        # for book in book_data['message']:
        #     book_id = (int)(book['bookID'])
        #     title = book['title']
        #     authors = book['authors']
        #     # avg_rating = (int)(book['average_rating'])
        #     avg_rating = (float)(book['average_rating'])
        #     isbn = book['isbn']
        #     isbn13 = book['isbn13']
        #     language_code = book['language_code']
        #     num_pages = (int)(book['  num_pages'])
        #     rating_count = (int)(book['ratings_count'])
        #     textrev_count = (int)(book['text_reviews_count'])
        #     publ_date = book['publication_date']
        #     publ_date = datetime.datetime.strptime(publ_date, '%m/%d/%Y').strftime('%Y-%m-%d')
        #     publisher = book['publisher']


        #     # sql = "INSERT INTO books (title, authors, isbn) VALUES (%d, %s, %s, %f, %s, %s, %s, %d, %d, %d, %s, %s)"
        #     # sql = """INSERT INTO books VALUES (%d, %s, %s, %s, %s, %s, %s, %s, %d, %s, %s, %s)"""
        #     sql = f"""INSERT INTO books VALUES ({book_id}, "{title}", '{authors}', {avg_rating}, '{isbn}', '{isbn13}', '{language_code}', {num_pages}, {rating_count}, {textrev_count}, '{publ_date}', "{publisher}")"""
        #     # val = (book_id, title, authors, avg_rating, isbn, isbn13, language_code, num_pages, rating_count, textrev_count, publ_date, publisher)
        #     cursor.execute(sql)
        #     db.commit()

    def check_if_bookid_exists(self, book_id):
        cursor = db.cursor()
        # sql = f"SELECT * FROM books WHERE book_id = {book_id}"
        sql = f"select count(book_id) from books where book_id = {book_id}"
        cursor.execute(sql)
        r = cursor.fetchall()
        if r[0][0] == 0:
            return False
        else:
            return True

    def get_books_records(self):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM books")
        return cursor.fetchall()

    def search_books(self, search_term):
        cursor = db.cursor()
        sql = f"SELECT * FROM books WHERE title LIKE '%{search_term}%' OR authors LIKE '%{search_term}%' OR publisher LIKE '%{search_term}%'"
        cursor.execute(sql)
        return cursor.fetchall()

    def search_members(self, search_term):
        cursor = db.cursor()
        sql = f"SELECT * FROM members WHERE member_name LIKE '%{search_term}%' OR member_contact LIKE '%{search_term}%' OR member_email LIKE '%{search_term}%'"
        cursor.execute(sql)
        return cursor.fetchall()

    def add_book_count(self, book_id):
        cursor = db.cursor()
        sql = f"UPDATE books SET count = count + 1 WHERE book_id = {book_id}"
        cursor.execute(sql)
        db.commit()

    def book_data(self, book_id):
        cursor = db.cursor()
        sql = f"SELECT * FROM books WHERE book_id = {book_id}"
        cursor.execute(sql)
        return cursor.fetchall()

    def get_book_count(self, book_id):
        cursor = db.cursor()
        sql = f"SELECT total_count FROM books WHERE book_id = {book_id}"
        cursor.execute(sql)
        return cursor.fetchall()

    def delete_from_books(self, book_id):
        cursor = db.cursor()
        sql = f"DELETE FROM books WHERE book_id = {book_id}"
        cursor.execute(sql)
        db.commit()

    def get_members_records(self):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM members")
        return cursor.fetchall()

    def insert_into_members(self, member_id, name, phone,  email, address, debt):
        cursor = db.cursor()
        sql = f"""INSERT INTO members VALUES ({member_id}, "{name}", '{phone}', '{email}', '{address}', {debt})"""
        cursor.execute(sql)
        db.commit()

    def update_member(self, member_id, name, phone,  email, address, debt):
        cursor = db.cursor()
        sql = f"""UPDATE members SET member_name = "{name}", member_contact = "{phone}", member_email = "{email}", member_addr = "{address}", member_debt = {debt} WHERE member_id = {member_id}"""
        cursor.execute(sql)
        db.commit()

    def update_books(self, book_id, count):
        cursor = db.cursor()
        sql = f"""UPDATE books SET count = count +{count} WHERE book_id = {book_id}"""
        cursor.execute(sql)
        db.commit()

    def delete_from_members(self, member_id):
        cursor = db.cursor()
        sql = f"DELETE FROM members WHERE member_id = {member_id}"
        cursor.execute(sql)
        db.commit()

    def get_member_debt(self, member_id):
        cursor = db.cursor()
        sql = f"SELECT member_debt FROM members WHERE member_id = {member_id}"
        cursor.execute(sql)
        return cursor.fetchall()

    def update_member_debt(self, member_id, rent):
        cursor = db.cursor()
        sql = f"UPDATE members SET member_debt = member_debt+ {rent} WHERE member_id = {member_id}"
        cursor.execute(sql)
        db.commit()

    def issue_book(self, issue_id, book_id, member_id, issue_date):
        cursor = db.cursor()
        sql = f"""INSERT INTO bookissue VALUES ({issue_id}, {book_id}, "{member_id}", "{issue_date}")"""
        cursor.execute(sql)
        db.commit()
    
    def book_return(self, return_id, issue_id, return_date, rent, ifpaid):
        cursor = db.cursor()
        # sql = f"DELETE FROM bookissue WHERE issue_id = {issue_id}"
        sql = f"INSERT INTO bookreturn VALUES ({return_id}, {issue_id}, '{return_date}', {rent}, {ifpaid})"
        cursor.execute(sql)
        db.commit()
    
    def get_bookid_from_bookissue(self, issue_id):
        cursor = db.cursor()
        sql = f"SELECT book_id FROM bookissue WHERE issue_id = {issue_id}"
        cursor.execute(sql)
        return cursor.fetchall()

    def get_memberid_from_bookissue(self, issue_id):
        cursor = db.cursor()
        sql = f"SELECT member_id FROM bookissue WHERE issue_id = {issue_id}"
        cursor.execute(sql)
        return cursor.fetchall()

    def book_issue_records(self):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM bookissue")
        return cursor.fetchall()
    
    def book_return_records(self):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM bookreturn")
        return cursor.fetchall()
    
    # def update_member_debt(self, member_id, debt):
    #     cursor = db.cursor()
    #     sql = f"UPDATE members SET member_debt = {debt} WHERE member_id = {member_id}"
    #     cursor.execute(sql)
    #     db.commit()
# d=BookDb()
# id = d.get_memberid_from_bookissue(1)
# print(id[0][0])