from django.urls import reverse
import json

def test_hello_world():
    assert 'hello_world' == 'hello_world'
    assert 'bad' != 'Bad'

def test_fist_view(client):
    url = reverse('first_view')
    response = client.get(url)
    context = json.loads(response)

    assert response.status_code == 200
    assert context['ping'] == 'pong'

