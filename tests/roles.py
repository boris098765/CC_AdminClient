import pytest
from datetime import datetime

from main_client import client as api_client


def get_test_role_name() -> str:
    return f"test_role_{datetime.now().timestamp()}"

@pytest.fixture
def client():
    return api_client

class TestRolesAPI:
    def test_CERT_role(self, client):
        test_role_name = get_test_role_name()

        # GET ALL 1
        response = client.roles.get_all()
        assert response.success == True
        roles = response.data
        roles_count_before_create = len(roles)

        # CREATE
        response = client.roles.create(test_role_name)
        assert response.success == True
        role_id = response.data['id']

        # GET ALL 2
        response = client.roles.get_all()
        assert response.success == True
        roles = response.data
        roles_count_after_create = len(roles)
        assert roles_count_after_create == roles_count_before_create + 1

        # GET BY ID
        response = client.roles.get(
            role_id=role_id
        )
        assert response.success == True
        assert response.data['id'] == role_id

        # GET BY ROLE NAME
        response = client.roles.get(
            name = test_role_name
        )
        assert response.success == True
        assert response.data['name'] == test_role_name


        test_role_name_2 = get_test_role_name()

        # EDIT
        response = client.roles.edit(
            role_id = role_id,
            name = test_role_name_2
        )
        assert response.success == True
        assert response.data['id'] == role_id
        assert response.data['name'] == test_role_name_2

        # DELETE
        response = client.roles.delete(
            role_id = role_id
        )
        assert response.success == True

        # GET ALL 3
        response = client.roles.get_all()
        assert response.success == True
        roles = response.data
        roles_count_after_delete = len(roles)

        assert roles_count_before_create == roles_count_after_delete
