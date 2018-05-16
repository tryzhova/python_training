from model.contact import Contact

def test_modify_first_contact_name(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(name="New group"))
    app.session.logout()


def test_modify_first_contact_header(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(address="New header"))
    app.session.logout()
