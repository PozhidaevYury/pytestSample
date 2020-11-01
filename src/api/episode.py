import requests


def api_create_episode(name):
    data = {"name": name}
    response = requests.post("http://localhost:8087/api/episodes", json=data, headers={
        "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxIiwiaXNBZG1pbiI6dHJ1ZSwibmFtZSI6ImFkbWluIiwiaWF0IjoxNjA0MjIwMjQ5LCJleHAiOjE2MDQ4MjUwNDl9.9ordOPNLgWN7IZGdG0jpaun-b2v-vZbFAutTuC8vlcI-UaE2BeAllpVggUssAPgpFBfHXlAf659zYWD7XILhhw"})

    assert response.status_code == 200
