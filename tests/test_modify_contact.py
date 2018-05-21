from model.contact import Contact


def test_modify_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    app.contact.modify_first_contact(Contact(name="New group"))


def test_modify_first_contact_header(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    app.contact.modify_first_contact(Contact(address="New header"))
