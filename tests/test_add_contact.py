# -*- coding: utf-8 -*-
from model.contact import Contact


def test_test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact()
    app.contact.create(Contact(name="Tatiana", midname="V", lastname="Kotova", nickname="TKotova",
                               title="Quality Assurance Engineer", company="RS",
                               address="Boston, MA", home="123", mobile="456", work="789", fax="10",
                               email1="email1@tk.com", email2="email2@tk.com", email3="email3.tk.com",
                               homepage="homepage.xom", day=6, month=5, year="1984", aday=17, amonth=7,
                               ayear="2006", address2="address2", phone2="321", notes="notes"))
    app.session.logout()


def test_test_add_empty_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact()
    app.contact.create(Contact(name="", midname="", lastname="", nickname="",
                               title="", company="",
                               address="", home="", mobile="", work="", fax="",
                               email1="", email2="", email3="",
                               homepage="", day=6, month=5, year="", aday=17, amonth=7,
                               ayear="", address2="", phone2="", notes=""))
    app.session.logout()

