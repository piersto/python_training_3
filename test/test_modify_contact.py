from model.contact import Contact


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname='New first name'))


def test_modify_contact_middlename(app):
    app.contact.modify_first_contact(Contact(middlename='II', birthday='15'))


def test_modify_contact_birth_month(app):
    app.contact.modify_first_contact(Contact(birth_month='April'))

