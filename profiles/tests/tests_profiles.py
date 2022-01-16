from django.urls import reverse
import pytest


@pytest.mark.django_db
@pytest.mark.parametrize('url, apps', [
    ['profiles:index', ('oc_lettings_site:index', 'lettings:index')]
])
def test_render_profiles(client, url, apps, create_test_user, create_test_profile):
    url = reverse(url)
    resp = client.get(url)
    urls_redirection_apps = [reverse(app) for app in apps]

    assert resp.status_code == 200

    assert b"<title>Profiles</title>" in resp.content

    assert f"""<a href="{url}{create_test_user.username}/">""".encode('utf-8') in resp.content

    for url in urls_redirection_apps:
        assert f"""<a href="{url}">""".encode('utf-8') in resp.content


@pytest.mark.django_db
@pytest.mark.parametrize('url, apps', [
    ['profiles:profile', ('oc_lettings_site:index', 'lettings:index', 'profiles:index')]
])
def test_render_profile_user_information(client, url, apps, create_test_user, create_test_profile):
    url = reverse(url, kwargs={'username': create_test_user.username})
    resp = client.get(url)
    urls_redirection_apps = [reverse(app) for app in apps]
    informations_user_profile = {'First name': create_test_user.first_name,
                                 'Last name': create_test_user.last_name,
                                 'Email': create_test_user.email,
                                 'Favorite city': create_test_profile.favorite_city}

    assert resp.status_code == 200

    assert f"""<title>{create_test_user.username}</title>""".encode('utf-8') in resp.content

    for url in urls_redirection_apps:
        assert f"""<a href="{url}">""".encode('utf-8') in resp.content

    for key, value in informations_user_profile.items():
        assert f"""<p>{key}: {value}</p>""".encode('utf-8') in resp.content
