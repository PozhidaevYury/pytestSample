from selene import have

from src.api.episode import api_create_episode


def test_can_edit_episode(app, faker):
    episode_name = faker.job()
    api_create_episode(episode_name)

    app \
        .login_page() \
        .open() \
        .auth()

    app \
        .main_page() \
        .open() \
        .episode_name() \
        .should(have.text(episode_name))
