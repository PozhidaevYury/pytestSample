import requests


def api_create_episode(name):
    data = {"name": name}
    response = requests.post("http://localhost:8087/api/episodes", json=data, headers={
        "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxIiwiaXNBZG1pbiI6dHJ1ZSwibmFtZSI6ImFkbWluIiwiaWF0IjoxNjA0OTQxNjEzLCJleHAiOjE2MDU1NDY0MTN9.OLFlhIsTjKA4ogkG1-VytK9fdwU41zn1BXnpXcwKggUCm13ivOcQanGb3Z2irHFmqmCQugj3FMrUWr6yr5SEQg"})

    assert response.status_code == 200
