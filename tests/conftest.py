import pytest
import os
from datetime import datetime
import main_client

@pytest.fixture
def client():
    return main_client.client

@pytest.fixture
def get_test_role_name():
    def _generate_name():
        return f"test_role_{datetime.now().timestamp()}"
    return _generate_name

@pytest.fixture
def get_test_login():
    def _generate_login():
        return f"test_user_{datetime.now().timestamp()}"
    return _generate_login

@pytest.fixture
def get_test_permission_name():
    def _generate_permission():
        return f"test_perm_{datetime.now().timestamp()}"
    return _generate_permission

def pytest_collection_modifyitems(items):
    item_order = {
        "test_users.py":       0,
        "test_roles.py":       1,
        "test_permissions.py": 2,
    }
    def get_order(item):
        test_file = os.path.basename(item.location[0])
        return item_order.get(test_file, 999)
    items.sort(key=get_order)
