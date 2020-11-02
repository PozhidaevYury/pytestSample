from selene.support.conditions import have


def test_covid19(app):
    app \
        .covid_page() \
        .open() \
        .search_by_inn("773466902356")

    app \
        .support_page() \
        .switch_to_page() \
        .show_support_measures() \
        .info_block() \
        .should(have.text("До 30 июня включительно:"))
