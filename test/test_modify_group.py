from model.group import Group


def test_modify_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name='New Name'))
    app.session.logout()