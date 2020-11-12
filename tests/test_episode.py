from selene import have

from src.api.episode import api_create_episode


def test_can_edit_episode(auth_app, faker):
    episode_name = faker.job()
    api_create_episode(episode_name)

    auth_app \
        .main_page() \
        .open() \
        .episode_name() \
        .should(episode_name)
