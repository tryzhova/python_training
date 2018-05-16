# -*- coding: utf-8 -*-
from model.contact import Contact


def test_test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact()
    app.contact.create(Contact(name="Tati", midname="V", lastname="Kotova", nickname="TKotova",
                               title="Quality Assurance Engineer", company="RS",
                               address="Boston, MA", home="123", mobile="456", work="789", fax="10",
                               email1="email1@tk.com", email2="email2@tk.com", email3="email3.tk.com",
                               homepage="homepage.xom", day="4", month="April", year="1984", aday="15", amonth="May",
                               ayear="2006", address2="address2", phone2="321", notes="notes"))
    app.session.logout()


def test_test_add_empty_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact()
    app.contact.create(Contact())
    app.session.logout()

