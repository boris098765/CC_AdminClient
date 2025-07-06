import pytest
from datetime import datetime

from main_client import client as api_client


def get_test_login() -> str:
    return f"test_user_{datetime.now().timestamp()}"

@pytest.fixture
def client():
    return api_client

class TestUsersAPI:
    def test_CERT_user(self, client):
        test_user_login = get_test_login()

        # GET COUNT 1
        response = client.users.get_count()
        assert response.success == True
        users_count_before_create = response.data['count']

        # CREATE
        response = client.users.create(
            login = test_user_login,
            name = test_user_login,
            role_id = 1
        )
        assert response.success == True
        user_id = response.data['id']
        user_api_key = response.data['api_key']

        # GET COUNT 2
        response = client.users.get_count()
        assert response.success == True
        users_count_after_create = response.data['count']
        assert users_count_after_create == users_count_before_create + 1

        # EDIT
        test_user_login_2 = get_test_login()
        response = client.users.edit(
            user_id = user_id,
            login = test_user_login_2
        )
        assert response.success == True

        # GET BY ID
        response = client.users.get(
            user_id = user_id
        )
        assert response.success == True
        assert response.data['id'] == user_id

        # GET BY LOGIN
        response = client.users.get(
            login=test_user_login_2
        )
        assert response.success == True
        assert response.data['id'] == user_id

        # GET BY API_KEY
        response = client.users.get(
            user_api_key=user_api_key
        )
        assert response.success == True
        assert response.data['api_key'] == user_api_key

        # DELETE
        response = client.users.delete(
            user_id = user_id
        )
        assert response.success == True

        # GET COUNT 3
        response = client.users.get_count()
        assert response.success == True
        users_count_after_delete = response.data['count']
        assert users_count_after_delete == users_count_before_create
