# test_product_app.py
import requests
import json

base_url = 'http://localhost:5000/products'


def test_add_product():
    data = {
        'name': 'Produto Teste',
        'description': 'Descrição do Produto Teste',
        'price': 10.5
    }
    response = requests.post(base_url, json=data)
    assert response.status_code == 201
    assert response.json()['message'] == 'Product created successfully'
    assert 'product' in response.json()


def test_get_products():
    response = requests.get(base_url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_product():
    response = requests.get(f"{base_url}/1")
    if response.status_code == 200:
        assert 'id' in response.json()
        assert 'name' in response.json()
        assert 'description' in response.json()
        assert 'price' in response.json()
    else:
        assert response.json()['error'] == 'Product not found'


def test_update_product():
    data = {
        'name': 'Produto Atualizado',
        'description': 'Descrição Atualizada',
        'price': 15.5
    }
    response = requests.put(f"{base_url}/1", json=data)
    if response.status_code == 200:
        assert response.json()['message'] == 'Product updated successfully'
        assert 'product' in response.json()
    else:
        assert response.json()['error'] == 'Product not found'


def test_delete_product():
    response = requests.delete(f"{base_url}/1")
    if response.status_code == 200:
        assert response.json()['message'] == 'Product deleted successfully'
    else:
        assert response.json()['error'] == 'Product not found'


#python product_app.py
#pytest test_product_app.py
