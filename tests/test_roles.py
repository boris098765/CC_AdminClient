class TestRolesAPI:
    def test_roles(self,
            client,
            get_test_role_name,
            get_test_login
    ):
        test_role_name = get_test_role_name()

        # GET ALL 1
        response = client.roles.get_all()
        assert response.success == True, f"Request failed. Error: {response.error}"
        roles = response.data
        roles_count_before_create = len(roles)

        # CREATE ROLE
        response = client.roles.create(
            name = test_role_name
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        role_id = response.data['id']

        # GET ROLE'S USERS 1
        response = client.roles.get_users(
            role_id = role_id
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        users = response.data
        assert len(users) == 0

        # GET ROLE'S PERMISSIONS 1
        response = client.roles.get_permissions(
            role_id=role_id
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        permissions = response.data
        assert len(permissions) == 0

        # GET ALL 2
        response = client.roles.get_all()
        assert response.success == True, f"Request failed. Error: {response.error}"
        roles = response.data
        roles_count_after_create = len(roles)
        assert roles_count_after_create == roles_count_before_create + 1

        # GET BY ID
        response = client.roles.get(
            role_id=role_id
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        assert response.data['id'] == role_id

        # GET BY NAME
        response = client.roles.get(
            name = test_role_name
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        assert response.data['id'] == role_id
        assert response.data['name'] == test_role_name

        test_role_name_2 = get_test_role_name()

        # EDIT
        response = client.roles.edit(
            role_id = role_id,
            name = test_role_name_2
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        assert response.data['id'] == role_id
        assert response.data['name'] == test_role_name_2

        # CREATE TEST USER
        test_login = get_test_login()
        response = client.users.create(
            login=test_login,
            name=test_login,
            role_id=1
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        user_id = response.data['id']

        # GRANT
        response = client.roles.grant(
            user_id = user_id,
            role_id = role_id
        )
        assert response.success == True, f"Request failed. Error: {response.error}"

        # GET ROLE'S USERS 2
        response = client.roles.get_users(
            role_id=role_id
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        users = response.data
        assert len(users) == 1

        # GET USER
        response = client.users.get(
            user_id = user_id
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        assert response.data['id'] == user_id
        assert response.data['role_id'] == role_id

        # DELETE USER
        response = client.users.delete(
            user_id=user_id
        )
        assert response.success == True, f"Request failed. Error: {response.error}"

        # DELETE ROLE
        response = client.roles.delete(
            role_id = role_id
        )
        assert response.success == True, f"Request failed. Error: {response.error}"

        # GET ALL 3
        response = client.roles.get_all()
        assert response.success == True, f"Request failed. Error: {response.error}"
        roles = response.data
        roles_count_after_delete = len(roles)

        assert roles_count_before_create == roles_count_after_delete
