from selene.support.conditions import have


def test_login_with_valid_data(app):
    app \
        .login_page() \
        .open() \
        .login_as("admin", "123456")

    app \
        .main_page() \
        .brand_element() \
        .should(have.exact_text("QAGuild"))
