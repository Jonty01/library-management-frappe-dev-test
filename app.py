from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql.cursors
import mysql.connector
from db.handler import *

app = Flask(__name__)


@app.route('/')
def login():
    return render_template("index.html")


@app.route('/homeAdmin')
def home_admin():
    return render_template("home_admin.html")


@app.route('/viewBooks')
def view_papers_page():
    try:
        db = BookDb()
        result = db.get_books_records()
        return render_template("view_books.html", items=result, success='')
    except Exception as e:
        return render_template("view_books.html",
                               items=[],
                               cols=[],
                               success='Can\'t view Papers: ' + str(e))


@app.route('/addBooks')
def add_papers_page():
    return render_template("add_books.html", success='')


@app.route('/addBookReq', methods=['GET'])
def add_paper():
    book_id = request.args.get('book_id')
    name = request.args.get('name')
    authors = request.args.get('authors')
    avg_rating = request.args.get('avg_rating')
    isbn = request.args.get('isbn')
    isbn13 = request.args.get('isbn13')
    language_code = request.args.get('language')
    num_pages = request.args.get('pages')
    rating_count = request.args.get('ratings')
    textrev_count = request.args.get('text_reviews')
    publ_date = request.args.get('publication_date')
    publisher = request.args.get('publisher')
    count = request.args.get('count')
    if name == '' or authors == '' or authors == '' or book_id == '' or book_id == '':
        return render_template("add_books.html",
                               success='Please fill all fields.')
    try:
        db = BookDb()
        db.insert_into_books(book_id, name, authors, avg_rating, isbn, isbn13,
                             language_code, num_pages, rating_count,
                             textrev_count, publ_date, publisher, count)
        return render_template("add_books.html",
                               success='Book added successfully!')
    except Exception as e:
        return render_template("add_books.html",
                               success='Can\'t add Book: ' + str(e))


@app.route('/updateBooks')
def update_papers_page():
    return render_template("update_books.html", success='')


@app.route('/updateBookReq', methods=['GET'])
def update_paper():
    book_id = request.args.get('book_id')
    name = request.args.get('name')
    count = request.args.get('count')
    if book_id == '' or count == '':
        return render_template("update_books.html",
                               success='Please fill all fields.')
    try:
        db = BookDb()
        if db.check_if_bookid_exists(book_id):
            db.update_books(book_id, count)
            return render_template("update_books.html",
                                   success='Book updated successfully!')
        else:
            return render_template("update_books.html",
                                   success='Book ID does not exist.')
    except Exception as e:
        return render_template("update_books.html",
                               success='Can\'t update Paper: ' + str(e))


@app.route('/deleteBooks')
def delete_papers_page():
    return render_template("delete_books.html", success='')


@app.route('/deleteBookReq', methods=['GET'])
def delete_paper():
    book_id = request.args.get('book_id')
    if book_id == '':
        return render_template("delete_books.html",
                               success='Book ID Can not be empty')
    try:
        db = BookDb()
        if db.check_if_bookid_exists(book_id):
            db.delete_from_books(book_id)
            return render_template("delete_books.html",
                                   success='Book deleted successfully!')
        else:
            return render_template("delete_books.html",
                                   success='Book ID does not exist.')
    except Exception as e:
        return render_template("delete_books.html",
                               success='Can\'t delete Paper: ' + str(e))


@app.route('/viewMembers')
def view_members_page():
    try:
        db = BookDb()
        result = db.get_members_records()
        # sql = "select * from members"
        # cols = ['id', 'name', 'email
        return render_template("view_members.html", items=result, success='')
    except Exception as e:
        return render_template("view_members.html",
                               items=[],
                               cols=[],
                               success='Can\'t view Members: ' + str(e))


@app.route('/addMembers')
def add_members_page():
    return render_template("add_members.html", success='')


@app.route('/addMemberReq', methods=['GET'])
def add_member():
    member_id = request.args.get('member_id')
    name = request.args.get('name')
    contact = request.args.get('contact')
    email = request.args.get('email')
    address = request.args.get('address')
    debt = request.args.get('debt')
    if name == '' or email == '' or member_id == '' or contact == '' or address == '' or debt == '':
        return render_template("add_members.html",
                               success='Please fill all fields.')
    try:
        db = BookDb()
        db.insert_into_members(member_id, name, contact, email, address, debt)
        return render_template("add_members.html",
                               success='Member added successfully!')
    except Exception as e:
        return render_template("add_members.html",
                               success='Can\'t add Member: ' + str(e))


@app.route('/updateMembers')
def update_members_page():
    return render_template("update_members.html", success='')


@app.route('/updateMemberReq', methods=['GET'])
def update_member():
    member_id = request.args.get('member_id')
    name = request.args.get('name')
    contact = request.args.get('contact')
    email = request.args.get('email')
    address = request.args.get('address')
    debt = request.args.get('debt')
    if name == '' or email == '' or member_id == '' or contact == '' or address == '' or debt == '':
        return render_template("update_members.html",
                               success='Please fill all fields.')
    try:
        db = BookDb()
        db.update_member(member_id, name, contact, email, address, debt)
        return render_template("update_members.html",
                               success='Member updated successfully!')
    except Exception as e:
        return render_template("update_members.html",
                               success='Can\'t update Member: ' + str(e))


@app.route('/deleteMembers')
def delete_members_page():
    return render_template("delete_member.html", success='')


@app.route('/deleteMemberReq', methods=['GET'])
def delete_member():
    member_id = request.args.get('member_id')
    if member_id == '':
        return render_template("delete_member.html",
                               success='Member ID Can not be empty')
    try:
        db = BookDb()
        db.delete_from_members(member_id)
        return render_template("delete_member.html",
                               success='Member deleted successfully!')
    except Exception as e:
        return render_template("delete_member.html",
                               success='Can\'t delete Member: ' + str(e))


@app.route('/searchBooks')
def search_books_page():
    return render_template("search_books.html", success='')


@app.route('/searchBookReq', methods=['GET'])
def search_book():
    searched = request.args.get('keyword')
    if searched == '':
        return render_template("search_books.html",
                               success='Please enter a keyword')
    try:
        db = BookDb()
        result = db.search_books(searched)
        return render_template("search_books.html", items=result, success='')
    except Exception as e:
        return render_template("search_books.html",
                               items=[],
                               cols=[],
                               success='Can\'t search Books: ' + str(e))


@app.route('/searchMembers')
def search_members_page():
    return render_template("search_members.html", success='')


@app.route('/searchMemberReq', methods=['GET'])
def search_member():
    searched = request.args.get('keyword')
    if searched == '':
        return render_template("search_members.html",
                               success='Please enter a keyword')
    try:
        db = BookDb()
        result = db.search_members(searched)
        return render_template("search_members.html", items=result, success='')
    except Exception as e:
        return render_template("search_members.html",
                               items=[],
                               cols=[],
                               success='Can\'t search Members: ' + str(e))


@app.route('/bookIssue')
def book_issue_page():
    return render_template("book_issue.html", success='')


@app.route('/bookIssueReq', methods=['GET'])
def book_issue():
    issue_id = request.args.get('issue_id')
    book_id = request.args.get('book_id')
    book_name = request.args.get('bookname')
    member_id = request.args.get('member_id')
    member_name = request.args.get('membername')
    issue_date = request.args.get('issuedate')

    if member_id == '' or book_id == '' or issue_id == '' or issue_date == '':
        return render_template("book_issue.html",
                               success='Please fill all fields.')
    try:
        db = BookDb()
        db.issue_book(issue_id, book_id, member_id, issue_date)
        db.update_books(book_id, -1)
        return render_template("book_issue.html",
                               success='Book issued successfully!')
    except Exception as e:
        return render_template("book_issue.html",
                               success='Can\'t issue Book: ' + str(e))


@app.route('/bookReturn')
def book_return_page():
    return render_template("book_return.html", success='')


@app.route('/bookReturnReq', methods=['GET'])
def book_return():
    return_id = request.args.get('return_id')
    issue_id = request.args.get('issue_id')
    return_date = request.args.get('returndate')
    rent = request.args.get('rent')
    ifpaid = request.args.get('ifpaid')
    if return_id == '' or issue_id == '' or return_date == '' or rent == '' or ifpaid == '':
        return render_template("book_return.html",
                               success='Please fill all fields.')
    try:
        db = BookDb()
        db.book_return(return_id, issue_id, return_date, rent, ifpaid)
        book_id = db.get_bookid_from_bookissue(issue_id)
        member_id = db.get_memberid_from_bookissue(issue_id)
        db.update_books(book_id[0][0], 1)
        if ifpaid == '0':
            db.update_member_debt(member_id[0][0], rent)
        return render_template("book_return.html",
                               success='Book returned successfully!')
    except Exception as e:
        return render_template("book_return.html",
                               success='Can\'t return Book: ' + str(e))


@app.route('/issueRecords')
def issue_records_page():
    try:
        db = BookDb()
        result = db.book_issue_records()
        return render_template("issue_records.html", items=result, success='')
    except Exception as e:
        return render_template("issue_records.html",
                               items=[],
                               cols=[],
                               success='Can\'t fetch issue records: ' + str(e))


@app.route('/returnRecords')
def return_records_page():
    try:
        db = BookDb()
        result = db.book_return_records()
        return render_template("return_records.html", items=result, success='')
    except Exception as e:
        return render_template("return_records.html",
                               items=[],
                               cols=[],
                               success='Can\'t fetch return records: ' +
                               str(e))


if __name__ == '__main__':
    app.run(debug=True)