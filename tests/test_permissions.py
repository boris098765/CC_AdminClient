class TestPermissionsAPI:
    def test_permissions(self,
            client,
            get_test_permission_name,
            get_test_login,
            get_test_role_name
    ):
        test_permission_name = get_test_permission_name()

        # GET ALL 1
        response = client.permissions.get_all()
        assert response.success == True, f"Request failed. Error: {response.error}"
        permissions = response.data
        permissions_count_before_create = len(permissions)

        # CREATE PERMISSION
        response = client.permissions.create(
            name = test_permission_name
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        permission_id = response.data['id']

        # GET PERMISSION'S ROLES 1
        response = client.permissions.get_roles(
            permission_id = permission_id
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        roles = response.data
        assert len(roles) == 0

        # GET ALL 2
        response = client.permissions.get_all()
        assert response.success == True, f"Request failed. Error: {response.error}"
        permissions = response.data
        permissions_count_after_create = len(permissions)
        assert permissions_count_after_create == permissions_count_before_create + 1

        # GET BY ID
        response = client.permissions.get(
            permission_id = permission_id
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        assert response.data['id'] == permission_id

        # GET BY NAME
        response = client.permissions.get(
            name = test_permission_name
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        assert response.data['id'] == permission_id
        assert response.data['name'] == test_permission_name

        test_permission_name_2 = get_test_permission_name()

        # EDIT
        response = client.permissions.edit(
            permission_id = permission_id,
            name = test_permission_name_2
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        assert response.data['id'] == permission_id
        assert response.data['name'] == test_permission_name_2

        test_role_name = get_test_role_name()

        # CREATE TEST ROLE
        response = client.roles.create(
            name = test_role_name
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        role_id = response.data['id']

        test_user_login = get_test_login()

        # CREATE TEST USER
        response = client.users.create(
            login = test_user_login,
            name = test_user_login,
            role_id = role_id
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        user_id = response.data['id']

        # CHECK PERMISSION 1
        response = client.permissions.check(
            user_id = user_id,
            permission = test_permission_name_2
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        assert response.data == False

        # GRANT PERMISSION
        response = client.permissions.grant(
            role_id = role_id,
            permission_id = permission_id
        )
        assert response.success == True, f"Request failed. Error: {response.error}"

        # CHECK PERMISSION 2
        response = client.permissions.check(
            user_id = user_id,
            permission = test_permission_name_2
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        assert response.data == True

        # GET PERMISSION'S ROLES 2
        response = client.permissions.get_roles(
            permission_id=permission_id
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        roles = response.data
        assert len(roles) == 1
        assert roles[0]['id'] == role_id
        assert roles[0]['name'] == test_role_name

        # REVOKE PERMISSION
        response = client.permissions.revoke(
            role_id = role_id,
            permission_id = permission_id
        )
        assert response.success == True, f"Request failed. Error: {response.error}"

        # CHECK PERMISSION 3
        response = client.permissions.check(
            user_id = user_id,
            permission = test_permission_name_2
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        assert response.data == False

        # GET PERMISSION'S ROLES 3
        response = client.permissions.get_roles(
            permission_id = permission_id
        )
        assert response.success == True, f"Request failed. Error: {response.error}"
        roles = response.data
        assert len(roles) == 0

        # DELETE TEST USER
        response = client.users.delete(
            user_id = user_id
        )
        assert response.success == True, f"Request failed. Error: {response.error}"

        # DELETE TEST ROLE
        response = client.roles.delete(
            role_id = role_id
        )
        assert response.success == True, f"Request failed. Error: {response.error}"

        # DELETE PERMISSION
        response = client.permissions.delete(
            permission_id = permission_id
        )
        assert response.success == True, f"Request failed. Error: {response.error}"

        # GET ALL 3
        response = client.permissions.get_all()
        assert response.success == True, f"Request failed. Error: {response.error}"
        permissions = response.data
        permissions_count_after_delete = len(permissions)

        assert permissions_count_before_create == permissions_count_after_delete
